#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------

import wx
from leia import *

class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(200, 200))
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
        text = wx.StaticText(panel, -1, "Main Menu | LEIA")
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        opt1 = wx.Button(panel,-1,"Single Word Analysis")
        opt2 = wx.Button(panel,-1,"I/O Text Analysis")
        opt3 = wx.Button(panel,-1,"Datafile Analysis")
        opt4 = wx.Button(panel,-1,"Quit")

        # bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.OnTimeToClose, opt4)
        self.Bind(wx.EVT_BUTTON, self.OnTimeForThree, opt3)
        self.Bind(wx.EVT_BUTTON, self.OnTimeForTwo, opt2)
        self.Bind(wx.EVT_BUTTON, self.OnTimeForOne, opt1)

        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.CENTER, 15)
        sizer.Add(opt1, 0, wx.ALIGN_CENTER, 15)
        sizer.Add(opt2, 0, wx.ALIGN_CENTER, 15)
        sizer.Add(opt3, 0, wx.ALIGN_CENTER, 15)
        sizer.Add(opt4, 0, wx.ALIGN_CENTER, 15)
        panel.SetSizer(sizer)
        panel.Layout()

        # And also use a sizer to manage the size of the panel such
        # that it fills the frame
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
    def OnTimeForOne(self, evt):
        dlg = wx.TextEntryDialog(None,"Input word:","Single Word Analysis","word")
        dlg.ShowModal()
        word = dlg.GetValue()
        if word != "word":
            print "WORD SEARCHED: ",word
            print "SINGLE WORD ANALYSIS RESULTS:"
            opt1(word)
        dlg.Destroy()

    def OnTimeForTwo(self, evt):
        dlg = wx.TextEntryDialog(None,"Input text:","I/O Text Analysis","text")
        dlg.ShowModal()
        text = dlg.GetValue()
        if text != "text":
            print "TEXT: ",text
            opt2(text)
        dlg.Destroy()

    def OnTimeForThree(self, evt):
        dlg = wx.TextEntryDialog(None, "Input file name (must be .csv)","Datafile Analysis","file.csv")
        dlg.ShowModal()
        docname = dlg.GetValue()
        if docname != "file.csv":
            if opt3(docname):
                msg = wx.MessageDialog(None,"Done! Results have been saved as results.csv","FINISH",wx.OK)
            else:
                msg = wx.MessageDialog(None,"Could not find file.","ERROR",wx.OK|wx.ICON_EXCLAMATION)
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

