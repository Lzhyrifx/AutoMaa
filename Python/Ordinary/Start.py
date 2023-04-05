import sys

sys.path.append(r'D:\AutoMaa\Python')  # 设置临时模块路径,编译器报错可忽略
from Module import *

o = Ordinary()

if test("MAA.exe", o.maa):
    pass
else:
    os.system(o.maa)  # 启动MAA
    time.sleep(60)
    os.system(capture_update)  # 检测MAA更新
    time.sleep(120)
    guilog(o.file, o.log, o.log_bak)  # 日志整理
