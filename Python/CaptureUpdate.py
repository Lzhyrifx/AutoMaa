import ctypes
import os
import sys
import time

import cv2
import pyautogui
import pyscreeze
import win32con
import win32gui


def is_admin():  # 提取管理员权限
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


t = 0
screenScale = 1
if is_admin():
    hwnd1 = win32gui.FindWindow(None, r'新版本下载完成')
    if hwnd1 != 0:
        win32gui.SetForegroundWindow(hwnd1)
        target = cv2.imread(r'CaptureUpdate.png', cv2.IMREAD_GRAYSCALE)
        screenshot = pyscreeze.screenshot('Screenshot.png')
        temp = cv2.imread(r'Screenshot.png', cv2.IMREAD_GRAYSCALE)
        theight, twidth = target.shape[:2]
        tempheight, tempwidth = temp.shape[:2]
        scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
        stempheight, stempwidth = scaleTemp.shape[:2]
        res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
        mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(max_val)
        if max_val >= 0.7:
            top_left = max_loc
            bottom_right = (top_left[0] + twidth, top_left[1] + theight)
            tagHalfW = int(twidth / 2)
            tagHalfH = int(theight / 2)
            tagCenterX = top_left[0] + tagHalfW
            tagCenterY = top_left[1] + tagHalfH
            pyautogui.click(tagCenterX, tagCenterY, button='left')
        os.remove('Screenshot.png')
        while t <= 60:
            t += 1
            hwnd2 = win32gui.FindWindow(None, r'版本已更新')
            if hwnd2 != 0:
                win32gui.PostMessage(hwnd2, win32con.WM_CLOSE, 0, 0)
                break
            time.sleep(1)
    os.system("taskkill /f /im cmd.exe")

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)  # 提取管理员权限
