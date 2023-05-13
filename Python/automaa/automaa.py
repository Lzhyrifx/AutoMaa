import configparser
import ctypes
import json
import os
import re
import subprocess
import sys
import time
import psutil
import schedule

paths = configparser.ConfigParser()
paths.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paths.ini'))  # 读取paths.ini
source = os.path.dirname(os.getcwd())  # 源文件夹
nox = paths.get('paths', 'nox')  # 夜神模拟器路径
bluestack = paths.get('paths', 'bluestack')  # 蓝叠模拟器路径
python = paths.get('paths', 'python')  # python路径
interpreter = os.path.join(source, r'Initialization\interpreter.json')  # 配置文件路径
capture_update = os.path.join(source, 'CaptureUpdate.py')  # 检测更新程序
gui_json = os.path.join(source, r'Ordinary\MAA\config\gui.json')
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
# Normal模式配置
normal_config = [
    True,
    True,
    True,
    True,
    True,
    False
]
# Rougelike模式配置
rougelike_config = [
    False,
    False,
    False,
    False,
    False,
    True
]


def kill(x, y):  # 进程结束函数
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % prcs.pid, shell=True)


def kill_python(x):  # Python进程结束函数
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
        return False


def gui_log(file, log, log_bak):  # 整理日志
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f1:
            read = f1.readlines()  # 读取日志文件
            with open(log, 'a+', encoding='utf-8', errors='ignore') as f2:
                f2.write(line + ("{:=^106s}".format(data)) + '\n' + line + '\n')  # 分割线
                for i in read:
                    f2.write(i)  # 遍历内容
                f2.write('\n')
            count = len(open(log, 'r', encoding='utf-8', errors='ignore').readlines())  # 读取文件行数
            open(file, 'w').close()
        if count > 1000:  # 行数超过1000行转移日志内容
            with open(log, 'r', encoding='utf-8', errors='ignore') as f3:
                cache = f3.readlines()
                with open(log_bak, 'a+', encoding='utf-8', errors='ignore') as f4:
                    for i in cache:
                        f4.write(i)
            open(log, 'w').close()
    except PermissionError:
        admin()


def json_change(nest, key, value):  # 更改配置文件键值
    with open(interpreter, "r") as f:
        config = json.load(f)
    config[nest][key] = value
    with open(interpreter, "w") as f:
        json.dump(config, f, indent=4)


def json_read(nest, key):  # 读取配置文件键值
    with open(interpreter, "r") as f:
        config = json.load(f)
    return config.get(nest).get(key)


def rougelike_judge():  # 判断Rougelike模式
    if test("MAA.exe", Ordinary.maa) and json_read("rougelike", "mode") == "Rougelike":
        admin()  # 提权
        kill("MAA.exe", Ordinary.maa)  # 终止MAA进程
        kill("HD-Player.exe", bluestack)  # 终止模拟器进程
        json_change("rougelike", "relay", "True")


def set_normal():  # 设置Normal模式
    if not test("MAA.exe", Ordinary.maa):  # 检测MAA进程
        with open(gui_json, 'r', encoding='utf-8') as f1:
            read = f1.readlines()  # 读取gui.json文件内容
            with open(gui_json, 'w', encoding='utf-8') as f2:
                for text in read:  # 读取gui.json每一行内容
                    match = False  # 匹配标志
                    for unicode, boolean in zip(unicodelist, normal_config):
                        x = r'"TaskQueue.{}.IsChecked"'.format(unicode)  # 关键字
                        if re.search(x + r': ".*",', text):  # 正则匹配
                            replace = re.sub(x + r': ".*",', x + ': "{}",'.format(boolean), text)  # re替换字符串
                            f2.write(replace)  # 写入
                            match = True  # 匹配成功
                            break
                    if not match:  # 匹配失败
                        f2.write(text)  # 写入
        json_change("rougelike", "mode", "Normal")


def set_rougelike():  # 设置Rougelike模式
    if not test("MAA.exe", Ordinary.maa):  # 检测MAA进程
        with open(gui_json, 'r', encoding='utf-8') as f1:
            read = f1.readlines()  # 读取gui.json文件内容
            with open(gui_json, 'w', encoding='utf-8') as f2:
                for text in read:  # 读取gui.json每一行内容
                    match = False  # 匹配标志
                    for unicode, boolean in zip(unicodelist, rougelike_config):
                        x = r'"TaskQueue.{}.IsChecked"'.format(unicode)  # 关键字
                        if re.search(x + r': ".*",', text):  # 正则匹配
                            replace = re.sub(x + r': ".*",', x + ': "{}",'.format(boolean), text)  # re替换字符串
                            f2.write(replace)  # 写入
                            match = True  # 匹配成功
                            break
                    if not match:  # 匹配失败
                        f2.write(text)  # 写入
        json_change("rougelike", "mode", "Rougelike")


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
    maa = os.path.join(source, r'Ordinary\MAA\MAA.exe')  # MAA路径
    # 日志文件
    file = os.path.join(source, r'Ordinary\MAA\debug\gui.log')
    log = os.path.join(source, r'Ordinary\gui.log')
    log_bak = os.path.join(source, r'Ordinary\gui.bak.log')


class Special:
    maa_first = os.path.join(source, r'Special\MAA1\MAA.exe')  # MAA1路径
    maa_second = os.path.join(source, r'Special\MAA2\MAA.exe')  # MAA2路径
    # 日志文件
    file = os.path.join(source, r'Special\MAA1\debug\gui.log')
    log = os.path.join(source, r'Special\gui.log')
    log_bak = os.path.join(source, r'Special\gui.bak.log')
