#import modul1 as operasi 
#print("penjumlahan: ", operasi.hitung(5,2))

#import modul1
#result = modul1.hitung(5,2)
#print(result)

# sampel1.py
import modul1

def main():
    r = 5
    s = 2

    hasil_ta = modul1.tambah(r, s)
    hasil_ku = modul1.kurang(r, s)
    hasil_ka = modul1.kali(r, s)
    hasil_ba = modul1.bagi(r, s)
    hasil_pa = modul1.pangkat(r, s)

    # Menampilkan hasil
    print(f"Hasil tambah: {hasil_ta}")
    print(f"Hasil kurang: {hasil_ku}")
    print(f"Hasil kali: {hasil_ka}")
    print(f"Hasil bagi: {hasil_ba}")
    print(f"Hasil pangkat: {hasil_pa}")

if __name__ == "__main__":
    main()
