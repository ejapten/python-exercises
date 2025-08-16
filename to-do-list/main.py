from datetime import datetime

# Menambah Tugas
def add_task():
  todo_list = {}

  print("Format date and time -> Years-Month-Day Hours:Minute:Second")
  enter_date_task = input("Enter a date and time : ")  
  date_task_format = '%Y-%m-%d %H:%M:%S'
  date_task = datetime.strptime(enter_date_task, date_task_format)
    
  todo_list['Date'] =  date_task.strftime(date_task_format)

  print(todo_list)

  return 
  
add_task()

# Menampilkan tugas
#def displays_list():
 # print(add_task())
#displays_list()





