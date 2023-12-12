#writelines
#with open("C:\latihan vscode\.vscode\modularisasi\penanganan_berkas12.txt", "w") as buka:
 #   buka.writelines("ini data saya")

buka = open ("C:\latihan vscode\.vscode\modularisasi\penanganan_berkas12.txt", "w")
data = [f"nama saya: Adrian ramadany \n", "umur saya: 19"]
buka.writelines(data)

#Baca Isi File
buka = open("C:\latihan vscode\.vscode\modularisasi\penanganan_berkas12.txt", "r")
baca = buka.read()
print(baca)