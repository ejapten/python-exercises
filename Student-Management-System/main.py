import re
from datetime import datetime
import numbers

data_pribadi_siswa = {}
data_siswa_disekolah = {}

# Fungsi Pesan 
def notifikasi(teks):
  print(f"{teks}\n")

def identitas_pribadi_siswa():

  """"Fungsi Untuk memasukan identitas pribadi siswa
  """

  while True:

    #NIK
    nik_siswa = input("Masukan NIK Siswa : ").strip()

    if len(nik_siswa) < 16 :
      notifikasi("--> ⚠️ NIK Tidak Boleh Kurang dari 16 angka")
      continue
    elif len(nik_siswa) > 16:
      notifikasi("--> ⚠️ NIK Tidak Boleh lebih dari 16 angka")
      continue
    elif not re.fullmatch(r"\d+", nik_siswa):
      notifikasi("--> ⚠️ NIK tidak boleh mengandung Karakter")
      continue
    else: 
      notifikasi("--> ✅ NIK  Berhasil ditambah")

    # Nama Lengkap
    nama_lengkap_siswa = input("Masukan Nama Lengkap : ")

    if re.fullmatch(r"[A-Za-z ]+", nama_lengkap_siswa):
      notifikasi("--> ✅ Nama Berhasil ditambahkan")
    else:
      print("--> ⚠️ Nama Tidak Valid. Tidak boleh menggunakan angka dan simbol")

    # Alamat Rumah
    alamat_rumah_siswa = input("Masukan alamat rumah : ")
    if alamat_rumah_siswa == ' ':
      notifikasi("--> ⚠️ Alamat Tidak Boleh kosong")
      continue
    else:
      notifikasi("--> ✅ Alamat Valid")

    # Tanggal Lahir
    while True: 
      try:
          tanggal_lahir_siswa = input("Masukan Tanggal Lahir : ")
          format_tanggal_lahir = "%Y-%m-%d"
          format_tanggal_lahir_siswa = datetime.strptime(tanggal_lahir_siswa, format_tanggal_lahir)
          format_tanggal_lahir_siswa2 = format_tanggal_lahir_siswa.strftime(format_tanggal_lahir)

          if tanggal_lahir_siswa == format_tanggal_lahir_siswa2  :
            notifikasi("--> ✅ Tanggal lahir telah ditambahkan")
            break
          
      except ValueError:
        notifikasi("Masukan Tanggal lahir dengan format benar")

    # Umur
    tanggal_hari_ini = datetime.now()
    umur_siswa = tanggal_hari_ini.year - format_tanggal_lahir_siswa.year

    if (tanggal_hari_ini.month, tanggal_hari_ini.day) < (format_tanggal_lahir_siswa.month, format_tanggal_lahir_siswa.day):
      umur_siswa -=1
  
    break

def data_pribadi_siswa_sekolah():

  while True:
    # Dictionary kumpulan data pribadi siswa
    kumpulan_data_pribadi_siswa_sekolah = data_pribadi_siswa
    # Apply fungsi untuk menambahkan data pribadi siswa
    identitas_pribadi_siswa_sekolah = identitas_pribadi_siswa()
    if identitas_pribadi_siswa_sekolah is None:
      break


def identitas_siswa_di_sekolah():

  """Fungsi untuk memasukan identitas siswa di sekolah
  """

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

  """Fungsi untuk menginput pada sebuah fungsi nilai mata pelajaran di sekolah
  """

  while True:
    try:
      input_nilai = int(input(f"Masukan Nilai {mata_pelajaran}"))
      return input_nilai
    except ValueError:
      print("Nilai yang anda masukan Tidak Valid, masukan angka")

def nilai_mata_pelajaran_ipa():

  """Fungsi untuk memasukan nilai mata pelajaran siswa kelas IPA
  """

  nilai_bahasa_indonesia = input_nilai_mata_pelajaran("Bahasa Indonesia = ")
  nilai_bahasa_inggris = input_nilai_mata_pelajaran("Bahasa Inggris = ")
  nilai_matematika = input_nilai_mata_pelajaran("Matematika = ")
  nilai_sejarah = input_nilai_mata_pelajaran("Sejarah = ")
  nilai_biologi = input_nilai_mata_pelajaran("Biologi = ")
  nilai_kimia = input_nilai_mata_pelajaran("Kimia = ")
  nilai_fisika =  input_nilai_mata_pelajaran("Fisika = ")

def nilai_mata_pelajaran_ips():

  """Fungsi untuk memasukan nilai mata pelajaran siswa kelas IPA
  """

  nilai_bahasa_indonesia = input_nilai_mata_pelajaran("Bahasa Indonesia = ")
  nilai_bahasa_inggris = input_nilai_mata_pelajaran("Bahasa Inggris = ")
  nilai_matematika = input_nilai_mata_pelajaran("Matematika = ")
  nilai_sejarah = input_nilai_mata_pelajaran("Sejarah = ")
  nilai_ekonomi = input_nilai_mata_pelajaran("Ekonomi = ")
  nilai_geografi = input_nilai_mata_pelajaran("Geografi = ")
  nilai_sosiologi =  input_nilai_mata_pelajaran("Sosiologi = ")



# print("\nPilihan Jurusan")
# print("1. IPA")
# print("2. IPS")

# pilihan_jurusan = input("Masukan Jurusan = ")
# if pilihan_jurusan == "1":
#   nilai_mata_pelajaran_ipa()
# elif pilihan_jurusan == "2":
#   nilai_mata_pelajaran_ips()
# else:
#   print("Masukan tepat")

data_pribadi_siswa_sekolah()