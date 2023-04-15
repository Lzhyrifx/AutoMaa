from automaa import *


if not (test("MAA.exe", Ordinary.maa) and test("MAA.exe", Special.maa_first) and test("MAA.exe", Special.maa_second)):
    set_rougelike()
    time.sleep(2)
    os.system(Ordinary.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
