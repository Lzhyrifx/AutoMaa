import sys

sys.path.append(r'D:\AutoMaa\Python')  # 设置临时模块路径,编译器报错可忽略
from Module import *
import os

admin()  # 提权
kill("MAA.exe", Special.maa_first)  # 终止MAA1进程
kill("MAA.exe", Special.maa_second)  # 终止MAA2进程
kill("Nox.exe", nox)  # 终止模拟器进程
killpython("python.exe")  # 终止python进程
os.system("taskkill /f /im cmd.exe")  # 关闭cmd
