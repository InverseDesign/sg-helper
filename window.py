import sys
import os
import math
import queue
import time
import subprocess
import ctypes
from ctypes import wintypes
import numpy as np
import win32api
import win32con
import win32gui
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer, QThread, Qt

from ui import Ui_MainWindow
from capture import CaptureProcess
import config

import util

# ---- 全局快捷键（RegisterHotKey，替代 keyboard.add_hotkey）----
# 不下 WH_KEYBOARD_LL 系统级钩子，由 OS 直接以 WM_HOTKEY 派发，焦点无关
HOTKEY_ID = 0x0001                      # 进程内唯一标识，任意 int
# 反引号/波浪号键的虚拟键码。win32con 在部分 pywin32 版本里没有 VK_OEM_3 名字，
# 这里直接用其标准值 0xC0，避免 AttributeError。
VK_BACKTICK = 0xC0

global app, capture_process
window = {}
current_hwnd = None  # 当前选中的窗口
capture_process: Optional[CaptureProcess] = None

# 主线程 -> worker 线程：传递本次工作的参数
trigger_queue = queue.Queue()
# worker 线程 -> 主线程：传递结果 (kind, pct)
result_queue = queue.Queue()

# 每个窗口的独立状态
class WindowState:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stuck_key_enabled = False
        self.enable_blood_helper = True
        self.enable_magic_helper = True
        self.blood_key = 'R'
        self.magic_key = 'T'
        self.tick_keys = ['A', '', '', '', '', '', '', '']  # Tick1-8

window_states = {}  # {hwnd: WindowState}


class HelperThread(QThread):
    """后台工作线程：执行像素分析、按键等耗时操作。

    截图数据由 CaptureProcess 通过 Queue 传递，这里直接消费。
    通过 trigger_queue 接收本次工作的参数（blood_pct, enable_blood, 等），
    通过 result_queue 向主线程传递 numpy 结果数组用于 UI 显示。
    """

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
            # 尝试从 trigger_queue 获取最新参数（非阻塞）
            try:
                params = trigger_queue.get_nowait()
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

            # 从截图队列获取截图
            try:
                q = capture_process.get_queue()
                if q is None:
                    time.sleep(0.05)
                    continue
                hwnd, blood_arr, magic_arr, role_arr = q.get(timeout=0.1)
            except Exception:
                continue

            if latest_hwnd != hwnd:
                continue

            # 角色截图（显示在主线程处理，这里不传递）

            # 血量判断
            if blood_arr.size > 0:
                blood_pct = calc_bar_pct(blood_arr)
                result_queue.put(('blood', blood_pct))
                position = math.ceil(blood_arr.shape[1] * latest_blood_pct)
                if position < blood_arr.shape[1] and pixel_is_white(blood_arr, position, 0):
                    if latest_enable_blood:
                        util.press(hwnd, latest_blood_key)

            # 蓝量判断
            if magic_arr.size > 0:
                magic_pct = calc_bar_pct(magic_arr)
                result_queue.put(('magic', magic_pct))
                position = math.ceil(magic_arr.shape[1] * 0.3)
                if position < magic_arr.shape[1] and pixel_is_white(magic_arr, position, 0):
                    if latest_enable_magic:
                        util.press(hwnd, latest_magic_key)

            # 卡键
            if latest_stuck_enabled:
                for tick_key in latest_tick_keys:
                    if tick_key:
                        util.press(hwnd, tick_key)




def _gather_params():
    """在主线程中收集本次工作所需的参数（避免在 worker 中访问 widget）。"""
    global current_hwnd, window_states
    if not current_hwnd or current_hwnd not in window_states:
        return None
    state = window_states[current_hwnd]
    try:
        blood_pct = int(window.MinBloodPrecentageSelecter.currentText()) * 0.01
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


def _poll_results():
    """在主线程里消费 result_queue 里的结果（目前仅用于日志/扩展）。"""
    while True:
        try:
            result_queue.get_nowait()
        except queue.Empty:
            break


def _on_timer_timeout():
    """定时器回调（在主线程）：投递给 worker 并消费结果。"""
    params = _gather_params()
    if params is not None:
        trigger_queue.put(params)
    _poll_results()

    # 在主线程中直接截图显示到 QGraphicsView（与原版逻辑一致）
    if current_hwnd:
        try:
            pic = util.grab_image_qt(current_hwnd, util.Position(130, 7), util.Rectangle(90, 15))
            util.show_pix_on_graph_view(window.CurrentRolePicture, pic)

            pic = find_blood_pic(current_hwnd)
            util.show_pix_on_graph_view(window.CurrentBloodPicture, pic)

            pic = find_magic_pic(current_hwnd)
            util.show_pix_on_graph_view(window.CurrentMagicPicture, pic)
        except Exception:
            pass


