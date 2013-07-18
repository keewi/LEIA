#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------

import wx
from renew import *
import leia


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(250, 280))
        self.Centre()

        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu 
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this program")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()
        

        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # and a few controls
        text = wx.StaticText(panel, -1, "MAIN MENU")
        text.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        text.SetSize(text.GetBestSize())
        opt1 = wx.Button(panel,-1,"Single Word Analysis")
        opt2 = wx.Button(panel,-1,"IO Text Analysis")
        opt3 = wx.Button(panel,-1,"Datafile Analysis")
        sync= wx.Button(panel,-1,"Sync Database")
        about = wx.Button(panel,-1,"About")
        opt4 = wx.Button(panel,-1,"Quit")

        # bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.OnTimeToClose, opt4)
        self.Bind(wx.EVT_BUTTON, self.OnTimeForThree, opt3)
        self.Bind(wx.EVT_BUTTON, self.OnTimeForTwo, opt2)
        self.Bind(wx.EVT_BUTTON, self.OnTimeForOne, opt1)
        self.Bind(wx.EVT_BUTTON, self.OnTimeSync, sync)
        self.Bind(wx.EVT_BUTTON, self.OnTimeAbout, about)

        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.CENTER|wx.ALL, 15)
        sizer.Add(opt1, 0, wx.ALIGN_CENTER, 15)
        sizer.Add(opt2, 0, wx.ALIGN_CENTER, 15)
        sizer.Add(opt3, 0, wx.ALIGN_CENTER, 15)
        sizer.Add(sync,0, wx.ALIGN_CENTER, 15)
        sizer.Add(about,0, wx.ALIGN_CENTER, 15)
        sizer.Add(opt4, 0, wx.ALIGN_CENTER, 15)
        panel.SetSizer(sizer)
        panel.Layout()

        # And also use a sizer to manage the size of the panel such
        # that it fills the frame
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
    def OnTimeSync(self, evt):
        #Ttest code for R
        # code = ""
        # for x in range(1,5):
        #     for y in range(1,10):
        #         if y != 6:
        #             code = code + "v"+str(x)+str(y)+" <- t.test(d$v"+str(x)+"a"+str(y)+", d$v"+str(x)+"b"+str(y)+", na.rm=TRUE)\n"
        #     code = code + "v"+str(x)+" <- c(v"+str(x)+"1$p.value, v"+str(x)+"2$p.value, v"+str(x)+"3$p.value, v"+str(x)+"4$p.value, v"+str(x)+"5$p.value, v"+str(x)+"7$p.value, v"+str(x)+"8$p.value, v"+str(x)+"9$p.value)\n"
        # print code
        run()

    def OnTimeAbout(self, evt):
        n = str(leia.getSize())
        msg = wx.MessageDialog(None, "This program is designed to analyze text for emotional words. \n\nNumber of Words in Database: "+n, "About", wx.OK)
        msg.ShowModal()
        msg.Destroy()

    def OnTimeForOne(self, evt):
        dlg = wx.TextEntryDialog(None,
            "Input word:",
            "Single Word Analysis",
            "")
        if dlg.ShowModal() == wx.ID_OK:
            word = dlg.GetValue()
            print "WORD SEARCHED: ",word
            print "SINGLE WORD ANALYSIS RESULTS:"
            leia.opt1(word)
        dlg.Destroy()

    def OnTimeForTwo(self, evt):
        dlg = wx.TextEntryDialog(None,
            "Input text:",
            "I/O Text Analysis",
            "")
        if dlg.ShowModal() == wx.ID_OK:
            text = dlg.GetValue()
            if text != "":
                print "TEXT: ",text
                leia.opt2(text)
        dlg.Destroy()

    def OnTimeForThree(self, evt):
        dlg = wx.TextEntryDialog(None, 
            "Input file name (must be .csv)",
            "Datafile Analysis",
            "file.csv")
        if dlg.ShowModal() == wx.ID_OK:
            docname = dlg.GetValue()
            resultsdlg = wx.TextEntryDialog(None, 
                "Name results file name (must be .csv)",
                "Datafile Analysis",
                "results.csv")
            if resultsdlg.ShowModal()==wx.ID_OK:
                results = resultsdlg.GetValue()
                if leia.opt3(docname, results):
                    msg = wx.MessageDialog(None,"Done! Results have been saved as "+results,"FINISH",wx.OK)
                else:
                    msg = wx.MessageDialog(None,"Could not find file.","ERROR",wx.OK|wx.ICON_ERROR)
                msg.ShowModal()
                msg.Destroy()
        dlg.Destroy()

    def OnTimeToClose(self, evt):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "LEIA")
        self.SetTopWindow(frame)

        
        # print "RESULTS:"

        frame.Show(True)
        return True
        
app = MyApp(redirect=True)
app.MainLoop()

