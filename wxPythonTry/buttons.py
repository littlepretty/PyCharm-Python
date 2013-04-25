import wx


app=wx.App()
win=wx.Frame(None, title='simple editor', size=(420,350))
win.Show()

loadButton=wx.Button(win,label='Open',pos=(250,5),size=(80,25))

saveButton=wx.Button(win,label='Save',pos=(315,5),size=(80,25))

filename=wx.TextCtrl(win,pos=(5,5),size=(210,25))

contents=wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE | wx.HSCROLL)


def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

loadButton.Bind(wx.EVT_BUTTON,load)
saveButton.Bind(wx.EVT_BUTTON,save)

app.MainLoop()