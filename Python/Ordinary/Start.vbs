set ws=WScript.CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
Set file = fso.OpenTextFile("D:\AutoMaa\Python\Initialization\interpreter.txt", 1)
file_contents = file.ReadAll()
file.Close

If InStr(file_contents, "python") > 0 Then
    path = "D:\AutoMaa\Python\Ordinary\Start.py"
ElseIf InStr(file_contents, "conda") > 0 Then
    path = "conda run -n Automaa python D:\AutoMaa\Python\Ordinary\Start.py"
Else
    path = "D:\AutoMaa\Python\Ordinary\Start.py"
End If

ws.Run path,0