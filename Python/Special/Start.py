import os
import time
import psutil

MAA = r"D:\AutoMaa\Python\Special\MAA1\MAA.exe"
Automaa = r"D:\AutoMaa\Python\Special\Automaa.vbs"
CaptureUpdate = r"D:\AutoMaa\Python\CaptureUpdate.vbs"


def test(x, y):  # 判断进程是否存活
    for prcs in psutil.process_iter():
        if prcs.name() == x:
            process = psutil.Process(prcs.pid)
            path = process.exe()
            if path == y:
                return True


nowtime = time.strftime("%H:%M:%S", time.localtime())
if "20:00:00" < nowtime < "20:45:00":  # 指定时间
    if test("MAA.exe", MAA):
        pass
    else:
        os.system(MAA)
        os.system(Automaa)
        time.sleep(60)
        os.system(CaptureUpdate)
        time.sleep(120)
        os.system(r"log.py")
