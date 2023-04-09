from Module import *

o = Ordinary()
s = Ordinary()
mode = Mode()

if not test("MAA.exe", o.maa) and not test("MAA.exe", s.maa):
    mode.set_rougelike()
    time.sleep(5)
    os.system(o.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
