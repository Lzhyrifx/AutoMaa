from automaa.automaa import *
import cv2
import pyautogui
import pyscreeze
import win32con
import win32gui


t = 0
screenScale = 1  # 屏幕缩放系数
admin()  # 提权
hwnd1 = win32gui.FindWindow(None, r'新版本下载完成')  # 捕获更新窗口
if hwnd1 != 0:
    win32gui.SetForegroundWindow(hwnd1)  # 置顶更新窗口
    target = cv2.imread(r'captureupdate.png', cv2.IMREAD_GRAYSCALE)  # 读取按钮图片
    screenshot = pyscreeze.screenshot('screenshot.png')  # 全屏截图
    temp = cv2.imread(r'screenshot.png', cv2.IMREAD_GRAYSCALE)  # 二值化
    # 缩放屏幕截图
    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.7:
        # 计算中心点
        top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)
        tagHalfW = int(twidth / 2)
        tagHalfH = int(theight / 2)
        tagCenterX = top_left[0] + tagHalfW
        tagCenterY = top_left[1] + tagHalfH
        #  左键点击
        pyautogui.click(tagCenterX, tagCenterY, button='left')
    os.remove('screenshot.png')  # 删除全屏截图
    while t <= 60:
        # 计时器,等待60秒
        t += 1
        hwnd2 = win32gui.FindWindow(None, r'版本已更新')  # 捕获更新完成窗口
        if hwnd2 != 0:
            win32gui.PostMessage(hwnd2, win32con.WM_CLOSE, 0, 0)  # 关闭更新完成窗口
            break
        time.sleep(1)
os.system("taskkill /f /im cmd.exe")  # 关闭cmd窗口
