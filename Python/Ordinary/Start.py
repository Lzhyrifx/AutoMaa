from Module import *

o = Ordinary()

rougelikejudge()
mode = Mode()
mode.set_normal()
time.sleep(2)
os.system(o.maa)  # 启动MAA
time.sleep(60)
os.system(capture_update)  # 检测MAA更新
time.sleep(120)
guilog(o.file, o.log, o.log_bak)  # 日志整理

