#Persistent
#SingleInstance, force
SetBatchLines, -1
FileEncoding,UTF-8
paths := {}
paths["/"] := Func("Null")
paths["404"] := Func("NotFound")
paths["/SpecialStart"] := Func("SpecialStart")
paths["/SpecialKill"] := Func("SpecialKill")
paths["/SpecialLogNow"] := Func("SpecialLogNow")
paths["/SpecialLog"] := Func("SpecialLog")
paths["/SpecialLogLast"] := Func("SpecialLogLast")
paths["/OrdinaryStart"] := Func("OrdinaryStart")
paths["/OrdinaryKill"] := Func("OrdinaryKill")
paths["/OrdinaryLogNow"] := Func("OrdinaryLogNow")
paths["/OrdinaryLog"] := Func("OrdinaryLog")
paths["/OrdinaryLogLast"] := Func("OrdinaryLogLast")
paths["/Todesk"] := Func("Todesk")
paths["/Shutdown"] := Func("Shutdown")
paths["/CancelShutdown"] := Func("CancelShutdown")

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

SpecialLogNow(ByRef req, ByRef res) {
    FileRead,SpecialLog,D:\AutoMaa\Python\Special\MAA1\debug\gui.log
    res.SetBodyText(SpecialLogNow)
    res.status := 200
}

SpecialLog(ByRef req, ByRef res) {
    FileRead,SpecialLog,D:\AutoMaa\Python\Special\gui.log
    res.SetBodyText(SpecialLog)
    res.status := 200
}

SpecialLogLast(ByRef req, ByRef res) {
    FileRead,SpecialLog,D:\AutoMaa\Python\Special\gui.bak.log
    res.SetBodyText(SpecialLogLast)
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

OrdinaryLogNow(ByRef req, ByRef res) {
    FileRead,OrdinaryLog,D:\AutoMaa\Python\Ordinary\MAA\debug\gui.log
    res.SetBodyText(OrdinaryLogNow)
    res.status := 200
}

OrdinaryLog(ByRef req, ByRef res) {
    FileRead,OrdinaryLog,D:\AutoMaa\Python\Ordinary\gui.log
    res.SetBodyText(OrdinaryLog)
    res.status := 200
}

OrdinaryLogLast(ByRef req, ByRef res) {
    FileRead,OrdinaryLog,D:\AutoMaa\Python\Ordinary\gui.bak.log
    res.SetBodyText(OrdinaryLogLast)
    res.status := 200
}

Todesk(ByRef req, ByRef res) {
    res.SetBodyText("Todesk")
    res.status := 200
    run, "C:\Program Files\ToDesk\ToDesk.exe"
}

Shutdown(ByRef req, ByRef res) {
    res.SetBodyText("Shutdown")
    res.status := 200
    run, %comspec% /c shutdown -s -t 120
}

CancelShutdown(ByRef req, ByRef res) {
    res.SetBodyText("CancelShutdown")
    res.status := 200
    run, %comspec% /c shutdown -a
}

#include, %A_ScriptDir%\AHKhttp.ahk
#include D:\AutoMaa\Web\AHKsock-master\AHKsock-master\AHKsock.ahk
