from automaa import *

nowtime = time.strftime("%H:%M:%S", time.localtime())

s = Special()
o = Ordinary()

if nowtime < "20:00:00":
    os.system(r"Schedule.vbs")  # 启动任务

elif "20:00:00" < nowtime < "20:45:00":  # 中途启动MAA
    rougelike_judge()
    gui_log(s.file, s.log, s.log_bak)  # 整理日志
    time.sleep(5)
    os.system(s.maa_first)  # 启动MAA
    os.system(r"Schedule.vbs")  # 启动任务
    time.sleep(60)
    os.system(capture_update)  # 检测更新

