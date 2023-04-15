from automaa.automaa import *

if json_read("rougelike", "relay") == "True":
    json_change("rougelike", "relay", "False")
    os.system(r"D:\AutoMaa\Python\Ordinary\Rougelike.vbs")
