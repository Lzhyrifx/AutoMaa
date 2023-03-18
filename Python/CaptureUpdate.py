import time
import win32api
import win32con
import win32gui

hwnd1 = win32gui.FindWindow(None, r'新版本下载完成')
time.sleep(5)
hwnd2 = win32gui.FindWindow(None, r'版本已更新')
if hwnd1 != 0:
    win32gui.SetForegroundWindow(hwnd1)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
if hwnd2 != 0:
    win32gui.PostMessage(hwnd2, win32con.WM_CLOSE, 0, 0)