def find_blood_pic(hwnd):
    return util.grab_image_qt(hwnd, util.Position(100, 33), util.Rectangle(118, 15))


def find_magic_pic(hwnd):
    return util.grab_image_qt(hwnd, util.Position(100, 54), util.Rectangle(98, 8))


def calc_bar_pct(arr):
    """计算血条/蓝条剩余百分比（0~100），numpy 向量化版。

    性能：原 Python 循环 h*w 次 np.var → 1 次 arr[y].var(axis=1) + 1 次 np.argmax
    加速比：典型血条 118×15，~20-50x
    """
    if arr.size == 0:
        return 100
    h, w, _ = arr.shape
    y = h // 2
    var = arr[y].var(axis=1)            # shape (w,)，一次性算中间行所有像素的 RGB 方差
    mask = var < 100.0                  # bool mask，True 即"白"
    if not mask.any():
        return 100
    # np.argmax 在全 False 时返回 0，但前面已用 any() 排除这种情况
    return int(np.argmax(mask) / w * 100)


def pixel_is_white(arr, x, y):
    """判断 numpy 数组指定位置像素是否为白色（RGB方差 < 100）"""
    pixel = arr[y, x]  # shape: (height, width, 3) -> RGB
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
    return float(np.var([r, g, b])) < 100


def on_window_select(idx):
    global current_hwnd, window_states, capture_process
    hwnd = window.WindowSelecter.itemData(idx)
    current_hwnd = hwnd
    print(f"切换到窗口: {hwnd}")
    
    # 根据是否选中有效窗口，控制选项卡可见性
    _update_tab_visibility(hwnd is not None and hwnd != 0)
    
    if not hwnd:
        return
    
    # 如果这个窗口没有状态，创建一个新的
    if hwnd not in window_states:
        window_states[hwnd] = WindowState(hwnd)
    
    # 通知截图进程切换目标窗口
    if capture_process is not None:
        capture_process.set_hwnd(hwnd)
    
    # 从 UI 加载状态到 WindowState
    state = window_states[hwnd]
    state.blood_key = window.MinBloodKeySelecter.currentText()
    state.magic_key = window.MinMagicKeySelecter.currentText()
    state.tick_keys = [
        window.Tick1.currentText(),
        window.Tick2.currentText(),
        window.Tick3.currentText(),
        window.Tick4.currentText(),
        window.Tick5.currentText(),
        window.Tick6.currentText(),
        window.Tick7.currentText(),
        window.Tick8.currentText()
    ]
    
    # 更新 UI 显示当前窗口的状态
    window.StuckKeyStatus.setChecked(state.stuck_key_enabled)
    print(f"当前窗口卡键状态: {state.stuck_key_enabled}")


def _update_tab_visibility(has_window: bool):
    """根据是否选中窗口，控制选项卡可见性。未选中时只显示'开始'选项卡。"""
    tab_widget = window.tabWidget
    # tab 索引: 0=开始, 1=基本功能, 2=更多功能, 3=日常活动, 4=尽请期待
    for i in range(1, tab_widget.count()):
        tab_widget.setTabVisible(i, has_window)
        tab_widget.setTabEnabled(i, has_window)


def save_current_window_state():
    """保存当前 UI 设置到当前窗口的状态"""
    global current_hwnd, window_states
    if current_hwnd and current_hwnd in window_states:
        state = window_states[current_hwnd]
        state.blood_key = window.MinBloodKeySelecter.currentText()
        state.magic_key = window.MinMagicKeySelecter.currentText()
        state.tick_keys = [
            window.Tick1.currentText(),
            window.Tick2.currentText(),
            window.Tick3.currentText(),
            window.Tick4.currentText(),
            window.Tick5.currentText(),
            window.Tick6.currentText(),
            window.Tick7.currentText(),
            window.Tick8.currentText()
        ]
        state.enable_blood_helper = window.EnableBloodHelper.isChecked()
        state.enable_magic_helper = window.EnableMagicHelper.isChecked()


