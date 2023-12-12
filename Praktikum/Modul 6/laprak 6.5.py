# Mendefinisikan list
nama = ["Adrian", "Ramadany"]
nim = [23, 11, 10, 24, 41, 10, 8]

# Menampilkan list nama dan nim
print("List nama:", nama)
print("List nim:", nim)

# Method append()
nama.append("Andi")
nim.append(15)

# append() digunakan untuk menambahkan elemen baru pada akhir list. 
# Dalam contoh di atas, "Andi" ditambahkan ke list nama dan angka 15 ditambahkan ke list nim.

# Menampilkan list setelah menggunakan append()
print("\nSetelah menggunakan append():")
print("List nama:", nama)
print("List nim:", nim)

# Method clear()
nama.clear()
nim.clear()

# clear() digunakan untuk menghapus semua elemen dalam list. 
# Setelah menggunakan clear(), list nama dan nim menjadi kosong.

# Menampilkan list setelah menggunakan clear()
print("\nSetelah menggunakan clear():")
print("List nama:", nama)
print("List nim:", nim)

# Mengisi list kembali
nama = ["Adrian", "Ramadany"]
nim = [23, 11, 10, 24, 41, 10, 8]

# Method copy()
nama_copy = nama.copy()
nim_copy = nim.copy()

# copy() digunakan untuk membuat salinan (copy) dari list. 
# Dalam contoh di atas, kita membuat salinan dari list nama dan nim ke nama_copy dan nim_copy.

# Menampilkan list hasil copy()
print("\nHasil dari copy():")
print("List nama_copy:", nama_copy)
print("List nim_copy:", nim_copy)

# Method count()
jumlah_10 = nim.count(10)

# count() digunakan untuk menghitung berapa kali elemen tertentu muncul dalam list. 
# Dalam contoh di atas, kita menghitung berapa kali angka 10 muncul dalam list nim.

# Menampilkan hasil count()
print(f"\nJumlah elemen 10 dalam list nim: {jumlah_10}")

# Method extend()
nama.extend(["Budi", "Cahyadi"])
nim.extend([15, 30])

# extend() digunakan untuk menambahkan elemen-elemen dari list lain ke akhir list yang ada. 
# Dalam contoh di atas, kita menambahkan elemen-elemen baru dari list ke list nama dan nim.

# Menampilkan list setelah menggunakan extend()
print("\nSetelah menggunakan extend():")
print("List nama:", nama)
print("List nim:", nim)

# Method index()
index_ramadany = nama.index("Ramadany")

# index() digunakan untuk mencari indeks (posisi) dari elemen tertentu dalam list. 
# Dalam contoh di atas, kita mencari indeks dari elemen "Ramadany" dalam list nama.
# Menampilkan hasil index()
print(f"\nIndex 'Ramadany' dalam list nama: {index_ramadany}")

# Method insert()
nama.insert(1, "Andi")
nim.insert(1, 35)

# insert() digunakan untuk menyisipkan elemen baru pada indeks tertentu dalam list. 
# Dalam contoh di atas, "Andi" disisipkan pada indeks 1 dalam list nama dan 35 disisipkan pada indeks 1 dalam list nim.

# Menampilkan list setelah menggunakan insert()
print("\nSetelah menggunakan insert():")
print("List nama:", nama)
print("List nim:", nim)

# Method pop()
pop_nama = nama.pop()
pop_nim = nim.pop()

# pop() digunakan untuk menghapus dan mengembalikan elemen terakhir dari list (atau indeks tertentu jika diberikan argumen). 
# Dalam contoh di atas, kita menghapus dan mengembalikan elemen terakhir dari list nama dan nim.

# Menampilkan hasil pop()
print(f"\nElemen yang di-pop dari list nama: {pop_nama}")
print(f"Elemen yang di-pop dari list nim: {pop_nim}")

# Method remove()
nama.remove("Andi")
nim.remove(35)

# remove() digunakan untuk menghapus elemen tertentu dari list. 
# Dalam contoh di atas, kita menghapus elemen "Andi" dari list nama dan elemen 35 dari list nim.

# Menampilkan list setelah menggunakan remove()
print("\nSetelah menggunakan remove():")
print("List nama:", nama)
print("List nim:", nim)

# Method reverse()
nama.reverse()
nim.reverse()

# reverse() digunakan untuk membalik urutan elemen dalam list. 
# Dalam contoh di atas, kita membalik urutan elemen dalam list nama dan nim.

# Menampilkan list setelah menggunakan reverse()
print("\nSetelah menggunakan reverse():")
print("List nama:", nama)
print("List nim:", nim)

# Method sort()
nama.sort()
nim.sort()

# sort() digunakan untuk mengurutkan elemen dalam list. 
# Dalam contoh di atas, kita mengurutkan elemen dalam list nama dan nim secara ascending (default).

# Menampilkan list setelah menggunakan sort()
print("\nSetelah menggunakan sort():")
print("List nama:", nama)
print("List nim:", nim)
