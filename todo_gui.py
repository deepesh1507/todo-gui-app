import tkinter as tk
from tkinter import messagebox
import json

def add_task():
    todo_gui_entry = entry.get()
    if todo_gui_entry:
        listbox.insert(tk.END, todo_gui_entry)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def save_tasks():
    todo_gui_entry = listbox.get(0, tk.END)
    with open("todo_gui_entry.json", "w") as f:
        json.dump(todo_gui_entry, f)
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("todo_gui_entry.json", "r") as f:
            todo_gui_entry = json.load(f)
            for task in todo_gui_entry:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# GUI Setup
root = tk.Tk()
root.title("📝 To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Selected", command=delete_task)
btn_delete.pack(pady=5)

btn_save = tk.Button(root, text="Save Tasks", command=save_tasks)
btn_save.pack(pady=5)

btn_load = tk.Button(root, text="Load Tasks", command=load_tasks)
btn_load.pack(pady=5)

load_tasks()  # Load saved todo_gui_entry on start

root.mainloop()