import wx
import data
import interface
import bayar


class Dialog(interface.MyDialog2):
    def __init__(self, parent):
        interface.MyDialog2.__init__(self, parent)
        self.parent = parent 

    def OnKlikPesan(self, event):
        print("Pesan")
        self.parent.insertDataPembelian( self.txtEmail.GetValue(), self.txtNama.GetValue(), self.txtAlamat.GetValue(), 
        self.comboWisata.GetStringSelection(), self.txtJmlTiket.GetValue(), self.txtTgl.GetValue())
        self.Destroy()
        wx.MessageDialog(None, 'Pembelian Berhasil!', 'Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

class Gui(interface.MyFrame1):
    def __init__(self, parent):
        interface.MyFrame1.__init__(self, parent)
        self.initData()

    def initData(self):
        self.beli = data.Pembelian()
        self.tkt = data.Tiket()
        daftarTiket = self.tkt.getDaftarTiket()
        baris = 0
        self.lastIdPerson = []
       
        for tkt_row in daftarTiket:
            self.tabeltiket.AppendRows(1)
            print(baris,'. ', tkt_row)
            nama_tiket,harga_tiket,lokasi,stok = tkt_row
            self.tabeltiket.SetCellValue(baris, 0, nama_tiket )
            self.tabeltiket.SetCellValue(baris, 1, harga_tiket )
            self.tabeltiket.SetCellValue(baris, 2, lokasi )
            self.tabeltiket.SetCellValue(baris, 3, stok)
            self.lastIdPerson.append(id)	
            baris += 1

    def OnPesan(self, event):
        dialog = Dialog(self)
        dialog.ShowModal()
        
    def insertDataPembelian(self, email, nama_lengkap, alamat, tempat_wisata, jumlah_tiket, tanggal_kunjungan):
        self.beli.setDataPembelian(email, nama_lengkap, alamat, tempat_wisata, jumlah_tiket, tanggal_kunjungan)
        self.initData()

    def OnUpload(self, event):
        byr = bayar.PhotoCtrl(self)
        byr.ShowModal()


# app = wx.App()
# frame = Gui(parent=None)
# frame.Show()
# app.MainLoop() 
