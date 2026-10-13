import os
taskfile="tasks.txt"

#Add tasks to the list
def add_task(tasks_ls):
    task=input("Enter a Task to add:   ").strip()
    if task:
        tasks_ls.append(task)
        print("Task added successfully")
    else:
        print("Task can not be empty")

# remove completed tasks
def remove_task(tasks_ls):
    if not tasks_ls:
        print("There are no tasks in the list")
        return
    view_tasks(tasks_ls)
    try:
        index=int(input("Enter the task number you completed"))-1
        if index>=0 or index<len(tasks_ls):
            remove=tasks_ls.pop(index)
            print("Cleared Task",remove)
        else:
            print("Invalid Task number")
    except ValueError:
        print("Please enter valid number")
    

#Write a function to view the current task list.
def view_tasks(tasks_ls):
    if not tasks_ls:
        print("Your task list is empty")
    else:
        print("\n******Current Tasks*********")
        for index,task in enumerate(tasks_ls,start=1):
            print(f"{index}.{task}")
    print("-"*25)

    #Write a function to save and load tasks from a file.
def save_task(tasks_ls):
    try:
        with open(taskfile,'w')as file:
            for task in tasks_ls:
                file.write(task+"\n")
        print("Tasks saved to file")
    except IOError as e:
        print("Error saving task",e)

def load_task():
    tasks=[]
    if not os.path.exists(taskfile):
        return tasks
    try:
        with open(taskfile,'r')as file:
            tasks=[line.strip() for line in file.readlines() if line.strip()]
        print("Tasks loaded from file")
    except IOError as e:
        print("Error loading Tasks from file",e)
    return tasks
def main():
    tasks=load_task()

    while True:
        print("\n-----------Task manager Menu------------")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Remove Completed Tasks")
        print("4. Save & Exit")

        choice=input("Choose an option (1-4): ").strip()

        if choice=="1":
            view_tasks(tasks)
        elif choice=="2":
            add_task(tasks)
        elif choice=="3":
            remove_task(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1-4")
main()
