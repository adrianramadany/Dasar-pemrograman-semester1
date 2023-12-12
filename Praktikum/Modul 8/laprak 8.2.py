# Set data
mahasiswa_set = {"Adrian", "Ramadany", 2311102441108}

# Method add: Menambahkan elemen ke dalam set
mahasiswa_set.add("Siapaya")
print("Set setelah method Add:", mahasiswa_set)

# Method clear: Mengosongkan set
mahasiswa_set.clear()
print("Set setelah method Clear:", mahasiswa_set)  # Output akan menjadi set kosong

# Method copy: Menduplikasi set
mahasiswa_set = {"Adrian", "Ramadany", 2311102441108}
mahasiswa_baru = mahasiswa_set.copy()
mahasiswa_baru.add("NimBaru")
print("Set setelah method Copy:", mahasiswa_set)
print("Copy of Set:", mahasiswa_baru)

# Method difference: Mengembalikan selisih antara dua set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference_set = set1.difference(set2)
print("Hasil Difference antara set1 dan set2:", difference_set)

# Method discard: Menghapus elemen dari set (jika ada)
mahasiswa_set = {"Adrian", "Ramadany", 2311102441108}
mahasiswa_set.discard("Ramadany")
print("Set setelah method Discard:", mahasiswa_set)

# Method intersection: Mengembalikan hasil irisan antara dua set
set3 = {"Adrian", "Ramadany", 2311102441108}
set4 = {"Ramadany", 2311102441108, "NewName"}
intersection_set = set3.intersection(set4)
print("Hasil Intersection antara set3 dan set4:", intersection_set)

# Method intersection_update: Memperbarui set dengan hasil irisan antara dua set
set3.intersection_update(set4)
print("Set setelah method Intersection_update:", set3)

# Method isdisjoint: Mengembalikan True jika dua set tidak memiliki elemen bersama
result = set1.isdisjoint(set2)
print("Hasil isdisjoint antara set1 dan set2:", result)

# Method issuperset: Mengembalikan True jika set berisi set lain atau set sama
result_superset = set1.issuperset(set2)
print("Hasil issuperset antara set1 dan set2:", result_superset)

# Method pop: Menghapus dan mengembalikan elemen acak dari set
popped_element = mahasiswa_set.pop()
print("Elemen yang di-pop dari set:", popped_element)
print("Set setelah method Pop:", mahasiswa_set)

# Method remove: Menghapus elemen tertentu dari set
mahasiswa_set = {"Adrian", "Ramadany", 2311102441108}
mahasiswa_set.remove(2311102441108)
print("Set setelah method Remove:", mahasiswa_set)

# Method symmetric_difference: Mengembalikan hasil dari symmetric difference antara dua set
symmetric_difference_set = set1.symmetric_difference(set2)
print("Hasil Symmetric Difference antara set1 dan set2:", symmetric_difference_set)

# Method symmetric_difference_update: Memperbarui set dengan hasil symmetric difference antara dua set
set1.symmetric_difference_update(set2)
print("Set setelah method Symmetric_difference_update:", set1)

# Method union: Mengembalikan hasil gabungan dari dua set
union_set = set1.union(set2)
print("Hasil Union antara set1 dan set2:", union_set)

# Method update: Memperbarui set dengan menambahkan elemen-elemen dari set lain
set1.update(set2)
print("Set setelah method Update:", set1)
