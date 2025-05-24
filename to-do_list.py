xyz = []
print("Welcome to To-Do list - ")
while True:

    print(" 1. Add Task\n 2. View Task\n 3. Mark Complete\n 4. delete Task\n 5. Exit\n (Which ever command you want to insert, the the number in it's front)")
    try:
        abc = int(input("Enter your command:- \n"))
    except ValueError:
        print("Please enter a valid command.")
        continue
    if abc == 1:
        task = input("Enter your task:- \n")
        xyz.append({"task": task, "Completed": False})
        print("task added successfully\n")
    elif abc == 2:
        if not xyz:
            print("No tasks are assigned yet")
        else:
            for i, task in enumerate(xyz, start = 1):
                status = "O" if task["Completed"] else "X"
                print(f"{i}. {status} {task['task']}")
                
    elif abc == 3:
        if not xyz:
            print("no tasks to mark as completed")
        else:
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(xyz):
                    xyz[index]["Completed"] = True
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif abc == 4:
        if not xyz:
            print("No tasks to delete.")
        else:
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(xyz):
                    deleted = xyz.pop(index)
                    print(f"Deleted task: {deleted['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif abc == 5:
        print("You have exited the to-do list. Goodbye!")
        break
    else:
        print("You've entered the wrong command.")
    print("\n")