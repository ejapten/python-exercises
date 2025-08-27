from datetime import datetime

daftar_tugas = {}

def tambah_nama_tugas():
  while True:
    nama_tugas = input("Masukan tugas : ")
    if nama_tugas == 'end':
      return None
    return nama_tugas

def tambah_tanggal_tugas():
  while True:
    try:
      tanggal_tugas = input("Masukan Tanggal : ").strip()
      format_tanggal = "%Y-%m-%d"
      format_tanggal_tugas = datetime.strptime(tanggal_tugas, format_tanggal)
      return format_tanggal_tugas.strftime(format_tanggal)
    
    except ValueError:
      print(f"Format tanggal anda '{tanggal_tugas}' Salah, masukan dalam bentuk format yang benar")
      continue

def tambah_daftar_tugas_todolist():
  while True:

    tambah_daftar_tanggal_tugas = tambah_tanggal_tugas()

    tambah_daftar_nama_tugas = tambah_nama_tugas()
    if tambah_daftar_nama_tugas is None:
      break

    # nomor urut sebagai key
    if daftar_tugas:
      nomor = max(daftar_tugas.keys()) + 1
    else:
      nomor = 1

    daftar_tugas[nomor] = {"tanggal":tambah_daftar_tanggal_tugas, "tugas":tambah_daftar_nama_tugas}
    print(f"Tugas berhasil ditambahkan dengan nomor {nomor}!\n")

tambah_daftar_tugas_todolist()
print("\nDaftar tugas:", daftar_tugas)





