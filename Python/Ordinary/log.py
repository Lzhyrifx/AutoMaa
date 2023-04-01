import os
import time

data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
line = '=' * 100 + '\n'
file = r"D:\AutoMaa\Python\Ordinary\MAA\debug\gui.bak.log"
log = r"D:\AutoMaa\Python\Ordinary\GuiLog.log"
logbak = r"D:\AutoMaa\Python\Ordinary\GuiLog.bak.log"
with open(file, 'r', encoding='utf-8') as f1:
    read = f1.readlines()  # 读取日志文件
    with open(log, 'a+') as f2:
        f2.write(line + ("{:=^106s}".format(data)) + '\n' + line + '\n')  # 分割线
        for i in read:
            f2.write(i)  # 遍历内容
        f2.write('\n')
    count = len(open(log, 'r').readlines())  # 读取文件行数
    os.remove(file)
if count > 1000:  # 行数超过1000行转移日志内容
    with open(log, 'r+') as f3:
        cache = f3.readlines()
        with open(logbak, 'a+') as f4:
            for i in cache:
                f4.write(i)
        f3.seek(0)  # 指定所有行
        f3.truncate()  # 清除所有行
