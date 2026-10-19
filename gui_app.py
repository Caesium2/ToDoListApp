import tkinter as tk #Imports Tkinter and shortens the name to tk
from tkinter import messagebox #Imprts message boxes

#Import shared data from main.py
from tasks import taskList, add_task, complete_task,delete_task
def refresh_tasks(): #Prevents duplicates
    task_list.delete(0,tk.END) #Clears displayed tasks before refreshing by deleting everything from the first item to the last
    for task in taskList: #Gives each item a completion status displays it
        if task["completed"]:
            completionStatus = "[x]"
        else:
            completionStatus="[ ]"
        task_list.insert(tk.END, completionStatus + " " + task["name"])

def add_task_gui():
    name = entry.get() #reads what is typed into the input box
    
    if add_task(name): #Validates name
        entry.delete(0,tk.END) #Clears input box after a task is added successfully
        refresh_tasks() #Updates list with the new task
    else:
        messagebox.showinfo("Error","Enter a task!") #Provides user feedback
def complete_task_gui():
    selectedItem = task_list.curselection() #Finds the selected rows of the user and makes a tuple out of it
    
    if selectedItem and complete_task(selectedItem[0]): #Checks if both are true, second half pulls row number out of tuple and passes it to function in main.py
     #This ensures that not only an item is selected but that a valid input has been passed   
        refresh_tasks() #Updates list
    else:
        messagebox.showinfo("Error", "Enter a task!") #Provides user feedback

def delete_task_gui():
    selectedItem = task_list.curselection()
    
    if selectedItem and delete_task(selectedItem[0]): #Right condition is only checked if left one is true, therefore ensuring an emoty value isn't passed
        refresh_tasks()
    else:
        messagebox.showinfo("Error", "Enter a task!") #Requires a heading first, then a message
#Main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x400")

tk.Label(root,text="To-Do List", font=("Arial",20)).pack(pady=10) #.pack used to make widget appear, pady adds spacing
entry = tk.Entry(root) #Creates and saves a widget with root as its parent widget
entry.pack(fill="x",padx=20,pady=5) #Makes widget appear and fills full width of space given horizontally

tk.Button(root,text="Add Task", command = add_task_gui).pack(pady=5) #Button given a parent widget, a label, and the function called when the button is clicked. function is given brackets as error given otherwise
task_list = tk.Listbox(root) #Makes box which shows the tasks on the parent widget
task_list.pack(fill="both", expand=True,padx=20,pady=10)
tk.Button(root, text ="Complete Task", command = complete_task_gui).pack(pady=5)
tk.Button(root, text ="Delete Task", command = delete_task_gui).pack(pady=5)

refresh_tasks() #Fills list box at start in case there are previously saved tasks
root.mainloop() #Keeps window open and waits for interaction