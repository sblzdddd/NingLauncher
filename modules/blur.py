# this module only support Windows
from ctypes import windll
from BlurWindow.blurWindow import blur
import win32gui

def windowblur(name):
    hwnd = windll.user32.GetForegroundWindow()
    if win32gui.GetWindowText(hwnd) == name:
        blur(hwnd)