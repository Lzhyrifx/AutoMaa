#Persistent
#SingleInstance, force
SetBatchLines, -1
FileEncoding,UTF-8
path := A_ScriptDir
SplitPath, path, name, dir, ext, name_no_ext
source := StrReplace(dir, "Web\AHKhttp-master", "Python")

paths := {}
paths["/"] := Func("Null")
paths["404"] := Func("NotFound")
paths["/OrdinaryStart"] := Func("OrdinaryStart")
paths["/OrdinaryKill"] := Func("OrdinaryKill")
paths["/OrdinaryLogNow"] := Func("OrdinaryLogNow")
paths["/OrdinaryLog"] := Func("OrdinaryLog")
paths["/OrdinaryLogLast"] := Func("OrdinaryLogLast")
paths["/OrdinaryDefault"] := Func("OrdinaryDefault")
paths["/OrdinaryRougelike"] := Func("OrdinaryRougelike")
paths["/OrdinaryTaskShelved"] := Func("OrdinaryTaskShelved")
paths["/SpecialStart"] := Func("SpecialStart")
paths["/SpecialKill"] := Func("SpecialKill")
paths["/SpecialLogNow"] := Func("SpecialLogNow")
paths["/SpecialLog"] := Func("SpecialLog")
paths["/SpecialLogLast"] := Func("SpecialLogLast")
paths["/SpecialTaskShelved"] := Func("SpecialTaskShelved")
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

OrdinaryStart(ByRef req, ByRef res) {
    res.SetBodyText("Starting...")
    res.status := 200
    combined_path := source . "\Ordinary\Start.vbs"
    run, %combined_path%
}

OrdinaryKill(ByRef req, ByRef res) {
    res.SetBodyText("Killing...")
    res.status := 200
    combined_path := source . "\Ordinary\Kill.vbs"
    run, %combined_path%
}

OrdinaryLogNow(ByRef req, ByRef res) {
    combined_path := source . "\Ordinary\MAA\debug\gui.log"
    FileRead,OrdinaryLogNow,%combined_path%
    res.SetBodyText(OrdinaryLogNow)
    res.status := 200
}

OrdinaryLog(ByRef req, ByRef res) {
    combined_path := source . "\Ordinary\gui.log"
    FileRead,OrdinaryLog,%combined_path%
    res.SetBodyText(OrdinaryLog)
    res.status := 200
}

OrdinaryLogLast(ByRef req, ByRef res) {
    combined_path := source . "\Ordinary\gui.bak.log"
    FileRead,OrdinaryLogLast,%combined_path%
    res.SetBodyText(OrdinaryLogLast)
    res.status := 200
}

OrdinaryDefault(ByRef req, ByRef res) {
    res.SetBodyText("Default")
    res.status := 200
    combined_path := source . "\Ordinary\Default.vbs"
    run, %combined_path%
}

OrdinaryRougelike(ByRef req, ByRef res) {
    res.SetBodyText("Rougelike")
    res.status := 200
    combined_path := source . "\Ordinary\Rougelike.vbs"
    run, %combined_path%
}

OrdinaryTaskShelved(ByRef req, ByRef res) {
    res.SetBodyText("TaskShelved")
    res.status := 200
    combined_path := source . "\Ordinary\TaskShelved.vbs"
    run, %combined_path%
}

SpecialStart(ByRef req, ByRef res) {
    res.SetBodyText("Starting...")
    res.status := 200
    combined_path := source . "\Special\Start.vbs"
    run, %combined_path%
}

SpecialKill(ByRef req, ByRef res) {
    res.SetBodyText("Killing...")
    res.status := 200
    combined_path := source . "\Special\Kill.vbs"
    run, %combined_path%
}

SpecialLogNow(ByRef req, ByRef res) {
    combined_path := source . "\Special\MAA1\debug\gui.log"
    FileRead,SpecialLogNow,%combined_path%
    res.SetBodyText(SpecialLogNow)
    res.status := 200
}

SpecialLog(ByRef req, ByRef res) {
    combined_path := source . "\Special\gui.log"
    FileRead,SpecialLog,%combined_path%
    res.SetBodyText(SpecialLog)
    res.status := 200
}

SpecialLogLast(ByRef req, ByRef res) {
    combined_path := source . "\Special\gui.bak.log"
    FileRead,SpecialLogLast,%combined_path%
    res.SetBodyText(SpecialLogLast)
    res.status := 200
}

SpecialTaskShelved(ByRef req, ByRef res) {
    res.SetBodyText("TaskShelved")
    res.status := 200
    combined_path := source . "\Special\TaskShelved.vbs"
    run, %combined_path%
}

Todesk(ByRef req, ByRef res) {
    res.SetBodyText("Todesk")
    res.status := 200
    run, "D:\Program Files (x86)\ToDesk\ToDesk.exe"
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
