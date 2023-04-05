from Module import *

o = Ordinary()

if not test("MAA.exe", o.maa):
    x = Rougelike()
    time.sleep(5)
    os.system(o.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
    time.sleep(120)
    guilog(o.file, o.log, o.log_bak)  # 日志整理
