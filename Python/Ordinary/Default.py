from Python.Module import *
import re

file = r"D:\AutoMaa\Python\Ordinary\MAA\config\gui.json"

if test("MAA.exe", Ordinary.maa):
    pass
else:
    with open(file, 'r', encoding='utf-8') as f1:
        read = f1.readlines()  # 读取内容
        with open(file, 'w+', encoding='utf-8') as f2:
            for text in read:
                x = re.sub(r'...MainFunction.Stage1.:.".*".', '  "MainFunction.Stage1": "",', text)  # 正则匹配
                f2.writelines(x)  # 重写
