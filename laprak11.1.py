class kendaraan: #kelas
    def __init__(self, jenis, roda): #constructor
        self.jenis = jenis 
        self.roda = roda 

    def info(self): #method
        print(f"jenis: {self.jenis}, Roda: {self.roda}")

#membuat objek dari kelas kendaraan 
mobil = kendaraan("mobil", 4)
motor = kendaraan("motor", 2)

#memanggil method pada objek 
mobil.info()
motor.info()