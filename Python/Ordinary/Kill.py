from __future__ import print_function

import ctypes
import os
import subprocess
import sys
import psutil

MaaProcess = r"MAA\MAA.exe"  # MAA路径
Simulator = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"  # 模拟器路径
python = r"C:\Users\Lzhyrifx\AppData\Local\Programs\Python\Python39\python.exe"  # python路径


def kill(x, y):  # 进程结束函数
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % prcs.pid, shell=True)


def killpython(x):  # 进程结束函数
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % prcs.pid, shell=True)


def is_admin():  # 提取管理员权限
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    kill("MAA.exe", MaaProcess)  # MAA进程名
    kill("HD-Player.exe", Simulator)  # 模拟器进程名
    killpython("python.exe")
    os.system("taskkill /f /im cmd.exe")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)  # 提取管理员权限
