from automaa import *

o = Ordinary()

rougelike_judge()
set_normal()
gui_log(o.file, o.log, o.log_bak)  # 日志整理
time.sleep(5)
os.system(o.maa)  # 启动MAA
time.sleep(60)
os.system(capture_update)  # 检测MAA更新

