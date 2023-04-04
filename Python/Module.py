import ctypes
import os
import subprocess
import sys
import time

import psutil

nox = r"D:\Program Files\Nox\bin\Nox.exe"  # 夜神模拟器路径
bluestack = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"  # 蓝叠模拟器路径
python = r"C:\Users\Lzhyrifx\AppData\Local\Programs\Python\Python39\python.exe"  # python路径
capture_update = r"D:\AutoMaa\Python\CaptureUpdate.py"  # 检测更新程序
data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取时间
line = '=' * 100 + '\n'  # 分割线


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


def test(x, y):  # 判断进程是否存活
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                return True


def guilog(file, log, log_bak):  # 整理日志
    try:
        with open(file, 'r', encoding='utf-8') as f1:
            read = f1.readlines()  # 读取日志文件
            with open(log, 'a+') as f2:
                f2.write(line + ("{:=^106s}".format(data)) + '\n' + line + '\n')  # 分割线
                for i in read:
                    f2.write(i)  # 遍历内容
                f2.write('\n')
            count = len(open(log, 'r').readlines())  # 读取文件行数
            os.remove(file)
        if count > 1000:  # 行数超过1000行转移日志内容
            with open(log, 'r+') as f3:
                cache = f3.readlines()
                with open(log_bak, 'a+') as f4:
                    for i in cache:
                        f4.write(i)
                f3.seek(0)  # 指定所有行
                f3.truncate()  # 清除所有行
    except FileNotFoundError:
        pass


def admin():  # 获取管理员权限
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def start(x):
    os.system(x)


class Ordinary:
    maa = r"D:\AutoMaa\Python\Ordinary\MAA\MAA.exe"  # MAA路径
    file = r"D:\AutoMaa\Python\Ordinary\MAA\debug\gui.bak.log"
    log = r"D:\AutoMaa\Python\Ordinary\gui.log"
    log_bak = r"D:\AutoMaa\Python\Ordinary\gui.bak.log"


class Special:
    maa_first = r"D:\AutoMaa\Python\Special\MAA1\MAA.exe"  # MAA1路径
    maa_second = r"D:\AutoMaa\Python\Special\MAA2\MAA.exe"  # MAA2路径
    file = r"D:\AutoMaa\Python\Special\MAA1\debug\gui.bak.log"
    log = r"D:\AutoMaa\Python\Special\gui.log"
    log_bak = r"D:\AutoMaa\Python\Special\gui.bak.log"
