# Dictionary bio
bio = {
    "nama": "Adrian Ramadany",
    "nim": 2311102441108
}

# Method Clear
bio.clear()
print("Setelah menggunakan method clear:", bio)

# Method Copy
bio = {
    "nama": "Adrian Ramadany",
    "nim": 2311102441108
}
bio_copy = bio.copy()
print("\nSetelah menggunakan method copy:")
print("Copy dari dictionary bio:", bio_copy)

# Method Fromkeys
keys = ["nama", "nim"]
values = "Tidak Tersedia"
default_bio = dict.fromkeys(keys, values)
print("\nSetelah menggunakan method fromkeys:")
print("Dictionary default_bio:", default_bio)

# Method Get
nama_mahasiswa = bio.get("nama", "Tidak Tersedia")
print("\nSetelah menggunakan method get:")
print("Nama Mahasiswa:", nama_mahasiswa)

# Method Items
items = bio.items()
print("\nSetelah menggunakan method items:")
print("Items dalam dictionary bio:", items)

# Method Keys
keys_bio = bio.keys()
print("\nSetelah menggunakan method keys:")
print("Keys dalam dictionary bio:", keys_bio)

# Method Values
values_bio = bio.values()
print("\nSetelah menggunakan method values:")
print("Values dalam dictionary bio:", values_bio)

# Method Pop
nim_mahasiswa = bio.pop("nim", "Tidak Tersedia")
print("\nSetelah menggunakan method pop:")
print("NIM Mahasiswa yang di-pop:", nim_mahasiswa)
print("Dictionary bio setelah pop:", bio)

# Method Setdefault
angkatan_mahasiswa = bio.setdefault("angkatan", 2023)
print("\nSetelah menggunakan method setdefault:")
print("Angkatan Mahasiswa yang disetdefault:", angkatan_mahasiswa)
print("Dictionary bio setelah setdefault:", bio)

# Method Update
bio_update = {"jurusan": "Teknik Informatika"}
bio.update(bio_update)
print("\nSetelah menggunakan method update:")
print("Dictionary bio setelah update:", bio)

# Method Values (sekali lagi)
values_bio = bio.values()
print("\nSetelah menggunakan method values:")
print("Values dalam dictionary bio:", values_bio)
