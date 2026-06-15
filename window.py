"""
Window - 主窗口和UI初始化

处理窗口管理、事件绑定和UI交互。
游戏逻辑已拆分到 game_handler.py 模块。
"""

import sys
import os
import subprocess
from ctypes import wintypes
import win32con
import win32gui
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer, Qt

from ui import Ui_MainWindow
from capture import CaptureProcess
from game_handler import GameHandler
import config
import util


# ---- 全局快捷键常量 ----
HOTKEY_ID = 0x0001
VK_BACKTICK = 0xC0


class WindowState:
    """单个窗口的独立状态"""
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stuck_key_enabled = False
        self.enable_blood_helper = True
        self.enable_magic_helper = True
        self.blood_key = 'R'
        self.magic_key = 'T'
        self.tick_keys = ['', '', '', '', '', '', '', '']


# ---- 模块级状态 ----
_window_states: dict[int, WindowState] = {}
_current_hwnd: int | None = None
_main_window = None
_game_handler: GameHandler | None = None


def _get_window():
    """获取全局窗口引用"""
    return _main_window.ui if _main_window else None


def on_window_select(idx):
    """窗口选择变化"""
    global _current_hwnd, _window_states, _game_handler

    ui = _get_window()
    if not ui:
        return

    hwnd = ui.WindowSelecter.itemData(idx)
    _current_hwnd = hwnd
    print(f"切换到窗口: {hwnd}")

    _update_tab_visibility(hwnd is not None and hwnd != 0)

    if not hwnd:
        return

    if hwnd not in _window_states:
        _window_states[hwnd] = WindowState(hwnd)

    # 通知截图进程切换目标窗口
    capture_process = getattr(_main_window, '_capture_process', None)
    if capture_process:
        capture_process.set_hwnd(hwnd)

    # 从 UI 加载状态
    state = _window_states[hwnd]
    state.blood_key = ui.MinBloodKeySelecter.currentText()
    state.magic_key = ui.MinMagicKeySelecter.currentText()
    state.tick_keys = [
        ui.Tick1.currentText(), ui.Tick2.currentText(),
        ui.Tick3.currentText(), ui.Tick4.currentText(),
        ui.Tick5.currentText(), ui.Tick6.currentText(),
        ui.Tick7.currentText(), ui.Tick8.currentText()
    ]

    ui.StuckKeyStatus.setChecked(state.stuck_key_enabled)
    print(f"当前窗口卡键状态: {state.stuck_key_enabled}")


def _update_tab_visibility(has_window: bool):
    """控制选项卡可见性"""
    ui = _get_window()
    if not ui:
        return
    tab_widget = ui.tabWidget
    for i in range(1, tab_widget.count()):
        tab_widget.setTabVisible(i, has_window)
        tab_widget.setTabEnabled(i, has_window)


def save_current_window_state():
    """保存当前窗口状态"""
    global _current_hwnd, _window_states
    ui = _get_window()
    if not ui or not _current_hwnd or _current_hwnd not in _window_states:
        return

    state = _window_states[_current_hwnd]
    state.blood_key = ui.MinBloodKeySelecter.currentText()
    state.magic_key = ui.MinMagicKeySelecter.currentText()
    state.tick_keys = [
        ui.Tick1.currentText(), ui.Tick2.currentText(),
        ui.Tick3.currentText(), ui.Tick4.currentText(),
        ui.Tick5.currentText(), ui.Tick6.currentText(),
        ui.Tick7.currentText(), ui.Tick8.currentText()
    ]
    state.enable_blood_helper = ui.EnableBloodHelper.isChecked()
    state.enable_magic_helper = ui.EnableMagicHelper.isChecked()


def refresh_window_list():
    """刷新窗口列表"""
    global _current_hwnd
    ui = _get_window()
    if not ui:
        return

    prev_hwnd = _current_hwnd
    ui.WindowSelecter.blockSignals(True)
    ui.WindowSelecter.clear()

    ws = util.find_window('QQ三国')
    for w in ws:
        ui.WindowSelecter.addItem(w.window_text, w.hwnd)

    target_idx = 0
    if prev_hwnd is not None:
        for i in range(ui.WindowSelecter.count()):
            if ui.WindowSelecter.itemData(i) == prev_hwnd:
                target_idx = i
                break

    ui.WindowSelecter.setCurrentIndex(target_idx)
    ui.WindowSelecter.blockSignals(False)
    on_window_select(target_idx)


