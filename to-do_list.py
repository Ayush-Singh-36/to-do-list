import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
from plyer import notification

tasks = []

window = tk.Tk()
window.title("To-Do List")
window.geometry("700x500")

def add_task():
    task = task_entry.get()
    due = due_entry.get_date()
    priority = priority_var.get()
    category = category_var.get()

    if task.strip() == "":
        messagebox.showwarning("Input Error, Task cannot be empty!")
        return
    task.append({
        "task": task,
        "completed": False,
        "due_date": due.strftime("%Y-%m-%d"),
        "priority": priority,
        "category": category
    })
    task_entry.delete(0, tk.END)
    update_task_list()
    messagebox.showinfo("Success", "Task added successfully!")

def update_task_list(filter_text = ""):
    task_list.delete(*task_list.get_children())
    for i, t in enumerate(tasks):
        if filter_text.lower() in t["task"].lower():
            status = "Done" if t["completed"] else "Not yet"
            task_list.insert("", "end", iid = i, values = (status, t["due_date"], t["priority"], t["category"]))

def mark_complete():
    selected = task_list.focus()
    if selected:
        tasks[int(selected)]["completed"] = True
        update_task_list()

def delete_task():
    selected = task_list.focus()
    if selected:
        del tasks[int(selected)]
        update_task_list()

def search_task(event = None):
    filter_text = search_entry.get()
    update_task_list(filter_text)

def notify_due_tasks():
    today = datetime.today().strftime("%Y-%m-%d")
    for t in tasks:
        if not t["completed"] and t["due_date"] == today:
            notification.notify(
                title = "Task-Reminder",
                message = f"Today: {t['task']}, ({t['category']}, {t['priority']})",
                timeout = 5
            )

add_frame = tk.LabelFrame(window, text="Add new task", padx=10, pady=10)
add_frame.pack(padx=10, pady=10, fill="x")

tk.Label(add_frame, text="Task:").grid(row=0, column=0, sticky="w")
task_entry = tk.Entry(add_frame, width=30)
task_entry.grid(row=0, column=1)

tk.Label(add_frame, text="Due date:").grid(row=0, column=2)
due_entry = DateEntry(add_frame, width= 12, bg = "darkblue", fg= "white", borderwidth= 2)
due_entry.grid(row= 0, column= 3)

tk.Label(add_frame, text="priority:").grid(row=1, column=0, sticky="w")
priority_var = tk.StringVar()
priority_menu = ttk.Combobox(add_frame, textvariable=priority_var, values=["High", "Medium", "Low"], state="readonly")
priority_menu.grid(row= 1, column= 1)
priority_menu.current(1)

tk.Label(add_frame, text="Category:").grid(row=1, column=2)
category_var = tk.StringVar(value="General")
category_menu = ttk.Combobox(add_frame, textvariable=category_var, values=["Personal", "Work", "Study", "Other"])
category_menu.grid(row=1, column=3)

tk.Button(add_frame, text="Add Task", command=add_task).grid(row=0, column=4, rowspan=2, padx=10)

search_frame = tk.Frame(window)
search_frame.pack(padx=10, pady=5, fill="x")

tk.Label(search_frame, text="Search:").pack(side="left")
search_entry = tk.Entry(search_frame)
search_entry.pack(side="left", fill="x", expand=True, padx=5)
search_entry.bind("<KeyRelease>", search_task)

task_list = ttk.Treeview(window, columns=("Status", "Task", "Due", "Priority", "Category"), show="headings")
task_list.heading("Status", text="Done")
task_list.heading("Task", text="Task")
task_list.heading("Due", text="Due Date")
task_list.heading("Priority", text="priority")
task_list.heading("Category", text="Category")
task_list.pack(padx=10, pady=10, fill="both", expand=True)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Mark Complete", command=mark_complete).pack(side="left", padx=10)
tk.Button(btn_frame, text="Delete Task", command=delete_task).pack(side="left", padx=10)
tk.Button(btn_frame, text="Notify Today's Tasks", command=notify_due_tasks).pack(side="left", padx=10)

update_task_list()
window.mainloop()
