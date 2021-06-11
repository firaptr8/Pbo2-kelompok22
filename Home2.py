import wx
from wx.core import Font
import Home
import main

class frHome(Home.MyFrame1):
    def __init__(self,parent):
        Home.MyFrame1.__init__(self,parent)

    def m_panel1OnPaint( self, event ):
        dc = wx.PaintDC(self.m_panel1)
        dc.DrawBitmap(wx.Bitmap("liburan.jpg"),210,160,True)
        color = wx.Colour(350,0,0)
        b = wx.Brush(color)

        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        dc.SetFont(font)
        dc.DrawText("Selamat datang di JalanKuy!", 500, 5),
        dc.DrawText("Temukan banyak referensi tempat wisata serta kemudahan dalam pemesanan tiket ", 250, 50),
        dc.DrawText("Anda nyaman kamipun senang" , 500,100)

    def lihatDaftar(self, event):
        dftr = main.Gui(parent=None)
        dftr.Show()
        


if __name__ == "__main__":
    app = wx.App(False)
    frame = frHome(None)
    frame.Show(True)
    app.MainLoop()