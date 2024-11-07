#PARSING LIBRARY
#ARGPARSE
#1
""" import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari panggildicoding.py") """

#2
""" import argparse
import datetime

parser = argparse.ArgumentParser(description="Handle name and date")

parser.add_argument('-n', '--name', required=True, help='Name argument')
parser.add_argument('-d', '--date', required=True, help='Data in format DD-MM-YY')

args = parser.parse_args()

try:
    parsed_date = datetime.datetime.strptime(args.date,'%d-%m-%y')

    comparison_date = datetime.datetime(1993, 1, 1)
    if parsed_date < comparison_date:
        print ("Terima kasih telah menggunakan panggildicoding.py, Bapak "+args.name)
    else:
        print (("Terima kasih telah menggunakan panggildicoding.py, "+args.name))
except ValueError:
    print('Error') """

#LIBRARY PENGOLAHAN DATA
#PANDAS
""" import pandas as pd

data = {
    'Nama': ['John', 'Jane', 'Bob', 'Alice'],
    'Usia': [25, 30, 22, 28],
    'Pekerjaan': ['Engineer', 'Teacher', 'Designer', 'Doctor']
}

df = pd.DataFrame(data)

print(df) """

#NUMPY
""" import numpy
matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print(matriks)
 """

#MATPLOTLIB
""" import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4,6,8,10]

plt.plot(x,y)

plt.title('Contoh Plot Garis')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show() """

#SEABORN
""" import seaborn as sns
import matplotlib.pyplot as plt
 
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show() """

#BEAUTIFULSOUP4 & URLIIB
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)