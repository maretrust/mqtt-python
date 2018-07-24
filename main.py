from mqtt import Mqtt
from frame import Frame
from tkFrame import tkFrame
from config import Config
import thread
import time
import Queue
import wx
import json
from datetime import datetime
from update import Update
from Tkinter import *

global queue
queue = Queue.Queue()


def mqttConnect():
    m = Mqtt(queue)
    m.connect()


def display():
    while True:
        time.sleep(3)
        try:
            data = queue.get(False)
            temp = str(data['Temperature']) + ' C'
            deviceId = str(data['DeviceId'])
            localtime = str(data['localtime'])
            frame.UpdateLabel(temp,deviceId,localtime)
        except Queue.Empty:
            data = 'empty'
        
def verifyAlarm():
    while True:
        time.sleep(100)
        for d in data:
            verifyTimeElapsed(d)
            verifyMinMaxTemp(d) 
            
              
def verifyTimeElapsed(d):
    print "verify time ..."
    if frame.getLabelTime(str(d)):
        try:
            timeLabel = frame.getLabelTime(str(d))
            timeNow = time.ctime(time.time())
            tdelta = datetime.strptime(timeNow,"%a %b %d %H:%M:%S %Y") - datetime.strptime(str(timeLabel),"%a %b %d %H:%M:%S %Y")
            print tdelta.seconds
            if tdelta.seconds > int(con.getTimeNoData()): 
                frame.errorLabel(d)
        except ValueError:
            print 'valore sbagliato ' + frame.getLabelTime(str(d))
            

def verifyMinMaxTemp(d):
    if d in maxTemp:
        if frame.getLabelTemperature(str(d)): 
            tempLabel =frame.getLabelTemperature(str(d))
            val = 0.0
            mt = 0.0
            try:
                val = float(tempLabel[:-2])     
                mt = float(maxTemp[d])
            except ValueError:
                pass
        
            if val > mt:
                frame.redLabel(d)
            else:
                frame.normalLabel(d)

def updateConfig():
    while True:
        time.sleep(10000)
        updt = Update()
        updt.getConfigFile()
        con.reloadFile()
        
# def showApp():
#     global frame
#     app = wx.App(False)
#     frame = Frame(None)
#     frame.Show(True)
#     app.MainLoop()

def showApp():
    global frame
    root = Tk()
    frame = tkFrame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes("-fullscreen", True) 
    #root.geometry('800x600')
    root.columnconfigure(0, weight=1)
    root.mainloop()


def loadConfig():
    data = con.getConfigDevice()

if __name__ == "__main__":
    global data,con,maxTemp
    con = Config()
    data = con.getConfigDevice()
    maxTemp = con.getMaxTemp()
    try:
        thread.start_new_thread(mqttConnect, ())
        thread.start_new_thread(display, ())
        thread.start_new_thread(verifyAlarm, ())
        thread.start_new_thread(updateConfig, ())
    except:
        print "Error: unable to start thread"

    showApp()
    