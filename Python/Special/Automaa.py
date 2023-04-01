import os
import shutil
import subprocess
import sys
import time
import psutil
import schedule

MaaOne = r"D:\AutoMaa\Python\Special\MAA1\MAA.exe"  # MAA1路径
MaaTwo = r"D:\AutoMaa\Python\Special\MAA2\MAA.exe"  # MAA2路径
Nox = r"D:\Program Files\Nox\bin\Nox.exe"  # 模拟器路径
CaptureUpdate = r"D:\AutoMaa\Python\CaptureUpdate.vbs"


def rename(x, y):  # 重命名文件
    old = x  # 旧文件名
    new = y  # 新文件名
    try:
        shutil.copy(old, new)  # 复制文件并重命名
        os.remove(old)  # 删除原文件
    except FileNotFoundError:  # 捕获FileNotFoundError异常
        pass


def kill(x, y):  # 进程结束函数
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % prcs.pid, shell=True)


def start(x):
    os.system(x)


# 定时任务
schedule.every().day.at("20:00:00").do(rename, x=r"MAA1\debug\gui.bak.log", y=r"MAA1\debug\gui.log")
schedule.every().day.at("20:00:00").do(start, x=MaaOne)
schedule.every().day.at("20:01:00").do(start, x=CaptureUpdate)
schedule.every().day.at("20:50:00").do(kill, x="MAA.exe", y=MaaOne)
schedule.every().day.at("20:50:00").do(kill, x="Nox.exe", y=Nox)  # 模拟器进程名
schedule.every().day.at("20:50:00").do(start, x=MaaTwo)
schedule.every().day.at("21:00:00").do(kill, x="MAA.exe", y=MaaTwo)
schedule.every().day.at("21:00:00").do(kill, x="Nox.exe", y=Nox)  # 模拟器进程名
schedule.every().day.at("21:00:00").do(sys.exit)

while True:  # 循环检测
    schedule.run_pending()
    time.sleep(1)
