import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Loads data from JSON or returns an empty list if file is missing."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def save_tasks(self):
        """Saves current task list to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        
        self.manager = TodoManager()

        self.title_label = tk.Label(root, text="My Tasks", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=15)

        self.task_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=5)
        self.task_entry.bind('<Return>', lambda event: self.add_task()) # Allow 'Enter' key to add

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, 
                                   bg="#4CAF50", fg="white", width=15, font=("Arial", 10, "bold"))
        self.add_button.pack(pady=10)

        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=12)
        self.tasks_listbox.pack(pady=10, padx=20)

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_task, 
                                      bg="#f44336", fg="white", width=15, font=("Arial", 10, "bold"))
        self.delete_button.pack(pady=5)

        self.refresh_listbox()

    def refresh_listbox(self):
        """Clears and repopulates the list with ordered numbering."""
        self.tasks_listbox.delete(0, tk.END)
        
        for idx, item in enumerate(self.manager.tasks, 1):
            display_text = f"{idx}. {item['task']}"
            self.tasks_listbox.insert(tk.END, display_text)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.manager.tasks.append({"task": task_text, "done": False})
            self.manager.save_tasks()
            self.task_entry.delete(0, tk.END)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task name.")

    def delete_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            self.manager.tasks.pop(selected_index)
            self.manager.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task from the list to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()