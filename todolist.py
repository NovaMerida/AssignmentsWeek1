print("ToDoList")
tasks = [] 
while True: 
  print("Press 1 to add task") 
  print("Press 2 to delete task ")
  print("Press 3 to view all tasks")
  print("Press q to quit")
  choice = input("Enter choice: ")
  if choice == "1": 
    title = input("Enter title: ")
    priority = input("Enter priority: ")
    task = {"title": title, "priority": priority} 
   
    tasks.append(task)

  if choice == "2":
    for index in range(0, len(tasks)): 
      task = tasks[index] 
      print("choice the number corresponding with the task below delete: ")
      print(f"{index + 1} - {task['title']} - {task['priority']}")

    delete_input = int(input("Which task you want to delete? (enter a number): "))

    tasks.pop(delete_input-1)
    
  if choice == "3":
    for index in range(0, len(tasks)): 
      task = tasks[index] 
      print(f"{index + 1} - {task['title']} - {task['priority']}")

  elif choice == "q":
    break