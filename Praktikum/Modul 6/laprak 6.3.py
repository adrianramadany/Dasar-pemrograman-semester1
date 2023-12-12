# Mendefinisikan list
nama = ["Adrian", "Ramadany"]
nim = [23, 11, 10, 24, 41, 10, 8]
matakuliah = ["Pemrograman", "Dasar"]

# Menampilkan list awal
print("List nama:", nama)
print("List nim:", nim)
print("List matakuliah:", matakuliah)

# Operasi Merubah element
nama[0] = "Andi"  # Mengubah elemen pertama dari "Adrian" menjadi "Andi"
nim[3] = 25  # Mengubah elemen keempat dari 24 menjadi 25
matakuliah[1] = "Algoritma"  # Mengubah elemen kedua dari "Dasar" menjadi "Algoritma"

# Menampilkan list setelah diubah
print("\nSetelah operasi merubah:")
print("List nama:", nama)
print("List nim:", nim)
print("List matakuliah:", matakuliah)

# Operasi Menghapus element
del nama[1]  # Menghapus elemen kedua dari list nama
del matakuliah[0]  # Menghapus elemen pertama dari list matakuliah

# Menampilkan list setelah menghapus elemen
print("\nSetelah operasi menghapus:")
print("List nama:", nama)
print("List matakuliah:", matakuliah)

# Mengecek element list
cari_nama = "Andi"
if cari_nama in nama:
    print(f"\n{cari_nama} ditemukan dalam list nama.")
else:
    print(f"\n{cari_nama} tidak ditemukan dalam list nama.")

# Perulangan pada list
print("\nPerulangan pada list nim:")
for n in nim:
    print(n)

print("\nPerulangan pada list matakuliah:")
for mata_kuliah in matakuliah:
    print(mata_kuliah)




# Mendefinisikan list
nama = ["Adrian", "Ramadany"]
nim = [23, 11, 10, 24, 41, 10, 8]

# Menampilkan list nama dan nim
print("\nList nama:", nama)
print("List nim:", nim)

# Menggunakan fungsi len() untuk menghitung jumlah elemen dalam list
jumlah_nama = len(nama)
jumlah_nim = len(nim)

# Menggunakan fungsi min() untuk mencari elemen dengan nilai terkecil
nilai_terkecil_nim = min(nim)

# Menggunakan fungsi max() untuk mencari elemen dengan nilai terbesar
nilai_terbesar_nim = max(nim)

# Menampilkan hasil dari fungsi-fungsi tersebut
print(f"\nJumlah elemen dalam list nama: {jumlah_nama}")
print(f"Jumlah elemen dalam list nim: {jumlah_nim}")
print(f"Nilai terkecil dalam list nim: {nilai_terkecil_nim}")
print(f"Nilai terbesar dalam list nim: {nilai_terbesar_nim}")



# Mendefinisikan list
nama = ["Adrian", "Ramadany"]
nim = [23, 11, 10, 24, 41, 10, 8]

# Menampilkan list nama dan nim
print("List nama:", nama)
print("List nim:", nim)

# Method append untuk menambahkan elemen baru ke dalam list
nama.append("Siti")
nim.append(15)

# Method clear untuk menghapus seluruh elemen dalam list
nama.clear()
nim.clear()

# Method copy() untuk menyalin elemen dari list ke variabel lain
nama_copy = nama.copy()
nim_copy = nim.copy()

# Method count untuk menghitung jumlah elemen tertentu dalam list
jumlah_10 = nim_copy.count(10)

# Method extend untuk menambahkan list lain ke bagian ujung list yang ada
nama_copy.extend(["Joko", "Linda"])
nim_copy.extend([19, 16])

# Method index untuk mencari indeks dari elemen tertentu dalam list
indeks_joko = nama_copy.index("Joko")

# Method insert untuk menyisipkan elemen baru dengan indeks tertentu
nama_copy.insert(1, "Budi")
nim_copy.insert(1, 12)

# Method pop untuk menghapus dan mengembalikan elemen terakhir dari list
elemen_terhapus = nama_copy.pop()
nim_copy.pop()

# Method remove untuk menghapus elemen tertentu dari list
nama_copy.remove("Linda")
nim_copy.remove(16)

# Method reverse untuk membalik urutan elemen dalam list
nama_copy.reverse()
nim_copy.reverse()

# Method sort untuk mengurutkan elemen dalam list
nama_copy.sort()
nim_copy.sort()

# Menampilkan list setelah operasi dengan metode
print("\nSetelah operasi dengan metode:")
print("List nama_copy:", nama_copy)
print("List nim_copy:", nim_copy)
