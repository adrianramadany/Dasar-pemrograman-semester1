i = 1  # Inisialisasi variabel i dengan nilai 1

while i < 100:  # Selama i kurang dari 100
    if i % 3 == 0 and i % 7 == 0:  # Jika i habis dibagi 3 dan 7
        break  # Berhenti dari perulangan
    if i % 3 == 0:  # Jika i habis dibagi 3
        print(i)  # Cetak nilai i
    i += 1  # Tambahkan 1 ke i

print("Output terakhir adalah", i)  # Cetak output terakhir



for angka in range(1, 100):
    if angka % 3 == 1:
        continue
    print(angka)
