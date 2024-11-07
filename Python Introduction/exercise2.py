#8
#Slicing
y = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(y[0:7:2])
print(y[2:])
print(y[:7])

#Tuple
x = (1, "Dicoding", 1+3j)
print(type(x))
print(x[1])
print(x[0:3])

#9
#Set
s = {1.2,7,2,3,13,3}
print(x)
print(x[0])
print(type(s))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

#10
#Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))
print(x['age'])

x["Job"] = "Plumber"
print(x)

x["age"] = 23
print(x)

#11
#Data Conversion
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

print(dict([['age',2],['brothers',4]]))

#12
#UPPERCASE & LOWERCASE
kata = 'diCOdIng'
print(kata.lower())
print(kata.upper())

#13
#STRIP
print("Dicoding             ".rstrip())
print("             Dicoding".lstrip())
print("             Dicoding            ".strip())
kata1 = 'CodeCodeDicodingCodeCode'
print(kata1.strip("Code"))

#14
#STARTSWITH() & ENDSWITH()
print('Dicoding Indonesia'.startswith('Dicoding'))
print('Dicoding Indonesia'.endswith('Dicoding'))

