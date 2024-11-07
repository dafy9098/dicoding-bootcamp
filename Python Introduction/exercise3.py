#15
#JOIN() & SPLIT()
print('123'.join(['Dicoding','Indonesia']))

print('Dicoding Indonesia'.split())

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

#16
#REPLACE()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Python"))

#17
#PENGECEKAN STRING
kata = 'SECTION'
print(kata.isupper())
print(kata.islower())

kata1 = '1234'
print(kata1.isalpha())

kata2 = 'dicoding123'
print(kata2.isalnum())

print('start123'.isdecimal())

print('         '.isspace())

print('Bad Blood'.istitle())

#18 
#ZFILL
teks = '15'
tambah_number = teks.zfill(4)
print(tambah_number)

#RJUST
print('oooo'.rjust(7,'o'))

#LJUST
print("U sure".ljust(8,'!'))

#CENTER
print('Hasta la Vista'.center(16,"-"))

#STRING LITERALS
""" \' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash """

st1 = "Jum'at"

#19
#LENGTH

exList = [1,2,2,3,3,3,7,7,9]
print(exList)
print(len(exList))

exSet = set([1,2,2,3,3,3,7,7,9])
print(exSet)
print(len(exSet))

contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list))

#20
#MIN AND MAX
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

#21
#COUNT
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

#22
#IN AND NOT IN
kalimat = 'Playing Horizon Zero Dawn on the Weekend feels so fulfilling'
print('Forbidden' in kalimat)
print('fulfilling' in kalimat)
print('feels' in kalimat)