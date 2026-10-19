import tkinter as tk #Imports Tkinter and shortens the name to tk
from tkinter import messagebox #Imprts message boxes

#Import shared data from main.py
from main import taskList, add_task, complete_task,delete_task
def refresh_tasks(): #Prevents duplicates
    task_list.delete(0,tk.END) #Clears displayed tasks before refreshing by deleting everything from the first item to the last
    for task in taskList:
        if task["completed"]:
            completionStatus = "[x]"
        else:
            completionStatus="[ ]"
        task_list.insert(tk.END, completionStatus + " " + task["name"])

def add_task_gui():
    name = entry.get() #Gets typed into the input box
    
    if add_task(name):
        entry.delete(0,tk.END) #Clears input box after a task is added successfully
        refresh_tasks() #Updates list with the new task
    else:
        messagebox.showinfo("Error","Enter a task!") #Provides user feedback
def complete_task_gui():
    selectedTaskIndex = task_list.curselection()
    
    if selectedTaskIndex:
        complete_task(selectedTaskIndex[0])
        refresh_tasks()
    else:
        messagebox.showinfo("Error", "Enter a task!") #Provides user feedback

def delete_task_gui():
    selectedTaskIndex = task_list.curselection()
    
    if selectedTaskIndex:
        delete_task(selectedTaskIndex[0])
        refresh_tasks()
    else:
        messagebox.showinfo("Error", "Enter a task!") #Requires a heading first, then a message
#Main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x400")

tk.Label(root,text="To-Do List", font=("Arial",20)).pack(pady=10)
entry = tk.Entry(root)
entry.pack(fill="x",padx=20,pady=5)

tk.Button(root,text="Add Task", command = add_task_gui).pack(pady=5)
task_list = tk.Listbox(root)
task_list.pack(fill="both", expand=True,padx=20,pady=10)
tk.Button(root, text ="Complete Task", command = complete_task_gui).pack(pady=5)
tk.Button(root, text ="Delete Task", command = delete_task_gui).pack(pady=5)

refresh_tasks()
root.mainloop()