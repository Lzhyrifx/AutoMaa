' 导入vbsJSON.vbs
ExecuteGlobal CreateObject("Scripting.FileSystemObject").OpenTextFile("D:\AutoMaa\Python\Initialization\vbsJSON.vbs", 1).ReadAll()
' 创建json对象
Set json = New vbsJSON
' 创建一个 WScript.Shell 对象
set ws=WScript.CreateObject("WScript.Shell")
' 使用对应模式运行python程序
filepath = json.environmentJudge("Ordinary\TaskShelved.py")
ws.Run filepath,0