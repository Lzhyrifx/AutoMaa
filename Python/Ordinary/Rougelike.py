from Module import *

mode = Mode()

if not test("MAA.exe", Ordinary.maa) and not test("MAA.exe", Special.maa):
    mode.set_rougelike()
    time.sleep(5)
    os.system(Ordinary.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
