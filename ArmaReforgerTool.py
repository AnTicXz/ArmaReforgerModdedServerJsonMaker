from tkinter import *
from tkinter import filedialog
import os
import json


def openFile():

    filepath = filedialog.askdirectory()


    f = open("Modstext.json","w")
    f.write("\"mods\": [")


    jsonfiles = []
    for dirpath, subdirs, files in os.walk(filepath):
        for x in files:
            if x.endswith("ServerData.json"):
                jsonfiles.append(os.path.join(dirpath, x))
                
        
    for x in jsonfiles:           
        with open(x,encoding='utf-8-sig') as file:
            data = json.load(file)
            f.write("\n     {")
            f.write("\n          \"modsId\":" + "\""+data["id"]+"\",")
            f.write("\n          \"name\":" + "\""+data["name"]+"\",")
            f.write("\n          \"version\":" + "\""+data["revision"]["version"]+"\"")
            f.write("\n     },")      
    f.write("\n  ]")
    
    f.close()

window = Tk()
window.geometry("200x200")
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()