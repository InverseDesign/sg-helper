import win32gui, win32con, win32api
from PySide6.QtWidgets import QApplication, QGraphicsPixmapItem, QGraphicsScene
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap

import const


class Window:
    window_text = ''
    hwnd = 0x00

    def __init__(self, hwnd):
        self.window_text = win32gui.GetWindowText(hwnd)
        self.hwnd = hwnd


class Rectangle:
    width = 0
    hight = 0

    def __init__(self, w, h):
        self.width = w
        self.hight = h


class Position:
    x = 0
    y = 0

    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

def press(handle, key_str):
    """根据按键字符串前缀自动判断组合键类型。
    格式 "ALT+A"   -> alt_press(handle, 'a')
    格式 "CTRL+A"  -> ctrl_press(handle, 'a')
    格式 "SHIFT+A" -> shift_press(handle, 'a')
    格式 "A"       -> press(handle, 'a')
    """
    key_str = key_str.strip()
    parts = key_str.split('+', 1)
    if len(parts) == 2:
        modifier, key = parts[0].upper(), parts[1].lower()
        match modifier:
            case 'ALT':
                _alt_press(handle, key)
            case 'CTRL':
                _ctrl_press(handle, key)
            case 'SHIFT':
                _shift_press(handle, key)
            case _:
                _press(handle, key_str.lower())
    else:
        _press(handle, key_str.lower())


def _press(handle, key):
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, const.keyboard_map[key], 0)
    win32api.SendMessage(handle, win32con.WM_KEYUP, const.keyboard_map[key], 0)

def _alt_press(handle, key):
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, const.keyboard_map[key], 1 << 29)
    win32api.SendMessage(handle, win32con.WM_KEYUP, const.keyboard_map[key], 1 << 29)

def _ctrl_press(handle, key):
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, const.keyboard_map[key], 1 << 29 | 1 << 28)
    win32api.SendMessage(handle, win32con.WM_KEYUP, const.keyboard_map[key], 1 << 29 | 1 << 28)

def _shift_press(handle, key):
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, const.keyboard_map[key], 1 << 20)
    win32api.SendMessage(handle, win32con.WM_KEYUP, const.keyboard_map[key], 1 << 20)


def find_window(window_name):
    windows = []
    win32gui.EnumWindows(_callback, windows)
    ret = []
    for i in windows:
        if window_name in i.window_text:
            ret.append(i)
    return ret


def grab_image(hwnd, pos, rectangle):
    game_rect = win32gui.GetWindowRect(hwnd)
    return ImageGrab.grab(game_rect)


def grab_image_qt(hwnd, pos, rectangle):
    screen = QApplication.primaryScreen()
    pixmap = screen.grabWindow(hwnd)
    pic = QPixmap.copy(pixmap, rect=QRect(pos.x, pos.y, rectangle.width, rectangle.hight))
    return pic


def _callback(hwnd, ret):
    ret.append(Window(hwnd))


def int2rgb(num):
    return num >> 16 & 255, num >> 8 & 255, num & 255


def show_pix_on_graph_view(widget, pixmap):
    # 复用 scene，避免每次 setScene 触发 QGraphicsView 整块重绘导致光标闪烁
    scene = widget.scene()
    if scene is None:
        scene = QGraphicsScene()
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        widget.setScene(scene)
        widget._pixmap_item = item
    else:
        widget._pixmap_item.setPixmap(pixmap)


if __name__ == '__main__':
    ws = find_window('QQ三国')
    img = grab_image_qt(ws[0].hwnd, Position(100, 200), Rectangle(100, 200))
    img.show()
