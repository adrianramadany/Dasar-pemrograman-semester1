# Dictionary bio
bio = {
    "nama": "Adrian Ramadany",
    "nim": 2311102441108
}

print("Perulangan pada Index:")
for value in bio:
    print(value)

print("\nAkses Value pada Perulangan:")
for key in bio:
    print(bio[key])

print("\nPerulangan pada Value:")
for value in bio.values():
    print(value)

print("\nPerulangan pada Item/Elemen:")
for key, value in bio.items():
    print(key, value)
