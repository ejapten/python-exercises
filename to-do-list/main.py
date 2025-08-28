from datetime import datetime

daftar_tugas = {}

def notifikasi(teks):
    print("\n" + "."*60)
    print(f"{teks}")
    print("."*60)

def tampilkan_header(teks_header):
    print("\n" + "="*75)
    print(f"{teks_header}".center(70))
    print("="*75)

def tambah_nama_tugas():
  while True:
    nama_tugas = input("📝 Masukan tugas   : ")
    if nama_tugas.lower() == 'end':
      return None
    return nama_tugas

def tambah_tanggal_tugas():
  while True:
    try:
      tanggal_tugas = input("\n📅 Masukan Tanggal : ").strip()
      if tanggal_tugas == 'end':
        return None

      format_tanggal = "%Y-%m-%d"
      format_tanggal_tugas = datetime.strptime(tanggal_tugas, format_tanggal)
      return format_tanggal_tugas
    
    except ValueError:
      notifikasi (f"⚠️ Format tanggal anda '{tanggal_tugas}' Salah \n💡  Gunakan format YYYY-MM-DD")
      continue

def simpan_atau_tidak():

  while True:

    tugas_disimpan_atau_tidak = input("👉 Apakah tugas ingin disimpan sekarang? \n👉 (Y untuk simpan / N untuk lanjut menulis)  : ")
    
    if tugas_disimpan_atau_tidak.lower() == "y":
      notifikasi("✅ Berhasil disimpan!")
      return True   # kasih sinyal ke luar bahwa tugas disimpan
    
    elif tugas_disimpan_atau_tidak.lower() == "n":
      notifikasi("✅ Tugas disimpan, \n🔁 lanjutkan menambahkan tugas")
      return False  # kasih sinyal ke luar bahwa tidak disimpan
    
    else:
      notifikasi("⚠️ Masukan dengan benar")
      continue
    
def tambah_daftar_tugas_todolist():
  notifikasi("📌 ketik 'end' jika ingin keluar dari menu menambah tugas")

  while True:

    # Dictionary untuk menyimpa to-do-list
    daftar_tugas_yang_ditambahkan = daftar_tugas

    # Apply fungsi menambah tanggal  tugas
    tambah_daftar_tanggal_tugas = tambah_tanggal_tugas()
    if tambah_daftar_tanggal_tugas is None:
      break

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
      notifikasi(f"✅ Tugas {tambah_daftar_nama_tugas} berhasil ditambakan ke tanggl {tambah_daftar_tanggal_tugas.strftime('%Y-%m-%d')}")
    else:
      nomor = max(daftar_tugas_yang_ditambahkan.keys()) + 1 if daftar_tugas_yang_ditambahkan else 1
      daftar_tugas_yang_ditambahkan[nomor] = {"tanggal" : tambah_daftar_tanggal_tugas, "tugas" : [tambah_daftar_nama_tugas]}
      notifikasi(f"✅ Tugas {tambah_daftar_nama_tugas} berhasil dibuat pada tanggal {tambah_daftar_tanggal_tugas.strftime('%Y-%m-%d')}")

    # menanyankan untukk menyimpan tugas
    apakah_ingin_simpan_tugas = simpan_atau_tidak()
    if apakah_ingin_simpan_tugas:
      break
    else:
      continue

def melihat_daftar_tugas():
  if not daftar_tugas:
    notifikasi("⚠️ Belum ada tugas")
  else:
    print("\n📌 Daftar Tugas Anda:")
    for key, list_tugas in daftar_tugas.items():
      print(f"\n{key}. 📅 {list_tugas['tanggal'].strftime('%Y-%m-%d')}")
      for tugas_todolist in list_tugas["tugas"]:
        print(f"      ➡️  {tugas_todolist}")

def delete_by_tanggal():

  if not daftar_tugas:
    notifikasi("⚠️ Belum ada Tugas")
  else:

    hapus_tanggal = tambah_tanggal_tugas()
    hapus_tanggal = hapus_tanggal.strftime('%Y-%m-%d')
    
    for key, data in list(daftar_tugas.items()):
      if data["tanggal"].strftime("%Y-%m-%d") == hapus_tanggal:
        del daftar_tugas[key]
        notifikasi(f"✅ Tanggal {hapus_tanggal} berhasil dihapus")
        return
    notifikasi(f"⚠️ Tanggal {hapus_tanggal} tidak ditemukan")

def menyelesaikan_tugas():
  if not daftar_tugas:
    notifikasi("⚠️ Belum ada Tugas")

  else:
    tanggal_selesaikan_tugas = tambah_tanggal_tugas()
    tanggal_selesaikan_tugas = tanggal_selesaikan_tugas.strftime('%Y-%m-%d')

    tugas_yang_diselesaikan = tambah_nama_tugas()

    for key, data in daftar_tugas.items():
      if data["tanggal"].strftime("%Y-%m-%d") ==  tanggal_selesaikan_tugas:
        for i, tugas in enumerate(data["tugas"]):
          if tugas == tugas_yang_diselesaikan:
            data["tugas"][i] = f"✔️ ~~{tugas}~~"
            notifikasi(f"✅ Tugas '{tugas_yang_diselesaikan}' pada tanggal {tanggal_selesaikan_tugas} ditandai selesai")
            return
        notifikasi(f"⚠️ Tugas '{tugas_yang_diselesaikan}' tidak ditemukan pada tanggal {tanggal_selesaikan_tugas}")
    notifikasi(f"⚠️ Tanggal {tanggal_selesaikan_tugas} tidak ditemukan")

print("\n" + "="*80)
print("📌  MENU UTAMA - TO DO LIST  📌".center(75))
print("="*80)

while True:
  print("\n"+"-"*45)
  print("Pilihan Menu:")
  print(" 1. ✍️ Tambah Tugas")
  print(" 2. 📋 Daftar Tugas")
  print(" 3. ✔️ Tandai tugas selesai")
  print(" 4. 🗑️ Hapus Tugas Per Tanggal")
  print(" 5. 🚪 Keluar")
  print("-"*45)

  print("\n" + "-"*28)
  pilihan_menu = input("--> 📥 Masukan Pilihan : ")
  print("-"*28)

  if pilihan_menu == "1":
    tampilkan_header("ℹ️ Masukan Tanggal dan Nama Tugas ℹ️")
    tambah_daftar_tugas_todolist()

  elif pilihan_menu == "2":
    tampilkan_header("📋 Daftar Tugas ")
    melihat_daftar_tugas()

  elif pilihan_menu == "3":
    tampilkan_header("✔️ Pilih Tugas yang Sudah Selesai")
    menyelesaikan_tugas()

  elif pilihan_menu == "4":
    tampilkan_header("🗑️ Hapus Tugas per Tanggal")
    delete_by_tanggal()

  elif pilihan_menu == "5":
    break

  else:
    print("⚠️ Masukan pilihan yang tepat")
    continue






