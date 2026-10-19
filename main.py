import json

def save_tasks():
    with open("tasks.json", "w") as file: #Opens file for writing and creates it if it does not exist. with closes file after operation is completed
        json.dump(taskList,file,indent=4)
def load_tasks():
    global taskList
    try:
        with open("tasks.json","r") as file:
            taskList = json.load(file)
    except FileNotFoundError:
        taskList=[] #Task list is empty if saved one cannot be found
def show_Menu():
    print("--- To Do List---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Tasks")
    print("5. Exit")
def user_Choice():
    while True:
        show_Menu()
        userChoice = input("Choose an option: ")
        match userChoice: #Newly implemented switch statements
            case "1":
                print("View Tasks Selected")
                view_Tasks()
            case "2":
                print("Add Task Selected")
                add_Task()
            case "3":
                print("Complete Task Selected")
                complete_Task()
            case "4":
                print("Delete Task Selected")
                delete_Task()
            case "5":
                print("Goodbye")
                break
            case _: #Underscore acts as default case signifier
                print("Invalid choice, try again.")
def add_Task():
    userTask= { #Dictionary used to track if a task is completed
        "name":input("Enter your task: ").strip(),
         "completed":False      }
    if userTask["name"].strip()=="":
        print("Task cannot be empty")
    else:
        taskList.append(userTask)
        save_tasks()
        print("Task added successfully")
    
def view_Tasks():
    if len(taskList)==0:
        print("No tasks yet!")
    else:
        print("Current Tasks")
        for index in range(len(taskList)):
            if taskList[index]["completed"]:
                print((index+1),". [x]",taskList[index]["name"])
            else:
                print((index+1),". [ ]",taskList[index]["name"])
    
def complete_Task():
    if len(taskList)>0:
        try:
            taskNum=int(input("Which task number would you like to mark as completed?"))
        except ValueError:
            print("Please input a number")
        else:
            
            if taskList[taskNum-1]["completed"]:
                print("Task is already completed")
            elif taskNum>0 and taskNum<=len(taskList):
                taskList[taskNum-1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number put in, please try again")
    else:
        print("Task list is empty, please try again")
        
def delete_Task():
    if len(taskList)>0:
        taskNum=int(input("Which task number would you like to remove?"))
        taskList.pop(taskNum-1)
    else:
        print("Task List is empty")
        
#Program starts here
taskList=[]
load_tasks()
user_Choice()


