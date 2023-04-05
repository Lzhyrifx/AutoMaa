import sys

sys.path.append(r'D:\AutoMaa\Python')  # 设置临时模块路径,编译器报错可忽略
from Module import *
import os
import time

nowtime = time.strftime("%H:%M:%S", time.localtime())

s = Special()

if nowtime < "20:00:00":
    os.system(r"Schedule.vbs")  # 启动任务
elif "20:00:00" < nowtime < "20:45:00":  # 中途启动MAA
    if test("MAA.exe", s.maa_first):  # 检测MAA进程
        pass
    else:
        os.system(s.maa_first)  # 启动MAA
        os.system(r"Schedule.vbs")  # 启动任务
        time.sleep(60)
        os.system(capture_update)  # 检测更新
        time.sleep(120)
        guilog(s.file, s.log, s.log_bak)  # 整理日志
