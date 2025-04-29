import tkinter as tk
from tkinter import messagebox
import json
from ttkthemes import ThemedStyle
import ttkthemes  # Optional for themes


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
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
    tasks = listbox.get(0, tk.END)
    with open("todo_guigood.json", "w") as f:
        json.dump(tasks, f)
    messagebox.showinfo("Saved", "Tasks saved successfully!")


def load_tasks():
    try:
        with open("todo_guigood.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass


# Create main window
root = tk.Tk()
root.title("📝 Modern To-Do List")
root.geometry("450x500")
root.configure(bg="#2b2b2b")  # Dark background


# Style for themed widgets
try:
    style = ThemedStyle(root)
    style.set_theme("arc")  # Clean light/dark theme
except:
    pass  # Fallback to basic styling


# Frame for List + Scrollbar
frame = tk.Frame(root, bg="#2b2b2b")
frame.pack(pady=10)

# Scrollable listbox
listbox = tk.Listbox(
    frame,
    width=40,
    height=12,
    font=("Helvetica", 12),
    bd=0,
    bg="#1f1f1f",
    fg="white",
    selectbackground="#4a90e2",
    activestyle="none",
    highlightthickness=0
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Entry box
entry = tk.Entry(
    root,
    font=("Helvetica", 14),
    width=30,
    bg="#444",
    fg="white",
    insertbackground='white'
)
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#2b2b2b")
btn_frame.pack(pady=10)

btn_add = tk.Button(btn_frame, text="Add Task", width=12, command=add_task, bg="#2ecc71", fg="white", font=("Helvetica", 10))
btn_add.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete Selected", width=14, command=delete_task, bg="#e74c3c", fg="white", font=("Helvetica", 10))
btn_delete.grid(row=0, column=1, padx=5)

btn_save = tk.Button(btn_frame, text="Save Tasks", width=12, command=save_tasks, bg="#3498db", fg="white", font=("Helvetica", 10))
btn_save.grid(row=0, column=2, padx=5)

btn_load = tk.Button(btn_frame, text="Load Tasks", width=12, command=load_tasks, bg="#9b59b6", fg="white", font=("Helvetica", 10))
btn_load.grid(row=0, column=3, padx=5)

# Load tasks at startup
load_tasks()

# Run the app
root.mainloop()