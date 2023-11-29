# Fungsi lambda untuk menggandakan angka
gandakan_angka = lambda angka: angka * 2
# Fungsi lambda untuk memangkatkan angka
pangkatkan_angka = lambda angka: angka ** 2
# Fungsi lambda untuk mengecek apakah bilangan genap (<= 5)
cek_bilangan_genap = lambda angka: angka <= 5
# Fungsi lambda tanpa parameter untuk mencetak string
hello = lambda: "Adrian Ramadany"

# Mencetak hasil dari fungsi lambda
print(hello())
print(gandakan_angka(5))
print(cek_bilangan_genap(7))

# List angka_ajaib
angka_ajaib = [1, 2, 3, 4, 5, 6, 7, 8]

# Menggunakan map untuk menggandakan dan memangkatkan setiap angka dalam list
print(list(map(lambda angka: angka * 2, angka_ajaib)))
print(list(map(lambda angka: angka ** 2, angka_ajaib)))

# Menggunakan filter untuk memfilter angka yang kurang dari -5 dalam list
print(list(filter(lambda angka: angka < -5, angka_ajaib)))
