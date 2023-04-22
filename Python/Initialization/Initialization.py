import os
import shutil

path = os.path.dirname(os.__file__) + r'\site-packages'  # 获取python模块包路径
shutil.copy("AutoMaa.pth", path)  # 复制文件
shutil.copy(path + r'\cv2\cv2.pyd', path)