def _on_timer_timeout():
    """定时器回调：更新UI显示"""
    global _current_hwnd, _game_handler

    ui = _get_window()
    if not ui or not _current_hwnd or not _game_handler:
        return

    params = _game_handler.gather_params(_current_hwnd)
    if params:
        _game_handler.trigger(params)
    _game_handler.poll_results()

    try:
        pic = util.grab_image_qt(_current_hwnd, util.Position(130, 7), util.Rectangle(90, 15))
        util.show_pix_on_graph_view(ui.CurrentRolePicture, pic)

        pic = _game_handler.find_blood_pic(_current_hwnd)
        util.show_pix_on_graph_view(ui.CurrentBloodPicture, pic)

        pic = _game_handler.find_magic_pic(_current_hwnd)
        util.show_pix_on_graph_view(ui.CurrentMagicPicture, pic)
    except Exception:
        pass


def _on_stuck_key_toggled(state):
    """卡键复选框状态变化"""
    global _current_hwnd, _window_states
    if _current_hwnd and _current_hwnd in _window_states:
        _window_states[_current_hwnd].stuck_key_enabled = (state == 2)


def _on_ctrl_backtick_pressed():
    """快捷键 CTRL+` 被按下"""
    global _current_hwnd, _window_states
    ui = _get_window()
    print(f"快捷键被触发，当前窗口: {_current_hwnd}")

    if _current_hwnd and _current_hwnd in _window_states:
        _window_states[_current_hwnd].stuck_key_enabled = not _window_states[_current_hwnd].stuck_key_enabled
        if ui:
            ui.StuckKeyStatus.setChecked(_window_states[_current_hwnd].stuck_key_enabled)
        print(f"卡键状态已切换为: {_window_states[_current_hwnd].stuck_key_enabled}")


def _init_start_tab():
    """初始化开始选项卡"""
    ui = _get_window()
    if not ui:
        return

    game_path = config.get_game_path()
    ui.GamePathEdit.setText(game_path)
    _update_launch_btn(game_path)

    ui.BtnSearchGame.clicked.connect(_on_search_game)
    ui.BtnBrowsePath.clicked.connect(_on_browse_path)
    ui.BtnLaunchGame.clicked.connect(_on_launch_game)


def _update_launch_btn(game_path: str):
    """更新启动按钮状态"""
    ui = _get_window()
    if not ui:
        return
    ui.BtnLaunchGame.setEnabled(_is_valid_game_path(game_path))


_GAME_EXE = 'QQSG.exe'


def _is_valid_game_path(path: str) -> bool:
    """检查游戏路径是否有效"""
    return bool(path) and os.path.isfile(os.path.join(path, _GAME_EXE))


def _on_search_game():
    """搜索游戏路径"""
    ui = _get_window()
    if not ui:
        return

    search_paths = [
        os.environ.get('ProgramFiles(x86)', ''),
        os.environ.get('ProgramFiles', ''),
        os.environ.get('ProgramW6432', ''),
        'C:\\Program Files (x86)',
        'C:\\Program Files',
        'D:\\', 'E:\\',
    ]
    for drive in ['C', 'D', 'E', 'F']:
        search_paths.extend([f'{drive}:\\腾讯游戏', f'{drive}:\\游戏', f'{drive}:\\Games'])

    found = ''
    for base in search_paths:
        if not base or not os.path.isdir(base):
            continue
        for root, dirs, files in os.walk(base):
            if _GAME_EXE in files:
                found = root
                break
            if root.count(os.sep) - base.count(os.sep) >= 3:
                del dirs[:]
        if found:
            break

    if found:
        ui.GamePathEdit.setText(found)
        config.set_game_path(found)
        _update_launch_btn(found)
        print(f"找到游戏路径: {found}")
    else:
        print("未找到游戏路径，请手动选择")


