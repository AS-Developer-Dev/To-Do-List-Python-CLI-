from colorama import Fore
print ("")
print ("")
print ("")
print ("<<========================================================================================================>>")
print ("                                       Welcome To To Do List")
print ("<<========================================================================================================>>")
print ("")
list = []
while True:
    print ("")
    print (Fore.YELLOW + "1. Add Task")
    print (Fore.YELLOW + "2. View Tasks")
    print (Fore.YELLOW + "3. Remove Task")
    print (Fore.YELLOW + "4. Exit")
    try:
        choice = int(input(Fore.LIGHTBLUE_EX + "Enter your choice (1-4): "))
        if choice == 0 or choice >= 5:
            raise ValueError
        else:
            #Add Task
            if choice == 1:
                print ("")
                task = input(Fore.CYAN + "Enter the task you want to add: ")
                if task.strip() == "":
                    print ("")
                    print (Fore.RED + "Task cannot be empty. Please enter a valid task.")
                    print ("")
                    continue
                else:
                    list.append(task)
                    print ("")
                    print("Task added successfully!")
                    print ("")


                #View Tasks
            elif choice == 2:
                if not list:
                    print ("")
                    print (Fore.YELLOW + "No tasks in the list.")
                    print ("")
                else:
                    print ("")
                    print (Fore.GREEN + "Tasks in the list:")
                    
                    for index, task in enumerate(list, start=1):
                        print ("-----------")
                        print (f"{index}. {task}")

                #Remove Task
            elif choice == 3:
                if not list:
                    print ("No tasks to remove.")
                else:
                    print ("")
                    print (Fore.GREEN + "Tasks in the list:")
                    for index, task in enumerate(list, start=1):
                        print ("-----------")
                        print (f"{index}. {task}")

                    try:
                        remove_task = int(input(Fore.CYAN + "Enter the number of the task you want to remove: "))
                        if remove_task <= 0 or remove_task > len(list):
                            raise ValueError
                        else:
                            remove_task = list.pop(remove_task - 1)
                            print ("")
                            print (Fore.YELLOW + "Task removed successfully!")
                            print ("")
                    except ValueError:
                        print ("")
                        print (Fore.RED + "Invalid input. Please enter a valid task number.")
                        print ("")
                        continue

            elif choice == 4:
                print ("Exiting the program. Goodbye!")
                break        
            
    
            
    except ValueError:
        print ("")
        print(Fore.RED + "Invalid input. Please enter a number between 1 and 4.")
        print ("")
        continue