def refresh_window_list(main_window):
    """重新扫描游戏窗口，刷新选择器；尽量保留当前选中项。"""
    global current_hwnd
    prev_hwnd = current_hwnd
    main_window.WindowSelecter.blockSignals(True)
    main_window.WindowSelecter.clear()
    ws = util.find_window('QQ三国')
    for w in ws:
        main_window.WindowSelecter.addItem(w.window_text, w.hwnd)

    # 尝试恢复之前选中的窗口
    target_idx = 0
    if prev_hwnd is not None:
        for i in range(main_window.WindowSelecter.count()):
            if main_window.WindowSelecter.itemData(i) == prev_hwnd:
                target_idx = i
                break
    main_window.WindowSelecter.setCurrentIndex(target_idx)
    main_window.WindowSelecter.blockSignals(False)
    on_window_select(target_idx)


def init(main_window):
    global capture_process

    # 启动截图后台进程（程序启动时即运行）
    capture_process = CaptureProcess()
    capture_process.start()

    # 初始化窗口选择器
    refresh_window_list(main_window)
    main_window.WindowSelecter.currentIndexChanged.connect(on_window_select)
    main_window.RefreshWindowBtn.clicked.connect(lambda: refresh_window_list(main_window))
    
    # 连接 UI 变化事件，保存状态
    main_window.MinBloodKeySelecter.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.MinMagicKeySelecter.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick1.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick2.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick3.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick4.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick5.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick6.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick7.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick8.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.EnableBloodHelper.stateChanged.connect(lambda: save_current_window_state())
    main_window.EnableMagicHelper.stateChanged.connect(lambda: save_current_window_state())

    # 初始化卡键复选框
    main_window.StuckKeyStatus.stateChanged.connect(lambda: save_current_window_state())

    # 全局快捷键 CTRL+` 已由 MainWindow.__init__ 通过 win32gui.RegisterHotKey 注册，
    # WM_HOTKEY 消息由 MainWindow.nativeEvent 捕获并回调 on_ctrl_backtick_pressed
    
    # 创建后台工作线程，避免图像处理阻塞 UI
    main_window.helper_thread = HelperThread()
    main_window.helper_thread.start()

    # 定时器在主线程触发：推送参数并消费结果
    main_window.timer = QTimer()
    main_window.timer.start(200)
    main_window.timer.timeout.connect(_on_timer_timeout)

    # ---- 开始选项卡 ----
    _init_start_tab(main_window)

    # 退出时注销全局热键（用闭包捕获 main_window）
    def _unregister_hotkey():
        try:
            if main_window._hwnd:
                win32gui.UnregisterHotKey(main_window._hwnd, HOTKEY_ID)
        except Exception:
            pass

    # 应用退出时安全关闭后台线程、截图进程和全局热键
    app.aboutToQuit.connect(main_window.helper_thread.requestInterruption)
    app.aboutToQuit.connect(main_window.helper_thread.wait)
    app.aboutToQuit.connect(lambda: capture_process.stop() if capture_process else None)
    app.aboutToQuit.connect(_unregister_hotkey)


# ==================== 开始选项卡逻辑 ====================

# QQ三国游戏可执行文件名
_GAME_EXE = 'QQSG.exe'


def _init_start_tab(main_window):
    """初始化开始选项卡"""
    # 从配置加载游戏路径
    game_path = config.get_game_path()
    main_window.GamePathEdit.setText(game_path)
    _update_launch_btn(main_window, game_path)

    # 自动搜索游戏
    main_window.BtnSearchGame.clicked.connect(lambda: _on_search_game(main_window))
    # 手动选择路径
    main_window.BtnBrowsePath.clicked.connect(lambda: _on_browse_path(main_window))
    # 启动游戏
    main_window.BtnLaunchGame.clicked.connect(lambda: _on_launch_game(main_window))


def _update_launch_btn(main_window, game_path: str):
    """根据路径有效性更新启动按钮状态"""
    valid = _is_valid_game_path(game_path)
    main_window.BtnLaunchGame.setEnabled(valid)


def _is_valid_game_path(path: str) -> bool:
    """检查路径是否包含游戏可执行文件"""
    if not path:
        return False
    return os.path.isfile(os.path.join(path, _GAME_EXE))


