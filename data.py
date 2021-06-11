import db as database

class DataHandle:
    def __init__(self):
        self.con = database.connection
        self.cursor = self.con.cursor()
    def execQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_results

class Pengguna(DataHandle):
    def setDataPengguna(self, email, username, nama_depan, nama_belakang, jenis_kelamin, password, no_telepon):
        self.query = 'INSERT INTO pengguna (email, username, nama_depan, nama_belakang, jenis_kelamin, password, no_telepon) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
        self.query = self.query % (email, username, nama_depan, nama_belakang, jenis_kelamin, password, no_telepon)
        print('self.query: {} '.format(self.query))
        self.execQuery(self.query)

    def getDataPengguna(self, email):
        self.query = 'SELECT id_pengguna FROM pengguna WHERE email=\'%s\''
        self.query = self.query % str(email)
        print('self.query : ', self.query)
        id_pengguna = self.execQuery(self.query, retVal=True)
        return id_pengguna

    def getDataTiket(self, nama_tiket):
        self.query = 'SELECT id_tiket FROM tiket WHERE nama_tiket=\'%s\''
        self.query = self.query % str(nama_tiket)
        print('self.query : ', self.query)
        id_tiket = self.execQuery(self.query, retVal=True)
        return id_tiket

    def getDataLogin(self, username, password):
        self.query = 'SELECT username, password FROM pengguna WHERE username=\'%s\' AND password=\'%s\''
        self.query = self.query % (username, password)
        print('self.query: {} '.format(self.query))
        self.execQuery(self.query)

class Pembelian(Pengguna):
    def setDataPembelian(self, email, nama_lengkap, alamat, nama_tiket, jumlah_tiket, tanggal_kunjungan):
        id_pengguna = self.getDataPengguna(email)
        id_tiket = self.getDataTiket(nama_tiket)
        self.query = 'INSERT INTO pembelian (id_pengguna, id_tiket, nama_lengkap, alamat, tempat_wisata, jumlah_tiket, tanggal_kunjungan) VALUES (%s, %s,\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
        self.query = self.query % (id_pengguna[0][0], id_tiket[0][0], nama_lengkap, alamat, nama_tiket, jumlah_tiket, tanggal_kunjungan)
        print('self.query: {} '.format(self.query))
        self.execQuery(self.query)


class Tiket(DataHandle):
    def getDaftarTiket(self):
        self.query = 'SELECT nama_tiket, harga_tiket, lokasi, stok FROM tiket'
        print('self.query : ', self.query )
        daftar = self.execQuery(self.query, True)
        return daftar


if __name__ == '__main__':
    user = Pengguna()
    beli = Pembelian()
    tkt = Tiket()
    daftarTiket = tkt.getDaftarTiket()
    baris = 1
    for tkt_row in daftarTiket:
        print(baris,'. ', tkt_row)
        baris += 1