from automaa import *

kill = os.path.join(source, r'Ordinary\kill.py')

# 计划任务搁置
schedule.every().day.at("00:55:00").do(start, x=kill)
schedule.every().day.at("00:56:00").do(sys.exit)
schedule.every().day.at("08:55:00").do(start, x=kill)
schedule.every().day.at("08:56:00").do(sys.exit)
schedule.every().day.at("16:55:00").do(start, x=kill)
schedule.every().day.at("16:56:00").do(sys.exit)

while True:  # 循环检测
    schedule.run_pending()
    time.sleep(1)
