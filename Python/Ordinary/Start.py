import os
import shutil
import time

import psutil

Maa = r"MAA\MAA.exe"  # MAA路径
CaptureUpdate = r"D:\AutoMaa\Python\CaptureUpdate.vbs"

def rename(x, y):  # 重命名文件
    old = x  # 旧文件名
    new = y  # 新文件名
    try:
        shutil.copy(old, new)  # 复制文件并重命名
        os.remove(old)  # 删除原文件
    except FileNotFoundError:  # 捕获FileNotFoundError异常
        pass


def test(x, y):  # 判断进程是否存活
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                return True


def remove(x):
    try:
        os.remove(x)
    except FileNotFoundError:
        pass


if test("MAA.exe", Maa):
    pass
else:
    rename(r"MAA\debug\gui.bak.log", r"MAA\debug\gui.log")
    os.system(Maa)
    time.sleep(60)
    os.system(CaptureUpdate)
