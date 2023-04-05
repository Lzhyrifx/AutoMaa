import os
import shutil

path = os.path.dirname(os.__file__) + r'\site-packages'  # 获取python模块包路径
shutil.copy(r"D:\AutoMaa\Python\Initialization\AutoMaa.pth", path)  # 复制文件
