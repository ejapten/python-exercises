# Menambahkan nama, umur, kelas, nilai, ID

import re

data_siswa = {}

def identitas_pribadi_siswa():
  while True:
    nama_siswa = input("Masukan Nama Siswa : ")

    if re.fullmatch(r"[A-Za-z ]+", nama_siswa):
      break
    else:
      print("Nama Tidak Valid. Tidak boleh menggunakan angka dan simbol")

  while True:
    try:
      umur_siswa = int(input("Masukan Umur Siswa : "))
    except ValueError:
      print("Masukan dalam bentuk angka")
      break

    if umur_siswa > 6:
      break
    else:
        print("Masukan umur yang benar")
    

identitas_pribadi_siswa()

