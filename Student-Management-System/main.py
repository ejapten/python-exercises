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

def input_nilai_mata_pelajaran(mata_pelajaran):
  while True:
    try:
      input_nilai = int(input(f"Masukan Nilai {mata_pelajaran}"))
      return input_nilai
    except ValueError:
      print("Nilai yang anda masukan Tidak Valid, masukan angka")

def nilai_mata_pelajaran_ipa():
  nilai_bahasa_indonesia = input_nilai_mata_pelajaran("Bahasa Indonesia = ")
  nilai_bahasa_inggris = input_nilai_mata_pelajaran("Bahasa Inggris = ")
  nilai_matematika = input_nilai_mata_pelajaran("Matematika = ")
  nilai_sejarah = input_nilai_mata_pelajaran("Sejarah = ")
  nilai_biologi = input_nilai_mata_pelajaran("Biologi = ")
  nilai_kimia = input_nilai_mata_pelajaran("Kimia = ")
  nilai_fisika =  input_nilai_mata_pelajaran("Fisika = ")

def nilai_mata_pelajaran_ips():
  nilai_bahasa_indonesia = input_nilai_mata_pelajaran("Bahasa Indonesia = ")
  nilai_bahasa_inggris = input_nilai_mata_pelajaran("Bahasa Inggris = ")
  nilai_matematika = input_nilai_mata_pelajaran("Matematika = ")
  nilai_sejarah = input_nilai_mata_pelajaran("Sejarah = ")
  nilai_ekonomi = input_nilai_mata_pelajaran("Ekonomi = ")
  nilai_geografi = input_nilai_mata_pelajaran("Geografi = ")
  nilai_sosiologi =  input_nilai_mata_pelajaran("Sosiologi = ")


print("\nPilihan Jurusan")
print("1. IPA")
print("2. IPS")

pilihan_jurusan = input("Masukan Jurusan = ")
if pilihan_jurusan == "1":
  nilai_mata_pelajaran_ipa()
elif pilihan_jurusan == "2":
  nilai_mata_pelajaran_ips()
else:
  print("Masukan tepat")

