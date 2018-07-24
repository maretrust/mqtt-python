from config import Config
from Tkinter import *

class tkFrame():

    def makeFrame(self):
        r = 0
        for d in data:
            print d
            td = 't' + d
            name = Label(text=data[d])
            name.grid(sticky="W",row=r,column=0,pady=20)
            name.config(font=("Courier", 34))
            temp = Label(text="-------C", name=d)
            temp.grid(row=r,column=1,pady=20)
            temp.config(font=("Courier", 34))
            tm = Label(text="", name=td)
            tm.grid(row=r,column=2)
            #cancella la colonna
            tm.grid_forget()
            r = r + 1
           

    def UpdateLabel(self, value,name, time): 
        tname = 't' + name
        w = root.nametowidget("."+name)
        wt = root.nametowidget("."+tname)
        w.configure(text=value)
        wt.configure(text=str(time))
    
    def getLabelTime(self, name):
        tname = 't' + name
        r = root.nametowidget("."+tname)
        return r.cget("text")
    
    def getLabelTemperature(self, name):
        r = root.nametowidget("."+name)
        return r.cget("text")
    
    def errorLabel(self, name):
        r = root.nametowidget("."+name)
        r.configure(text="ERROR")
    
    def redLabel(self, name):
        r = root.nametowidget("."+name)
        r.configure(foreground="red")

    def normalLabel(self, name):
        r = root.nametowidget("."+name)
        r.configure(foreground="black")
        
       

    def __init__(self, r):
        global data,root
        root = r
        con = Config()
        data = con.getConfigDevice()
        frame = Frame(root, name="saefy")
        self.makeFrame()
       
    