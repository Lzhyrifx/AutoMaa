from automaa import *

if json_read("rougelike", "relay") == "True":
    json_change("rougelike", "relay", "False")
    os.system(os.path.join(source, r'Ordinary\Rougelike.vbs'))
