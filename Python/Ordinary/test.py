import os
import re

source = os.path.dirname(os.getcwd())  # 源文件夹
gui = os.path.join(source, r'Ordinary\MAA\config\gui.json')  # 配置文件
Relay = os.path.join(source, r'Relay\Relay.vbs')  # 目标路径
Relay = Relay.replace('\\', '\\\\')  # 转双斜杠
path = Relay.replace('\\', '\\\\')  # 转三斜杠
with open(gui, 'r', encoding='utf-8') as f1:
    read = f1.readlines()  # 读取内容
    with open(gui, 'w', encoding='utf-8') as f2:
        for text in read:
            x = re.sub(r'...Start.EndsWithScript.:.".*".', '  "Start.EndsWithScript": "{}",'.format(path), text)  # 正则匹配
            f2.write(x)  # 写入
