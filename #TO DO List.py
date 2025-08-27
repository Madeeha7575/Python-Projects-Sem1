#TO DO List
def task():
    tasks = [] #empty list
    print("__WELCOME TO THE TASK MANAGER APP__")
    total_task = int(input("How many tasks do you want to add?"))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i}:").lower()
        tasks.append(task_name)
        print(f"Today's tasks are\n{tasks}")
    while True:
        op = int(input("1-Add\n2-Update\n3-Remove\n4-View\n5-Exit\nEnter:"))
        if op == 1:
            add = input("Enter a task you want to add:").lower()
            tasks.append(add)
            print(f"Task {add} has been successfully added.")
        
        elif op == 2:
            updated_val = input("Enter a task you want to update:").lower()
            if updated_val in tasks:
                up = input("Enter new task:").lower()
                ind = tasks.index(updated_val)
                tasks[ind]= up
                print(f"Task {up} successfully updated.")
        elif op == 3:
            delete_val = input("Enter a task you want to delete:").lower()
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Task {delete_val} has been deleted.")
        elif op==4:
            print(f"Total tasks = {tasks}")   
        elif op ==5:
            print("Closing the app...")
            break
        else:
            print("Invalid input.Enter again.")     

task()
