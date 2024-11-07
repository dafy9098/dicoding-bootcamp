#23
#MULTIPLE VARIABLE VALUE
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(apparel)

#24
#SORT
kendaraan = ['motor','mobil','pesawat','kapal','kereta']
kendaraan.sort()
print(kendaraan)

kendaraan.sort(reverse=True)
print(kendaraan)

#25
#OPERATOR
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

#26
#ERROR HANDLING
var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    
"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
"""

#27
#INTENDED MISTAKES
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
    

"""
Traceback (most recent call last):
  File "/home/glot/main.py", line 3, in <module>
    raise ValueError("Bilangan negatif tidak diperbolehkan")
ValueError: Bilangan negatif tidak diperbolehkan
"""