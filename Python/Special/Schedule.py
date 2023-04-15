from automaa import *
import schedule

s = Special()

# 定时任务
schedule.every().day.at("19:59:55").do(rougelike_judge)
schedule.every().day.at("20:00:00").do(start, x=s.maa_first)  # 启动MAA1
schedule.every().day.at("20:01:00").do(start, x=capture_update)  # 检测MAA1更新
schedule.every().day.at("20:03:00").do(gui_log, x=s.file, y=s.log, z=s.log_bak)  # 整理日志
schedule.every().day.at("20:50:00").do(kill, x="MAA.exe", y=s.maa_first)  # 终止MAA1进程
schedule.every().day.at("20:50:00").do(kill, x="Nox.exe", y=nox)  # 终止模拟器进程
schedule.every().day.at("20:50:00").do(start, x=s.maa_second)  # 启动MAA2
schedule.every().day.at("20:51:00").do(start, x=capture_update)  # 检测MAA2更新
schedule.every().day.at("21:00:00").do(kill, x="MAA.exe", y=s.maa_second)  # 终止MAA2进程
schedule.every().day.at("21:00:00").do(kill, x="Nox.exe", y=nox)  # 终止模拟器
schedule.every().day.at("21:00:00").do(sys.exit)

while True:  # 循环检测
    schedule.run_pending()
    time.sleep(1)
