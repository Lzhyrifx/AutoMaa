#Persistent
#SingleInstance, force
SetBatchLines, -1
FileEncoding,UTF-8
paths := {}
paths["/"] := Func("Null")
paths["404"] := Func("NotFound")
paths["/SpecialTest"] := Func("SpecialTest")
paths["/SpecialStart"] := Func("SpecialStart")
paths["/SpecialKill"] := Func("SpecialKill")
paths["/SpecialLog"] := Func("SpecialLog")
paths["/OrdinaryTest"] := Func("OrdinaryTest")
paths["/OrdinaryStart"] := Func("OrdinaryStart")
paths["/OrdinaryKill"] := Func("OrdinaryKill")
paths["/OrdinaryLog"] := Func("OrdinaryLog")
paths["/Todesk"] := Func("Todesk")

server := new HttpServer()
server.LoadMimes(A_ScriptDir . "/mime.types")
server.SetPaths(paths)
server.Serve(1024)
return


NotFound(ByRef req, ByRef res) {
    res.SetBodyText("Page not found")
}

Null(ByRef req, ByRef res) {
    res.SetBodyText("Null")
    res.status := 200
}

SpecialTest(ByRef req, ByRef res) {
    res.SetBodyText("Success")
    res.status := 200
}

SpecialStart(ByRef req, ByRef res) {
    res.SetBodyText("Starting...")
    res.status := 200
    run, "D:\AutoMaa\Python\Special\Start.vbs"
}

SpecialKill(ByRef req, ByRef res) {
    res.SetBodyText("Killing...")
    res.status := 200
    run, "D:\AutoMaa\Python\Special\Kill.vbs"
}

SpecialLog(ByRef req, ByRef res) {
    FileRead,SpecialLog,D:\AutoMaa\Python\Special\MAA1\debug\gui.log
    res.SetBodyText(SpecialLog)
    res.status := 200
}

OrdinaryTest(ByRef req, ByRef res) {
    res.SetBodyText("Success")
    res.status := 200
}

OrdinaryStart(ByRef req, ByRef res) {
    res.SetBodyText("Starting...")
    res.status := 200
    run, "D:\AutoMaa\Python\Ordinary\Start.vbs"
}

OrdinaryKill(ByRef req, ByRef res) {
    res.SetBodyText("Killing...")
    res.status := 200
    run, "D:\AutoMaa\Python\Ordinary\Kill.vbs"
}

OrdinaryLog(ByRef req, ByRef res) {
    FileRead,OrdinaryLog,D:\AutoMaa\Python\Ordinary\MAA\debug\gui.log
    res.SetBodyText(OrdinaryLog)
    res.status := 200
}

Todesk(ByRef req, ByRef res) {
    res.SetBodyText("Todesk")
    res.status := 200
    run, "C:\Program Files\ToDesk\ToDesk.exe"
}
#include, %A_ScriptDir%\AHKhttp.ahk
#include D:\AutoMaa\Web\AHKsock-master\AHKsock-master\AHKsock.ahk
