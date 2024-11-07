#28
#FIND A MAX VALUE IN AN ARRAY
arr = [1,34,56,78,98,0]
leftpointer = arr[0]

for i in range (1,len(arr)):
    rightpointer = arr[i]

    if rightpointer > leftpointer:
        leftpointer =rightpointer
    else:
        continue

print (leftpointer)

#29
#MATRIX
matrix = [[1,0,1],
           [0,1,0],
           [1,0,1]]

print(matrix)

matrice = [[0 for kolom in range (3)] for baris in range (3)]

print(matrice)

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[2][2])

#30
#MATRIX OPERATIONS

#1
var_mat1 = [[5, 0, 4],
          [1, -2, 3]]
def_mat = [[0 for j in range(3)] for i in range(2)]

for i in range(len(var_mat1)):
  for j in range(len(var_mat1[0])):
    def_mat[i][j] = var_mat1[i][j]*2

print(def_mat)

#2
import numpy as n

mat = n.array([[1,2],
              [3,4]])

result = mat*2
print(result)

#31
#FUNCTION
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

y = mencari_luas_persegi_panjang(7, 8)

print(y)

#32
#PARAMETER

#POSITIONAL-OR-KEKYWORD
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

#POSITIONAL-ONLY
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(3,5))

#KEYWORD-ONLY
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))

#VAR-POSITIONAL
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))

#VAR-KEYWORD
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

#33
#FUNGSI ANONIM(LAMBDA EXPRESSION)
luas = lambda sisi: sisi*sisi*sisi
print(luas(5))

#34
#IMPORT
import rumus
rumus = rumus.luasSegitiga(4, 4)
print(rumus)

