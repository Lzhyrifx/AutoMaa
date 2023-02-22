@echo OFF
title StarryFrp一键启动脚本[启动命令]模式
SET FrpcName=frpc.exe
echo ---------------------
echo  欢迎使用StarryFrp
echo ---------------------
if not exist %FrpcName% (
    echo  请将此文件放置于frpc.exe的同级目录下
    PAUSE
)
echo  启动命令可以在隧道列表页面找到
echo -------------------------------------
:start
set /p code=请输入网站提供的启动命令：
if "%code%"=="" echo 您输入了一个错误的命令&goto :start
%code%
PAUSE
