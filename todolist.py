from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Invalid task", "Please enter a task!")

def delete_task():
    try:
        selected_task = task_list.curselection()
        task_list.delete(selected_task)
    except:
        messagebox.showwarning("No task selected", "Please select a task to delete!")

root = Tk()
root.title("To-Do List")
root.config(bg="PaleVioletRed")
root.geometry('300x400')

task_entry = Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

task_frame = Frame(root, bg="white")
task_frame.pack(pady=10)

task_scroll = Scrollbar(task_frame)
task_scroll.pack(side=RIGHT, fill=Y)

task_list = Listbox(task_frame, font=("Futura", 12), width=50, height=10, bd=0, yscrollcommand=task_scroll.set)
task_list.pack(side=LEFT, fill=BOTH)
task_scroll.config(command=task_list.yview)

add_button = Button(root, text="Add Task", font=("Futura", 12), command=add_task)
add_button.pack(pady=10, padx=10)

delete_button = Button(root, text="Delete Task", font=("Futura", 12), command=delete_task)
delete_button.pack(pady=10)

root.mainloop()
