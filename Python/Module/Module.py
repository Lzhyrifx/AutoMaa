import ctypes
import os
import re
import subprocess
import sys
import time

import psutil

nox = r"D:\Program Files\Nox\bin\Nox.exe"  # 夜神模拟器路径
bluestack = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"  # 蓝叠模拟器路径
python = r"C:\Users\Lzhyrifx\AppData\Local\Programs\Python\Python39\python.exe"  # python路径
capture_update = r"D:\AutoMaa\Python\CaptureUpdate.py"  # 检测更新程序
json = r"D:\AutoMaa\Python\Ordinary\MAA\config\gui.json"
data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取时间
line = '=' * 100 + '\n'  # 分割线
# unicode列表
unicodelist = [
    r"\\u81EA\\u52A8\\u516C\\u62DB",
    r"\\u57FA\\u5EFA\\u6362\\u73ED",
    r"\\u5237\\u7406\\u667A",
    r"\\u83B7\\u53D6\\u4FE1\\u7528\\u53CA\\u8D2D\\u7269",
    r"\\u9886\\u53D6\\u65E5\\u5E38\\u5956\\u52B1",
    r"\\u81EA\\u52A8\\u8089\\u9E3D"
]


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


def rougelike():
    with open(json, 'r', encoding='utf-8') as f1:
        read = f1.readlines()  # 读取gui.json文件内容
        for text in read:  # 读取gui.json每一行内容
            if re.search(r'\\u81EA\\u52A8\\u8089\\u9E3D.*True', text):  # 正则匹配
                return True
        return False


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

    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def start(x):
    os.system(x)


class Ordinary:
    maa = r"D:\AutoMaa\Python\Ordinary\MAA\MAA.exe"  # MAA路径
    # 日志文件
    file = r"D:\AutoMaa\Python\Ordinary\MAA\debug\gui.bak.log"
    log = r"D:\AutoMaa\Python\Ordinary\gui.log"
    log_bak = r"D:\AutoMaa\Python\Ordinary\gui.bak.log"


class Special:
    maa_first = r"D:\AutoMaa\Python\Special\MAA1\MAA.exe"  # MAA1路径
    maa_second = r"D:\AutoMaa\Python\Special\MAA2\MAA.exe"  # MAA2路径
    # 日志文件
    file = r"D:\AutoMaa\Python\Special\MAA1\debug\gui.bak.log"
    log = r"D:\AutoMaa\Python\Special\gui.log"
    log_bak = r"D:\AutoMaa\Python\Special\gui.bak.log"


# 正常模式
class Normal:
    boollist = [
        True,
        True,
        True,
        True,
        True,
        False
    ]

    def __init__(self):
        if not test("MAA.exe", Ordinary.maa):  # 检测MAA进程
            with open(json, 'r', encoding='utf-8') as f1:
                read = f1.readlines()  # 读取gui.json文件内容
                with open(json, 'w', encoding='utf-8') as f2:
                    for text in read:  # 读取gui.json每一行内容
                        match = False  # 匹配标志
                        for unicode, boolean in zip(unicodelist, Normal.boollist):
                            x = r'"TaskQueue.{}.IsChecked"'.format(unicode)
                            if re.search(x + r': ".*",', text):  # 正则匹配
                                replace = re.sub(x + r': ".*",', x + ': "{}",'.format(boolean), text)  # re替换字符串
                                f2.write(replace)  # 写入
                                match = True  # 匹配成功
                                break
                        if not match:  # 匹配失败
                            f2.write(text)  # 写入


# Rougelike模式
class Rougelike:
    boollist = [
        False,
        False,
        False,
        False,
        False,
        True
    ]

    def __init__(self):
        if not test("MAA.exe", Ordinary.maa):  # 检测MAA进程
            with open(json, 'r', encoding='utf-8') as f1:
                read = f1.readlines()  # 读取gui.json文件内容
                with open(json, 'w', encoding='utf-8') as f2:
                    for text in read:  # 读取gui.json每一行内容
                        match = False  # 匹配标志
                        for unicode, boolean in zip(unicodelist, Rougelike.boollist):
                            x = r'"TaskQueue.{}.IsChecked"'.format(unicode)
                            if re.search(x + r': ".*",', text):  # 正则匹配
                                replace = re.sub(x + r': ".*",', x + ': "{}",'.format(boolean), text)  # re替换字符串
                                f2.write(replace)  # 写入
                                match = True  # 匹配成功
                                break
                        if not match:  # 匹配失败
                            f2.write(text)  # 写入
