# Mendefinisikan tuple nim
nim = (23, 11, 10, 24, 41, 10, 8)

# Menampilkan indeks dari nilai pada tuple nim

# Menampilkan indeks dari value ke-2 (indeks 1)
print(f"Indeks dari value ke-2: {nim.index(11)}")

# Menampilkan indeks dari value ke-4 (indeks 3)
print(f"Indeks dari value ke-4: {nim.index(24)}")

# Menampilkan indeks dari value pertama sampai ke-enam (indeks 0 hingga 5)
print(f"\nIndeks dari value pertama sampai ke-enam: {nim.index(23)}, {nim.index(11)}, {nim.index(10)}, {nim.index(24)}, {nim.index(41)}, {nim.index(10)}")


# Daftar siswa kelas A
kelas_a = ("ayu", "budi", "dimas", "riki", "yuyun")

# Meminta input nama siswa
nama_siswa = input("\n Silahkan Masukkan Nama Siswa: ")

# Memeriksa apakah nama siswa termasuk dalam kelas A
if nama_siswa.lower() in kelas_a:
    print("Termasuk siswa kelas A")
else:
    print("\n Tidak Termasuk siswa kelas A")



# Mendefinisikan tuple bio
bio = ("Adrian Ramadany", 2311102441108)

# Mencetak format string dengan menggunakan tuple
print("\n Nama %s dengan nim %d" % bio)
