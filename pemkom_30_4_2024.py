# -*- coding: utf-8 -*-
"""PEMKOM 30_4_2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YOq3MPleKTP3e4_Z8Dmeo3FJtgimzAtt
"""

def cetak_nama():
  n = int(input('Enter a number (integer): '))
  nama = 'Diwantara Muhammad Qowim'
  for i in range(n):
    print(nama)
cetak_nama()

#n=5

#print(5* (print_nama))

def cetak_nama(n):
  if n % 2 == 0:
    for i in range(8):
      print(f'{i+1} Lingga Bayhaqie Saputera')
  else:
    for i in range(15):
      print(f'{i+1} Lingga Bayhaqie Saputera')

aNumber = int(input("Masukkan sebuah bilangan n: "))
cetak_nama (aNumber)

def tambah_kurang(a, b):
  addition = a + b
  substraction = a - b
  return addition, substraction

output1, output2 = tambah_kurang (20, 7)
print(f'addition result: {output1}')
print(f'substraction result: {output2}')

def cetak_nama (nama, n):
  for i in range(n):
    print(nama)
  num_character = len(nama)
  num_printed = num_character * n
  return num_character, num_printed

aNumber = int(input("Masukkan sebuah bilangan n: "))
aNama = 'Gina Lolabriga'

output1, output2 = cetak_nama (aNama, aNumber)

print(f'the number of characters in the name {output1}')
print(f'the total characters printed are {output2}')