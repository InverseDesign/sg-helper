"""
CaptureProcess - 后台独立截图进程

使用 multiprocessing.Queue 传递截图数据，稳定可靠。
持续捕获指定游戏窗口的固定区域，供 HelperThread 消费。

捕获区域（窗口相对坐标）：
- role:  (130, 7)  -> (90, 15)
- blood: (100, 33) -> (118, 15)
- magic: (100, 54) -> (98, 8)
"""

import os
import sys
import time
import multiprocessing as mp
from multiprocessing import Process, Event, Value, set_executable
from typing import Optional
import numpy as np
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, QImage


# ---- 截图区域几何集中定义（捕获循环里裁剪用）----
REGIONS = {
    'role':  (130, 7,  90, 15),
    'blood': (100, 33, 118, 15),
    'magic': (100, 54, 98,  8),
}


if sys.platform == 'win32':
    _exe = sys.executable or ''
    if _exe.lower().endswith('python.exe'):
        _pythonw = os.path.join(os.path.dirname(_exe), 'pythonw.exe')
        if os.path.isfile(_pythonw):
            set_executable(_pythonw)


class CaptureProcess:
    """截图进程封装，通过 Queue 向主进程传递截图数据"""

    def __init__(self):
        self._process: Optional[Process] = None
        self._shutdown_event: Optional[Event] = None
        self._current_hwnd: Optional[Value] = None
        # 截图数据队列：(hwnd, blood_ndarray, magic_ndarray)
        self._queue: Optional[mp.Queue] = None

    def start(self, hwnd: int = 0):
        """启动截图进程，初始目标窗口为 hwnd"""
        if self._process is not None and self._process.is_alive():
            return
        self._shutdown_event = Event()
        self._current_hwnd = Value('I', hwnd)
        self._queue = mp.Queue(maxsize=2)
        self._process = Process(
            target=_capture_loop,
            args=(self._shutdown_event, self._current_hwnd, self._queue),
            name='CaptureProcess'
        )
        self._process.start()

    def stop(self):
        """停止截图进程"""
        if self._shutdown_event is not None:
            self._shutdown_event.set()
        if self._process is not None:
            self._process.join(timeout=2.0)
            if self._process.is_alive():
                self._process.terminate()
                self._process.join(timeout=1.0)
            self._process = None

    def set_hwnd(self, hwnd):
        """切换目标窗口"""
        if self._current_hwnd is not None:
            self._current_hwnd.value = hwnd if hwnd is not None else 0

    def get_queue(self) -> Optional[mp.Queue]:
        """获取截图数据队列，供 HelperThread 消费"""
        return self._queue


def _capture_loop(shutdown_event: Event, current_hwnd: Value, output_queue: mp.Queue):
    """截图进程主循环，使用 Qt 截图"""
    # pythonw.exe 下 sys.stdout / sys.stderr 为 None，print() 会抛 AttributeError。
    # 重定向到 NUL，避免子进程崩溃。子进程的 print 仅用于错误诊断，静默丢弃。
    for _s in ('stdout', 'stderr'):
        if getattr(sys, _s) is None:
            setattr(sys, _s, open(os.devnull, 'w', encoding='utf-8'))

    # 子进程中创建 QApplication（与主进程隔离）
    app = QApplication([])

    last_hwnd = 0

    # P0 #2：复用模块级 REGIONS，避免内部分配
    regions = REGIONS

    while not shutdown_event.is_set():
        hwnd = current_hwnd.value

        if hwnd != last_hwnd:
            last_hwnd = hwnd

        if hwnd == 0:
            time.sleep(0.1)
            continue

        try:
            # 全屏截图
            screen = app.primaryScreen()
            full_pixmap = screen.grabWindow(hwnd)
            # 转为 RGB888 格式，方便后续 numpy 处理
            full_img = full_pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        except Exception:
            time.sleep(0.1)
            continue

        grabbed = {}
        for name, (x, y, w, h) in regions.items():
            try:
                # 从全屏截图中裁剪对应区域，转 RGB888
                img = full_img.copy(QRect(x, y, w, h)).convertToFormat(QImage.Format_RGB888)
                # constBits() 返回 memoryview，大小 = bytesPerLine * height
                ptr = img.constBits()
                bpl = img.bytesPerLine()
                arr = np.frombuffer(ptr, dtype=np.uint8).reshape((h, bpl))
                # bytesPerLine 可能有行对齐填充，只取前 w*3 列
                arr = arr[:, :w * 3].reshape((h, w, 3)).copy()
                grabbed[name] = arr
            except Exception as e:
                print(f'[CaptureProcess] 截图失败 {name}: {e}')
                break

        if len(grabbed) == 3:
            try:
                # 4 元 tuple：1 次 put，跨进程 pickle 由 multiprocessing 透明处理
                output_queue.put((hwnd, grabbed['blood'], grabbed['magic'], grabbed['role']),
                                 block=False)
            except Exception:
                # 队列满时跳过（消费者来不及处理，丢弃旧帧）
                try:
                    output_queue.get_nowait()
                except Exception:
                    pass
                try:
                    output_queue.put((hwnd, grabbed['blood'], grabbed['magic'], grabbed['role']),
                                     block=False)
                except Exception:
                    pass

        # ~5fps（QQ 三国 2D 端游 UI 刷新有限，5fps 已足够；降频可降低时序指纹与 CPU 占用）
        time.sleep(0.2)

    app.quit()
