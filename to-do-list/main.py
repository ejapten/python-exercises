from datetime import datetime

todo_list = {}

# Menambah Tugas
def add_task():
  print("Format date and time -> Years-Month-Day")

  while True:

    # Input Tanggal
    while True:
      try:
        enter_date_task = input("\nMasukan Tanggal : ").strip()
        # Format Tanggal
        format_date = '%Y-%m-%d'
        date_task = datetime.strptime(enter_date_task, format_date)
        break

      except ValueError:
        print(f"Format tanggal anda '{enter_date_task}' Salah, masukan dalam bentuk format yang benar")
        continue

    # Input Nama tugas yang akan dikerjakan 
    enter_task = input("Masukan tugas : ")
    if enter_task == 'end': #  jika tidak ingin menambahkan tugas
      break

    # Menambahkan ke dalam penyimpanan
    if date_task in todo_list:
      print(f"\n-->Tanggal {date_task.strftime('%Y-%m-%d')} sudah ada, menambahkan tugas baru.")
      todo_list[date_task].append(enter_task)
    else:
      print(f"\n-->Membuat entri baru untuk tanggal {date_task.strftime('%Y-%m-%d')}.")
      todo_list[date_task] = [enter_task] 


    # Input Lanjutan untuk simpan
    while True : 
      input_simpan = input("\nApakah ingin disimpan?\n")
      if input_simpan.lower() == "simpan":
        for key, task_list in todo_list.items():
          tasks_str = ", ".join(task_list) # ubah list menjadi string dengan dipisahkan koma dan spasi
          print(f"\nTanggal: {key.strftime('%Y-%m-%d')} | Tugas: {tasks_str}")
        exit()
      elif input_simpan.lower() == "tidak simpan":
        break
      else:
        print("\nMasukan dengan benar")
        continue

  return 
  
add_task()





