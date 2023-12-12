# Fungsi rekursif
def rekursif(angka):
    # kondisi: berhenti saat angka <= -5
    if angka > -5:
        print(angka)
        angka = angka - 1
        # Memanggil dirinya sendiri (rekursif)
        rekursif(angka)
    else:
        print(angka)

# Input dari pengguna
masukan = int(input("Masukkan angka: "))
# Memanggil fungsi rekursif dengan input pengguna
rekursif(masukan)
