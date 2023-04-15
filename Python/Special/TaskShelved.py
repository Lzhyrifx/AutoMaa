from automaa import *

# 任务搁置
schedule.every().day.at("19:55:00").do(start, x=r"D:\AutoMaa\Python\Special\Kill.py")
schedule.every().day.at("19:56:00").do(sys.exit)

while True:  # 循环检测
    schedule.run_pending()
    time.sleep(1)
