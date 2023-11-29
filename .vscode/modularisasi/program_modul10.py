# main_program.py
import tabung_module

def main():
    # Input dari pengguna
    radius = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))

    # Menghitung volume menggunakan modul
    volume = tabung_module.hitung_volume_tabung(radius, tinggi)

    # Menampilkan output
    print(f"Volume tabung dengan jari-jari {radius} dan tinggi {tinggi} adalah {volume:.2f}")

if __name__ == "__main__":
    main()

