for nama in "Adrian Ramadany":
    print(" nama",nama)
for angka in range(10, 0, -1):
    print(angka)

bilangan = 1  

while bilangan <= 19:  # Selama bilangan kurang dari atau sama dengan 19
    print(bilangan)  # Cetak bilangan
    bilangan += 2  # Tambahkan 2 untuk mendapatkan bilangan ganjil berikutnya

i = 1  # Inisialisasi variabel i dengan nilai 1

while i < 100:  # Selama i kurang dari 100
    if i % 3 == 0 and i % 7 == 0:  # Jika i habis dibagi 3 dan 7
        break  # Berhenti dari perulangan
    if i % 3 == 0:  # Jika i habis dibagi 3
        print(i)  # Cetak nilai i
    i += 1  # Tambahkan 1 ke i

print("/n Output terakhir adalah", i)  # Cetak output terakhir

