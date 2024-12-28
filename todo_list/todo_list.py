list = []

index =1 

print("\t\t\t\t##############################\n\n\t\t\t\t*********MY TO-DO LIST*********\t\n\n\t\t\t\t##############################")

while (True):
    user_input = input("Enter Your Command: (add || view || remove || exit)\n")

    if (user_input == 'add'):
        task = input("Enter The Task:\n")
        list.append(task)
        print(f"Task {index}: {task}")
        index+=1

    elif (user_input == 'view'):
        if not list:
            print("There are no tasks to display!\n")
        else:
            for idx, task in enumerate(list, start=1):
                print(f"Task {idx}: {task}")

    elif (user_input == 'remove'):
        if not list:
            print("There are no tasks to remove!\n")
        else:
            task = input("Enter The Task:\n")
            if task in list:
                list.remove(task)      
            else:
                print("Invalid Task!")
                
    elif (user_input == 'exit'):
        exit()

    else:
        print("Invalid Command!\n")