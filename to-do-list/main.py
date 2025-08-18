from datetime import datetime

# Menambah Tugas
def add_task():
  todo_list = {}
  print("Format date and time -> Years-Month-Day Hours:Minute:Second")

  while True:
    while True:
      try:
        enter_date_task = input("Masukan Tanggal : ").strip()
        format_date = '%Y-%m-%d %H:%M:%S'
        date_task = datetime.strptime(enter_date_task, format_date)
        todo_list['Date'] = date_task
        break

      except ValueError:
        print(f"Format tanggal anda '{enter_date_task}' Salah, masukan dalam bentuk format yang benar")
        continue

    enter_task = input("Masukan tugas : ")
    if enter_task == 'end':
      break

    todo_list['Task'] = enter_task


  # Menampilkan output tanggal dalam bentuk 'contoh : 2009-12-23 14:40:12'
  # print(f"Task : {todo_list['Task']}")
  # print(f"Date : {todo_list['Date'].strftime(date_task)} | Task : {todo_list['Task']}")
  # print(todo_list)
  

  return 
  
add_task()

# Menampilkan tugas
#def displays_list():
 # print(add_task())
#displays_list()





