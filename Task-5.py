import tkinter as tk
from tkinter import messagebox
import json
import os

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        self.file_path = "contacts.json"
        self.contacts = self.load_data()

        self.setup_ui()
        self.refresh_list()

    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump(self.contacts, f, indent=4)

    def setup_ui(self):

        input_frame = tk.LabelFrame(self.root, text="Add / Update Contact", padx=10, pady=10)
        input_frame.pack(padx=10, pady=10, fill="x")

        input_frame.columnconfigure(1, weight=1)

        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew", pady=5)

        tk.Label(input_frame, text="Phone:").grid(row=1, column=0, sticky="w", pady=5)
        self.phone_entry = tk.Entry(input_frame)
        self.phone_entry.grid(row=1, column=1, sticky="ew", pady=5)

        btn_frame = tk.Frame(input_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(
            btn_frame, text="Save Contact", width=15,
            command=self.add_contact
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame, text="Delete Selected", width=15, fg="red",
            command=self.delete_contact
        ).pack(side="left", padx=5)

        list_frame = tk.Frame(self.root)
        list_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(list_frame, text="Stored Contacts", font=("Arial", 10, "bold")).pack(anchor="w")

        listbox_frame = tk.Frame(list_frame)
        listbox_frame.pack(fill="both", expand=True)

        self.contact_listbox = tk.Listbox(listbox_frame, font=("Courier", 10))
        self.contact_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.contact_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contact_listbox.yview)

        self.contact_listbox.bind("<<ListboxSelect>>", self.load_selected_contact)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Error", "Please fill in both fields.")
            return

        if not phone.isdigit():
            messagebox.showwarning("Invalid Phone Number", "Phone number must contain only digits.")
            return

        if len(phone) < 8:
            messagebox.showwarning(
                "Invalid Phone Number",
                "Phone number must be at least 8 digits long."
            )
            return

        if name in self.contacts:
            if not messagebox.askyesno("Overwrite?", f"{name} already exists. Update contact?"):
                return

        self.contacts[name] = phone
        self.save_data()
        self.refresh_list()
        self.clear_entries()

        messagebox.showinfo("Added", f"Contact '{name}' saved.")

    def delete_contact(self):
        try:
            selected = self.contact_listbox.get(self.contact_listbox.curselection())
            name = selected.split("|")[0].strip()

            if messagebox.askyesno("Confirm Delete", f"Delete contact '{name}'?"):
                del self.contacts[name]
                self.save_data()
                self.refresh_list()
                self.clear_entries()

        except tk.TclError:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def refresh_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name, phone in sorted(self.contacts.items()):
            self.contact_listbox.insert(tk.END, f"{name.ljust(20)} | {phone}")

    def load_selected_contact(self, event):
        try:
            selected = self.contact_listbox.get(self.contact_listbox.curselection())
            name, phone = selected.split("|")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.name_entry.insert(0, name.strip())
            self.phone_entry.insert(0, phone.strip())
        except tk.TclError:
            pass

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
