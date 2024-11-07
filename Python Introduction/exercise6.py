#1
#CLASS CONSTRUCTOR
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil1 = Mobil("Grey","Mitsubishi", 200)

print(mobil1.merek)

#2
#KONSEP DECORATOR
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

@my_decorator
def say():
    print("Hola!")

say()

#3
#CLASS CONSTRUCTOR
#fungsi khusus dalam Python yang digunakan untuk menentukan nilai atau kondisi awal dari suatu kelas.
#"__init__" sebagai fungsi khusus untuk menjadi constructor. Selanjutnya, kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.
""" class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    #OBJECT METHOD
    #Jenis pertama adalah method yang melekat terhadap objek. Ciri dari jenis metode ini adalah adanya parameter self yang merujuk pada objek saat ini yang dibuat.

    def tambah_kecepatan(self):
    self.kecepatan += 10

mobil1 =('Merah', 'DicodingCar', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan) """

#STATIC METHOD
#metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas. Jadi, ini menjadi perilaku untuk kelas tersebut.
""" class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil() """

#CLASS METHOD
#Jika object method identik dengan parameter self yang merujuk pada objek, class methodjuga memerlukan sebuah parameter yang merujuk pada kelas.
""" class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil() """

#4
#INHERITANCE
""" class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan) """

#5
#OVERRIDE
""" class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

mobil2 = Mobil("Hijau", "Antasena", 180)
mobil2.tambah_kecepatan()
print(mobil2.kecepatan) """

#6
#SUPER
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)