@echo OFF
title StarryFrpһ�������ű�[��������]ģʽ
SET FrpcName=frpc.exe
echo ---------------------
echo  ��ӭʹ��StarryFrp
echo ---------------------
if not exist %FrpcName% (
    echo  �뽫���ļ�������frpc.exe��ͬ��Ŀ¼��
    PAUSE
)
echo  �����������������б�ҳ���ҵ�
echo -------------------------------------
:start
set /p code=��������վ�ṩ���������
if "%code%"=="" echo ��������һ�����������&goto :start
%code%
PAUSE
