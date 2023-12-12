# Mendefinisikan kelas Pekerja
class Pekerja:
    # Variabel kelas untuk menghitung total pekerja
    pkTotal = 0

    # Method konstruktor (__init__) untuk inisialisasi objek Pekerja
    def __init__(self, nama, gaji):
        # untuk menyimpan nama pekerja
        self.nama = nama
        # untuk menyimpan gaji pekerja
        self.gaji = gaji
        # Menambah total pekerja setiap kali objek Pekerja dibuat
        Pekerja.pkTotal += 1

    # Method untuk menampilkan total pekerja
    def displayTotal(self):
        print("Total pekerja: %d" % Pekerja.pkTotal)

    # Method untuk menampilkan informasi pekerja
    def displayPekerja(self):
        print("Nama: ", self.nama, " Gaji: ", self.gaji)

# Membuat objek pekerja
tukang1 = Pekerja("Tono", "2.000.000")
tukang2 = Pekerja("Toni", "3.000.000")

# Memanggil method displayTotal untuk menampilkan total pekerja
tukang1.displayTotal()

# Memanggil method displayPekerja untuk menampilkan informasi pekerja
tukang1.displayPekerja()
tukang2.displayPekerja()
