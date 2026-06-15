"""
GameHandler - 游戏逻辑处理器

封装 HelperThread 后台线程和像素分析逻辑，
处理血条/蓝条检测和自动按键操作。
"""

import math
import queue
import time
from typing import Optional

import numpy as np
from PySide6.QtCore import QThread

import util


class GameHandler:
    """游戏逻辑处理器 - 封装窗口状态和 HelperThread"""

    def __init__(self, window_states: dict, window_ref):
        self._window_states = window_states
        self._window = window_ref
        self._helper_thread: Optional[HelperThread] = None
        self._capture_process = None
        self._trigger_queue: Optional[queue.Queue] = None
        self._result_queue: Optional[queue.Queue] = None

    def set_capture_process(self, capture_process):
        """设置截图进程"""
        self._capture_process = capture_process

    def set_trigger_queue(self, trigger_queue):
        """设置触发队列"""
        self._trigger_queue = trigger_queue

    def set_result_queue(self, result_queue):
        """设置结果队列"""
        self._result_queue = result_queue

    def get_window_states(self):
        """获取窗口状态字典"""
        return self._window_states

    def get_window(self):
        """获取窗口引用"""
        return self._window

    def start(self):
        """启动后台工作线程"""
        if self._helper_thread is not None:
            return

        self._trigger_queue = queue.Queue()
        self._result_queue = queue.Queue()

        self._helper_thread = HelperThread(
            self._window_states,
            self._capture_process,
            self._trigger_queue,
            self._result_queue
        )
        self._helper_thread.start()

    def stop(self):
        """停止后台工作线程"""
        if self._helper_thread:
            self._helper_thread.requestInterruption()
            self._helper_thread.quit()
            self._helper_thread.wait(2000)
            self._helper_thread = None

    def gather_params(self, current_hwnd: int) -> Optional[dict]:
        """收集当前参数用于处理"""
        if not current_hwnd or current_hwnd not in self._window_states:
            return None
        state = self._window_states[current_hwnd]
        try:
            blood_pct = int(self._window.MinBloodPrecentageSelecter.currentText()) * 0.01
        except (ValueError, TypeError):
            blood_pct = 0.0
        return {
            'hwnd': current_hwnd,
            'blood_pct': blood_pct,
            'enable_blood': state.enable_blood_helper,
            'blood_key': state.blood_key,
            'enable_magic': state.enable_magic_helper,
            'magic_key': state.magic_key,
            'stuck_key_enabled': state.stuck_key_enabled,
            'tick_keys': list(state.tick_keys),
        }

    def poll_results(self):
        """消费结果队列"""
        while True:
            try:
                self._result_queue.get_nowait()
            except queue.Empty:
                break

    def trigger(self, params: dict):
        """向工作线程推送参数"""
        if self._trigger_queue:
            self._trigger_queue.put(params)

    def find_blood_pic(self, hwnd):
        """截取血条图片"""
        return util.grab_image_qt(hwnd, util.Position(100, 33), util.Rectangle(118, 15))

    def find_magic_pic(self, hwnd):
        """截取蓝条图片"""
        return util.grab_image_qt(hwnd, util.Position(100, 54), util.Rectangle(98, 8))


class HelperThread(QThread):
    """后台工作线程：执行像素分析、按键等耗时操作"""

    def __init__(self, window_states: dict, capture_process,
                 trigger_queue: queue.Queue, result_queue: queue.Queue):
        super().__init__()
        self._window_states = window_states
        self._capture_process = capture_process
        self._trigger_queue = trigger_queue
        self._result_queue = result_queue

    def run(self):
        last_hwnd = 0
        latest_hwnd = 0
        latest_blood_pct = 0.5
        latest_enable_blood = True
        latest_blood_key = 'r'
        latest_enable_magic = True
        latest_magic_key = 't'
        latest_stuck_enabled = False
        latest_tick_keys: list[str] = []

        while not self.isInterruptionRequested():
            try:
                params = self._trigger_queue.get_nowait()
                if params:
                    latest_hwnd = params['hwnd']
                    latest_blood_pct = params['blood_pct']
                    latest_enable_blood = params['enable_blood']
                    latest_blood_key = params['blood_key']
                    latest_enable_magic = params['enable_magic']
                    latest_magic_key = params['magic_key']
                    latest_stuck_enabled = params['stuck_key_enabled']
                    latest_tick_keys = list(params['tick_keys'])
            except queue.Empty:
                pass

            try:
                q = self._capture_process.get_queue()
                if q is None:
                    time.sleep(0.05)
                    continue
                hwnd, blood_arr, magic_arr, role_arr = q.get(timeout=0.1)
            except Exception:
                continue

            if latest_hwnd != hwnd:
                continue

            # 血量判断
            if blood_arr.size > 0:
                blood_pct = calc_bar_pct(blood_arr)
                self._result_queue.put(('blood', blood_pct))
                position = math.ceil(blood_arr.shape[1] * latest_blood_pct)
                if position < blood_arr.shape[1] and pixel_is_white(blood_arr, position, 0):
                    if latest_enable_blood:
                        util.press(hwnd, latest_blood_key)

            # 蓝量判断
            if magic_arr.size > 0:
                magic_pct = calc_bar_pct(magic_arr)
                self._result_queue.put(('magic', magic_pct))
                position = math.ceil(magic_arr.shape[1] * 0.3)
                if position < magic_arr.shape[1] and pixel_is_white(magic_arr, position, 0):
                    if latest_enable_magic:
                        util.press(hwnd, latest_magic_key)

            # 卡键
            if latest_stuck_enabled:
                for tick_key in latest_tick_keys:
                    if tick_key:
                        util.press(hwnd, tick_key)


def calc_bar_pct(arr) -> int:
    """计算血条/蓝条剩余百分比（0~100），numpy 向量化版"""
    if arr.size == 0:
        return 100
    h, w, _ = arr.shape
    y = h // 2
    var = arr[y].var(axis=1)
    mask = var < 100.0
    if not mask.any():
        return 100
    return int(np.argmax(mask) / w * 100)


def pixel_is_white(arr, x, y) -> bool:
    """判断像素是否为白色"""
    pixel = arr[y, x]
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
    return float(np.var([r, g, b])) < 100