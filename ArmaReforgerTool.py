from itertools import count
from tkinter import *
from tkinter import filedialog
import os
import json
from traceback import print_tb
from typing import Counter


def openFile():

    filepath = filedialog.askdirectory()

    f = open("Modstext.json","w")
    f.write("\"mods\": [")
    f.close()

    jsonfiles = []
    for dirpath, subdirs, files in os.walk(filepath):
        for x in files:
            if x.endswith("ServerData.json"):
                jsonfiles.append(os.path.join(dirpath, x))

    counter = 0
    r = [len(jsonfiles)]
    for item in jsonfiles:
        with open(item,encoding='utf-8-sig') as file:
            data = json.load(file)
            var = IntVar()
            Checkbutton(window, text = data["name"],variable = var,onvalue=1,offvalue=0).pack()
            r.append(var)
            counter += 1

    def CreateJson(): 
        counter = 1
        for x in jsonfiles:
            #print(counter)
            value = r[counter] 
            print(value)
            if value.get() == 1:       
                with open(x,encoding='utf-8-sig') as file:
                    data = json.load(file)
                    f = open("Modstext.json","a")
                    f.write("\n     {")
                    f.write("\n          \"modsId\":" + "\""+data["id"]+"\",")
                    f.write("\n          \"name\":" + "\""+data["name"]+"\",")
                    f.write("\n          \"version\":" + "\""+data["revision"]["version"]+"\"")
                f.write("\n     },")    
                counter += 1 
            else:
                counter += 1
                pass
        f.write("\n  ]")
        f.close()
    
    button1 = Button(text="Create",command=CreateJson)
    button1.pack()  
    
    f.close()

window = Tk()
window.geometry("300x1200")
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()