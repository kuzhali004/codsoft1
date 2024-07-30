tasks = []

def add_task(task):
  tasks.append(task)

def remove_task(task):
  tasks.remove(task)

def view_tasks():
  for task in tasks:
    print(task)

while True:
  print("Options:")
  print("1. Add task")
  print("2. Remove task")
  print("3. View tasks")
  print("4. Quit")
  
  choice = input("Enter your choice: ")
  
  if choice == "1":
    task = input("Enter task: ")
    add_task(task)
  elif choice == "2":
    task = input("Enter task to remove: ")
    remove_task(task)
  elif choice == "3":
    view_tasks()
  elif choice == "4":
    break
  else:
    print("Invalid choice")
