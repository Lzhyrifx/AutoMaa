from Module import *

if not test("MAA.exe", Ordinary.maa):
    with open(json, 'r', encoding='utf-8') as f1:
        read = f1.readlines()  # 读取内容
        with open(json, 'w', encoding='utf-8') as f2:
            for text in read:
                x = re.sub(r'...MainFunction.Stage1.:.".*".', '  "MainFunction.Stage1": "",', text)  # 正则匹配
                f2.write(x)  # 写入