def _on_browse_path():
    """选择游戏目录"""
    ui = _get_window()
    if not ui:
        return

    widget = QApplication.activeWindow()
    folder = QFileDialog.getExistingDirectory(widget, '选择游戏目录')
    if folder:
        ui.GamePathEdit.setText(folder)
        config.set_game_path(folder)
        _update_launch_btn(folder)
        print(f"设置游戏路径: {folder}")


def _on_launch_game():
    """启动游戏"""
    ui = _get_window()
    if not ui:
        return

    game_path = ui.GamePathEdit.text()
    if not _is_valid_game_path(game_path):
        print("游戏路径无效")
        return

    exe = os.path.join(game_path, _GAME_EXE)
    try:
        subprocess.Popen([exe], cwd=game_path)
        print(f"启动游戏: {exe}")
    except Exception as e:
        print(f"启动游戏失败: {e}")


def init(main_window):
    """初始化主窗口"""
    global _main_window, _game_handler

    _main_window = main_window
    ui = main_window.ui

    # 启动截图进程
    capture_process = CaptureProcess()
    capture_process.start()
    main_window._capture_process = capture_process

    # 初始化 GameHandler
    _game_handler = GameHandler(_window_states, ui)
    _game_handler.set_capture_process(capture_process)
    main_window._game_handler = _game_handler

    # 初始化窗口选择器
    refresh_window_list()
    ui.WindowSelecter.currentIndexChanged.connect(on_window_select)
    ui.RefreshWindowBtn.clicked.connect(refresh_window_list)

    # 连接 UI 事件
    for selector in ['MinBloodKeySelecter', 'MinMagicKeySelecter',
                     'Tick1', 'Tick2', 'Tick3', 'Tick4', 'Tick5', 'Tick6', 'Tick7', 'Tick8']:
        getattr(ui, selector).currentIndexChanged.connect(save_current_window_state)

    ui.EnableBloodHelper.stateChanged.connect(save_current_window_state)
    ui.EnableMagicHelper.stateChanged.connect(save_current_window_state)
    ui.StuckKeyStatus.stateChanged.connect(lambda s: (save_current_window_state(), _on_stuck_key_toggled(s)))

    # 启动后台工作线程
    _game_handler.start()

    # 定时器
    main_window.timer = QTimer()
    main_window.timer.start(200)
    main_window.timer.timeout.connect(_on_timer_timeout)

    # 开始选项卡
    _init_start_tab()

    # 退出处理
    def _cleanup():
        if main_window._hwnd:
            try:
                win32gui.UnregisterHotKey(main_window._hwnd, HOTKEY_ID)
            except Exception:
                pass
        if _game_handler:
            _game_handler.stop()
        if capture_process:
            capture_process.stop()

    QApplication.instance().aboutToQuit.connect(_cleanup)


class MainWindow(QMainWindow):
    """主窗口类"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        # 注册全局快捷键
        self._hwnd = 0
        try:
            self._hwnd = int(self.winId())
            if not win32gui.RegisterHotKey(self._hwnd, HOTKEY_ID,
                                           win32con.MOD_CONTROL, VK_BACKTICK):
                print("RegisterHotKey 返回 False")
        except Exception as e:
            print(f"注册全局热键 CTRL+` 失败: {e}")

    def nativeEvent(self, eventType, message):
        """处理 WM_HOTKEY 消息"""
        try:
            is_win_msg = (eventType == b'windows_generic_MSG' or
                          bytes(eventType) == b'windows_generic_MSG')
        except Exception:
            is_win_msg = False

        if is_win_msg and self._hwnd:
            try:
                msg = wintypes.MSG.from_address(int(message))
            except Exception:
                return False
            if msg.message == win32con.WM_HOTKEY and msg.wParam == HOTKEY_ID:
                _on_ctrl_backtick_pressed()
                return True
        return super().nativeEvent(eventType, message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    window = main_window.ui

    _update_tab_visibility(False)
    main_window.show()
    init(main_window)
    sys.exit(app.exec())
