import os
import time
import psutil

Maa = r"MAA1\MAA.exe"
Automaa = r"Automaa.vbs"


def test(x, y):  # 判断进程是否存活
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                return True


nowtime = time.strftime("%H:%M:%S", time.localtime())
if "20:00:00" < nowtime < "20:45:00":  # 指定时间
    if test("MAA.exe", Maa):
        pass
    else:
        os.system(Maa)
        os.system(Automaa)
