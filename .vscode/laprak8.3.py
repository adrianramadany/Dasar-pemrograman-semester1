# Dictionary data mahasiswa
mahasiswa_data = {
    "nama": "Adrian Ramadany",
    "nim": "2311102441108"
}

# daftar nama yang termasuk kelas A
kelas_a = {
    "Adrian Ramadany": True,
    "tono brewok": True,
    "sahrukan kw": True
}

# Program untuk mengecek apakah nama termasuk atau tidak termasuk kelas A

nama_mahasiswa = mahasiswa_data["nama"]

if kelas_a.get(nama_mahasiswa):
    print(f"{nama_mahasiswa} termasuk dalam kelas A.")
else:
    print(f"{nama_mahasiswa} tidak termasuk dalam kelas A.")


print("Data Mahasiswa:", mahasiswa_data)
