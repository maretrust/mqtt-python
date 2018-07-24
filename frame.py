import wx
from config import Config

class Frame(wx.Frame):


    def makeFrame(self):
        p = wx.Panel(self)
        p.SetBackgroundColour("white")

        numero_righe = 6
        numero_colonne = 4
        sizer = wx.FlexGridSizer(numero_righe, numero_colonne, 40, 20)
        #sizer.AddGrowableCol(2)
        #sizer.AddGrowableCol(1, 2)
        #sizer.AddGrowableCol(2, 3)
        #sizer.AddGrowableCol(3, 4)
        fontTemperature = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        fontLabel = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        for d in data:
            td = 't' + d
           # textId = wx.StaticText(p, -1, d)
            textName = wx.StaticText(p, -1, data[d])
            textTemperature = wx.StaticText(p, -1, label="----- C",name=d)
            textTime = wx.StaticText(p, -1, label = "" ,name=td)
            #textId.SetFont(fontLabel)
            textName.SetFont(fontLabel)
            textTime.SetFont(fontLabel)
            textTemperature.SetFont(fontTemperature)
           # textTime.SetSize(1,1)
            #sizer.Add(textId, 0, wx.ALIGN_CENTER_VERTICAL)
            sizer.Add(textTime, 0, wx.ALIGN_CENTER_VERTICAL, 0)
            sizer.Add(textName, 0, wx.EXPAND,0)
            sizer.AddStretchSpacer(prop=7)
            sizer.Add(textTemperature, 0, wx.ALIGN_RIGHT,0)
           

            textTime.Show(False)

        boxsizer = wx.BoxSizer()
        boxsizer.Add(sizer, 0, wx.EXPAND|wx.ALL, 10) # un bordo di cornice
        p.SetSizer(boxsizer)
       # sizer.Fit(self)
        #boxsizer.Fit(self)

    def UpdateLabel(self, value,name, time): 
        tname = 't' + name
        w = wx.FindWindowByName(name)
        wt = wx.FindWindowByName(tname)
        w.SetLabel(value)
        wt.SetLabel(time)
    
    def getLabelTime(self, name):
        tname = 't' + name
        r = wx.FindWindowByName(tname)
        return r.GetLabel()
    
    def getLabelTemperature(self, name):
        r = wx.FindWindowByName(name)
        return r.GetLabel()
    
    def errorLabel(self, name):
        w = wx.FindWindowByName(name)
        w.SetLabel('ERROR')
    
    def redLabel(self, name):
        w = wx.FindWindowByName(name)
        w.SetForegroundColour((220,34,34))

    def normalLabel(self, name):
        w = wx.FindWindowByName(name)
        w.SetForegroundColour((0,0,0))
        
       

    def __init__(self, *a, **k):
        #wx.Frame.__init__(self, *a, **k)
        default = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.CAPTION | wx.CLIP_CHILDREN | wx.NO_BORDER ^ wx.SYSTEM_MENU
        wx.Frame.__init__(self,None,style=default)
        global data
        con = Config()
        data = con.getConfigDevice()
        self.makeFrame()
       
        self.SetBackgroundColour('white')
       # self.ShowFullScreen(True)
       
    