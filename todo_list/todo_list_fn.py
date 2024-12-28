list = []

def add_task():
    idx = 1
    task = input("Enter The Task:\n")
    list.append(task)
    print(f"Task {idx}: {task}")
    idx+=1

def view_tasks():
     if not list:
        print("There are no tasks to display!\n")
     else:
        for idx, task in enumerate(list, start=1):
            print(f"Task {idx}: {task}")

def remove_task():
     if not list:
        print("There are no tasks to remove!\n")
     else:
        task = input("Enter The Task:\n")
        if task in list:
            list.remove(task)      
        else:
            print("Invalid Task!")


print("\t\t\t\t##############################\n\n\t\t\t\t*********MY TO-DO LIST*********\t\n\n\t\t\t\t##############################")

while (True):
    user_input = input("Enter Your Command: (add || view || remove || exit)\n")

    if (user_input == 'add'):
        add_task()
    elif (user_input == 'view'):
        view_tasks()
    elif (user_input == 'remove'):
        remove_task()
    elif (user_input == 'exit'):
        exit()
    else:
        print("Invalid Command!\n")




    