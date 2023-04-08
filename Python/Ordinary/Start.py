from Module import *

o = Ordinary()

if not test("MAA.exe", o.maa):
    x = Normal()
    time.sleep(5)
    os.system(o.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
    time.sleep(120)
    guilog(o.file, o.log, o.log_bak)  # 日志整理
elif test("MAA.exe", o.maa) and rougelike():
    admin()  # 提权
    kill("MAA.exe", Ordinary.maa)  # 终止MAA进程
    kill("HD-Player.exe", bluestack)  # 终止模拟器进程
    x = Normal()
    time.sleep(5)
    os.system(o.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
    time.sleep(120)
    guilog(o.file, o.log, o.log_bak)  # 日志整理