def _on_search_game(main_window):
    """自动搜索本地游戏路径"""
    search_paths = [
        os.environ.get('ProgramFiles(x86)', ''),
        os.environ.get('ProgramFiles', ''),
        os.environ.get('ProgramW6432', ''),
        'C:\\Program Files (x86)',
        'C:\\Program Files',
        'D:\\',
        'E:\\',
    ]
    # 添加常见游戏目录
    for drive in ['C', 'D', 'E', 'F']:
        search_paths.append(f'{drive}:\\腾讯游戏')
        search_paths.append(f'{drive}:\\游戏')
        search_paths.append(f'{drive}:\\Games')

    found = ''
    for base in search_paths:
        if not base or not os.path.isdir(base):
            continue
        for root, dirs, files in os.walk(base):
            if _GAME_EXE in files:
                found = root
                break
            # 只搜索前 3 层
            if root.count(os.sep) - base.count(os.sep) >= 3:
                del dirs[:]
        if found:
            break

    if found:
        main_window.GamePathEdit.setText(found)
        config.set_game_path(found)
        _update_launch_btn(main_window, found)
        print(f"找到游戏路径: {found}")
    else:
        print("未找到游戏路径，请手动选择")


def _on_browse_path(main_window):
    """手动选择游戏路径"""
    # 获取真正的 QWidget 父窗口
    parent = main_window.BrowsePath if hasattr(main_window, 'BrowsePath') else None
    widget = QApplication.activeWindow()
    folder = QFileDialog.getExistingDirectory(widget, '选择游戏目录')
    if folder:
        main_window.GamePathEdit.setText(folder)
        config.set_game_path(folder)
        _update_launch_btn(main_window, folder)
        print(f"设置游戏路径: {folder}")


def _on_launch_game(main_window):
    """启动游戏"""
    game_path = main_window.GamePathEdit.text()
    if not _is_valid_game_path(game_path):
        print("游戏路径无效")
        return
    exe = os.path.join(game_path, _GAME_EXE)
    try:
        subprocess.Popen([exe], cwd=game_path)
        print(f"启动游戏: {exe}")
    except Exception as e:
        print(f"启动游戏失败: {e}")


def on_stuck_key_toggled(state):
    global current_hwnd, window_states
    if current_hwnd and current_hwnd in window_states:
        window_states[current_hwnd].stuck_key_enabled = (state == 2)


def on_ctrl_backtick_pressed():
    global current_hwnd, window_states, window
    print(f"快捷键被触发，当前窗口: {current_hwnd}")
    if current_hwnd and current_hwnd in window_states:
        window_states[current_hwnd].stuck_key_enabled = not window_states[current_hwnd].stuck_key_enabled
        window.StuckKeyStatus.setChecked(window_states[current_hwnd].stuck_key_enabled)
        print(f"卡键状态已切换为: {window_states[current_hwnd].stuck_key_enabled}")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 隐藏最大化按钮，保留最小化和关闭
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        # 注册全局快捷键 CTRL+`：使用 RegisterHotKey，下发到本窗口消息循环，
        # 由 nativeEvent 统一拦截 WM_HOTKEY。无需 keyboard 库，避免 WH_KEYBOARD_LL 系统级钩子
        self._hwnd = 0
        try:
            self._hwnd = int(self.winId())
            if not win32gui.RegisterHotKey(self._hwnd, HOTKEY_ID,
                                            win32con.MOD_CONTROL, VK_BACKTICK):
                print("RegisterHotKey 返回 False")
        except Exception as e:
            print(f"注册全局热键 CTRL+` 失败: {e}")

    def nativeEvent(self, eventType, message):
        """拦截 WM_HOTKEY，转发给 on_ctrl_backtick_pressed。

        PySide6 中 eventType 是 QByteArray，message 是 sip.voidptr / 内存地址。
        """
        # PySide6 / PyQt 在 Windows 上 eventType 均为 b'windows_generic_MSG'
        try:
            is_win_msg = (eventType == b'windows_generic_MSG'
                          or bytes(eventType) == b'windows_generic_MSG')
        except Exception:
            is_win_msg = False
        if is_win_msg and self._hwnd:
            try:
                msg = wintypes.MSG.from_address(int(message))
            except Exception:
                return False
            if msg.message == win32con.WM_HOTKEY and msg.wParam == HOTKEY_ID:
                on_ctrl_backtick_pressed()
                return True
        return super().nativeEvent(eventType, message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle("windowsvista")
    mainWindow = MainWindow()
    window = mainWindow.ui
    # 在 show 之前隐藏非"开始"选项卡，避免闪烁
    _update_tab_visibility(False)
    mainWindow.show()
    init(window)
    sys.exit(app.exec())
