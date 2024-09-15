task = []

def addTask():
    new_task = input("Please add a task: ")
    task.append(new_task)
    print(f"Task `{new_task}´ added to the list.")


def listTasks():
    if not task:
        print("There are no tasks currently")
    else: 
        print("Curren Task: ")
        for index, t in enumerate(task):
            print(f"Task #{index }.{t}")
        
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the number the task you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(task):
            removed_task= task.pop(taskToDelete)
            print(f"Task '{removed_task}' was removed.")
        else:
            print(f"Task #{taskToDelete } was not found.")
    except:
        print("Invalid input")




if __name__ == "__main__":
    print("Welcome to the to-do list app")
    while True:
        print("\n")
        print("please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")
    print("Goodbye")