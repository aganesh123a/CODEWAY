import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("TODO List")
root.configure(bg="#f0f0f0")  # Light gray background

frame_tasks = tk.Frame(root, bg="#f0f0f0")  # Light gray background
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg="#ffffff", fg="#333333", selectbackground="#cce5ff")  
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, bg="#ffffff", fg="#333333") 
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task, bg="#4CAF50", fg="#ffffff")  
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task, bg="#FF5733", fg="#ffffff")
button_delete_task.pack()

root.mainloop()
