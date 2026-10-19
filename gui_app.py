import tkinter as tk

#Main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x400")

#Heading

heading = tk.Label(
    root,
    text="List",
    font=("Arial",20,"bold")
    )
heading.pack(pady=20)
root.mainloop()