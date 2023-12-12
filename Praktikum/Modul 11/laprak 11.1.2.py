class pekerja: #kelas
    pkTotal = 0
    
    def __init__(self, nama, gaji): #constructor
        self.nama = nama 
        self.gaji = gaji
        pekerja.pkTotal += 1

    def displayTotal (self): #method
        print("Total pekerja %d" %pekerja.pkTotal)

    def displaypekerja (self): #method
        print("Nama : ", self.nama, " Gaji : ", self.gaji)

#membuat objek dari kelas pekerjaan
tukang1 = pekerja ("tono", "2.000.000")
tukang2 = pekerja ("toni", "3.000.000")

#memanggil method pada objek 
tukang1.displayTotal()
tukang1.displaypekerja()
tukang2.displaypekerja()