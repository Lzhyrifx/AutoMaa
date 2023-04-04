from Python.Module import *
import os
import time

o = Ordinary()

if test("MAA.exe", o.maa):
    pass
else:
    os.system(o.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
    time.sleep(120)
    guilog(o.file, o.log, o.log_bak)  # 日志整理
