from automaa import *

kill = os.path.join(source, r'Special\Kill.py')
# 计划任务搁置
schedule.every().day.at("19:55:00").do(start, x=kill)
schedule.every().day.at("19:56:00").do(sys.exit)

while True:  # 循环检测
    schedule.run_pending()
    time.sleep(1)
