 #1
print('hello world!')

 #2
greet = 'Buenos dias'
print(greet)

 #3
""" penjumlahan = 2 + 1
hasilakhir = penjumlahan - 5
print(hasilakhir) """

 #4
name = input("You can call me ")
print('Hello, ' + name)

#5 
#Menampilkan string lebih dari satu baris (multi-line) menggunakan double quote (”””)
multi_line = """Halo! 
Namaku adalah Mochammad Dafy Irwansyah.
We met yesterday. """

print(multi_line)

#Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing. Perlu diingat bahwa indeks selalu dimulai dari 0.
x = 'dicoding'
print(x[2:])

#6
#Formatted String
name = "Perseus"
print(f"Hello, nama saya {name}")

#%-formatting
name = "Annabeth"
print("Nama saya %s" % (name))

#str.format()
name = "Nico di Angelo"
print("Nama saya {}".format(name))

#7
#Phyton's List
ex = [1,2.3,'Dicoding']
print(type(ex))
print(ex[0])

y = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(y[-5])
print(y[-1])
print(y[-3])
