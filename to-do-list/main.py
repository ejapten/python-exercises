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
      return format_tanggal_tugas
    
    except ValueError:
      print(f"Format tanggal anda '{tanggal_tugas}' Salah, masukan dalam bentuk format yang benar")
      continue

def simpan_atau_tidak():
  while True:
    tugas_disimpan_atau_tidak = input("Apakah tugas ingin disimpan? (Y/N) : ")
    
    if tugas_disimpan_atau_tidak.lower() == "y":
      print("Berhasil disimpan!")
      return True   # kasih sinyal ke luar bahwa tugas disimpan
    
    elif tugas_disimpan_atau_tidak.lower() == "n":
      print("Tugas disimpan, lanjutkan menambahkan tugas")
      return False  # kasih sinyal ke luar bahwa tidak disimpan
    
    else:
      print("\nMasukan dengan benar")
      continue

def tambah_daftar_tugas_todolist():
  while True:
    # Dictionary untuk menyimpa to-do-list
    daftar_tugas_yang_ditambahkan = daftar_tugas

    # Apply fungsi menambah tanggal  tugas
    tambah_daftar_tanggal_tugas = tambah_tanggal_tugas()

    # Apply Fungsi menambah nama tugas
    tambah_daftar_nama_tugas = tambah_nama_tugas()
    if tambah_daftar_nama_tugas is None:
      break

    # Cek apakah tanggal sudah ada
    nomor_as_key = None
    for key, data in daftar_tugas_yang_ditambahkan.items():
      if data['tanggal'] == tambah_daftar_tanggal_tugas:
        nomor_as_key = key
        break
    
    # Menambahan to-do-list
    if nomor_as_key:
      daftar_tugas_yang_ditambahkan[nomor_as_key]["tugas"].append(tambah_daftar_nama_tugas)
      print(f"Tugas {tambah_daftar_nama_tugas} berhasil ditambakan ke tanggl {tambah_daftar_tanggal_tugas.strftime('%Y-%m-%d')}")
    else:
      nomor = max(daftar_tugas_yang_ditambahkan.keys()) + 1 if daftar_tugas_yang_ditambahkan else 1
      daftar_tugas_yang_ditambahkan[nomor] = {"tanggal" : tambah_daftar_tanggal_tugas, "tugas" : [tambah_daftar_nama_tugas]}
      print(f"Tugas baru berhasil dibuat pada tanggal {tambah_daftar_tanggal_tugas.strftime('%Y-%m-%d')} dengan nomor {nomor}!\n")

    # menanyankan untukk menyimpan tugas
    apakah_ingin_simpan_tugas = simpan_atau_tidak()
    if apakah_ingin_simpan_tugas:
      break
    else:
      continue

def melihat_daftar_tugas():
  if not daftar_tugas:
    print("\n Belum ada tugas")
  else:
    for key, list_tugas in daftar_tugas.items():
      print(f"\n{key}. {list_tugas['tanggal'].strftime('%Y-%m-%d')}")
      for tugas_todolist in list_tugas["tugas"]:
        print(f"- {tugas_todolist}")

def delete_by_tanggal():
  hapus_tanggal = input("Masukan Tanggal yang ingin dihapus : ")
  for key, data in list(daftar_tugas.items()):
    if data["tanggal"].strftime("%Y-%m-%d") == hapus_tanggal:
      del daftar_tugas[key]
      print(f"Tanggal {hapus_tanggal} berhasil dihapus")
      return
  print(f"Tanggal {hapus_tanggal} tidak ditemukan")

def menyelesaikan_tugas():
  tanggal_selesaikan_tugas = input("Masukan Tangal : ")
  tugas_yang_diselesaikan = input("Masukan Tugas yang sudah diselesaikan : ")
  for key, data in daftar_tugas.items():
    if data["tanggal"].strftime("%Y-%m-%d") ==  tanggal_selesaikan_tugas:
      for i, tugas in enumerate(data["tugas"]):
        if tugas == tugas_yang_diselesaikan:
          data["tugas"][i] = f"~~{tugas}~~"
          print(f"Tugas '{tugas_yang_diselesaikan}' pada tanggal {tanggal_selesaikan_tugas} ditandai selesai")
          return
      print(f"Tugas '{tugas_yang_diselesaikan}' tidak ditemukan pada tanggal {tanggal_selesaikan_tugas}")
  print(f"Tanggal {tanggal_selesaikan_tugas} tidak ditemukan")

while True:
  print("\n" + "-"*20)
  print("Pilihan Menu:")
  print("1. Tambah Tugas")
  print("2. Daftar Tugas")
  print("3. Hapus tugas")
  print("4. Hapus Tugas Berdasakan Tanggal")
  print("5. Keluar")

  pilihan_menu = input("Masukan Pilihan : ")
  if pilihan_menu == "1":
    tambah_daftar_tugas_todolist()
  elif pilihan_menu == "2":
    melihat_daftar_tugas()
  elif pilihan_menu == "3":
    menyelesaikan_tugas()
  elif pilihan_menu == "4":
    delete_by_tanggal()
  elif pilihan_menu == "5":
    break
  else:
    print("Masukan pilihan yang tepat")
    continue




