import wx
import data
import registerlog
import Home2

class dlgDaftar(registerlog.MyDialog1):
    def __init__(self, parent):
        registerlog.MyDialog1.__init__(self, parent)
    
        self.user = data.Pengguna()

    def onDaftar(self, event):
        print("Daftar")
        self.insertDataPengguna(self.txtEmail.GetValue(), self.txtUsername.GetValue(),
        self.txtDepan.GetValue(), self.txtBelakang.GetValue(), self.comboKelamin.GetStringSelection(),
        self.txtPassword.GetValue(), self.txtNo.GetValue())
        self.Destroy()
        wx.MessageDialog(None, 'Registrasi Akun Berhasil!', 'Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

    def insertDataPengguna(self, email, username, nama_depan, nama_belakang, jenis_kelamin, password, no_telepon):
        self.user.setDataPengguna(email, username, nama_depan, nama_belakang, jenis_kelamin, password, no_telepon)


class dlgLogin(registerlog.MyDialog2):
    def __init__(self, parent):
        registerlog.MyDialog2.__init__(self, parent)
        self.parent = parent
        self.user = data.Pengguna()

    def onLogin(self, event):
        username = self.txtUsername.GetValue()
        password = self.txtPassword.GetValue()
        cek = self.cek(username, password)
        try:
            if (username, password == cek):
                beranda = Home2.frHome(None)
                beranda.Show()
            else:
                wx.MessageDialog(None,'Login Gagal.','Failed', style=wx.OK | wx.ICON_ERROR).ShowModal()

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()


    def cek(self, username, password):
        self.user.getDataLogin(username, password)


    def onRegister(self, event):
        dialog = dlgDaftar(parent=None)
        dialog.ShowModal()
        

app = wx.App()
frame = dlgLogin(parent=None)
frame.Show()
app.MainLoop()

