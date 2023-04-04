import sys

sys.path.append(r'D:\AutoMaa\Python')  # 设置临时模块路径
from Module import *
import os

admin()  # 提权
kill("MAA.exe", Ordinary.maa)  # 终止MAA进程
kill("HD-Player.exe", bluestack)  # 终止模拟器进程
killpython("python.exe")  # 终止python进程
os.system("taskkill /f /im cmd.exe")  # 关闭cmd窗口
