script_path = WScript.ScriptFullName
script_folder = Left(script_path, InStrRev(script_path, "\")) ' 获取脚本文件所在的文件夹路径
source_folder = Left(script_folder, InStrRev(Left(script_folder, InStrRev(script_folder, "\")-1), "\")-1) ' 获取源路径
' 导入vbsJSON.vbs
ExecuteGlobal CreateObject("Scripting.FileSystemObject").OpenTextFile(source_folder & "\Initialization\vbsJSON.vbs", 1).ReadAll()
' 创建json对象
Set json = New vbsJSON
' 创建一个 WScript.Shell 对象
set ws=WScript.CreateObject("WScript.Shell")
' 使用对应模式运行python程序
filepath = json.environmentJudge("Special\TaskShelved.py")
ws.Run filepath,0