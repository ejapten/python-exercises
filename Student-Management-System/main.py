# Menambahkan nama, umur, kelas, nilai, ID
# indo, inggris, mtk, biologi, kimia, fisika, sejarah = IPA
# indo, inggris, mtk, ekonomi, geografi, sosiologi, sejarah = IPS

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

def identitas_siswa_di_sekolah():

  daftar_kelas = ["X IPA 1", "X IPA 2", "X IPA 3", "X IPS 1", "X IPS 2", "X IPS 3",
                 "XI IPA 1", "XI IPA 2", "XI IPA 3", "XI IPS 1", "XI IPS 2", "XI IPS 3",
                 "XII IPA 1", "XII IPA 2", "XII IPA 3", "XII IPS 1", "XII IPS 2", "XII IPS 3"]
  
  while True:
    nis_siswa = input("Masukan NIS : ")

    if nis_siswa.isdigit():
      break
    else:
      print("NIS siswa tidak boleh mengandung angka dan simbol")
  
  while True:
    kelas_siswa = input("Masukan Kelas : ").strip().lower()
    
    for kelas in daftar_kelas:
      if kelas_siswa == kelas.lower():
        print("Kelas Berhasil ditemukan")
        return True
    else:
      print("Kelas tidak berhasil ditemukan")
    

identitas_siswa_di_sekolah()

