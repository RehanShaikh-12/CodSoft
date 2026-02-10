import tkinter as tk
from tkinter import messagebox
import secrets
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x480")
        self.root.resizable(False, False)

        
        self.length_var = tk.IntVar(value=12)
        self.use_lower = tk.BooleanVar(value=True) 
        self.use_upper = tk.BooleanVar(value=False)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=False)

        tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=15)

        tk.Label(root, text="Password Length:").pack()
        tk.Scale(root, from_=8, to_=20, orient="horizontal", variable=self.length_var).pack(pady=5)

        tk.Checkbutton(root, text="Lowercase (a-z)", variable=self.use_lower).pack(anchor="w", padx=80)
        tk.Checkbutton(root, text="Uppercase (A-Z)", variable=self.use_upper).pack(anchor="w", padx=80)
        tk.Checkbutton(root, text="Numbers (0-9)", variable=self.use_digits).pack(anchor="w", padx=80)
        tk.Checkbutton(root, text="Symbols (@#$%?)", variable=self.use_special).pack(anchor="w", padx=80)

        self.result_entry = tk.Entry(root, font=("Courier", 14), width=25, justify="center")
        self.result_entry.pack(pady=20)

        tk.Button(root, text="Generate Password", command=self.generate, 
                  bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=5)

        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clip, 
                  bg="#3498db", fg="white", font=("Arial", 10), width=20).pack(pady=5)

    def generate(self):
        """Builds a character pool based STRICTLY on user selection."""
        pool = ""
        
        if self.use_lower.get(): 
            pool += string.ascii_lowercase
        if self.use_upper.get(): 
            pool += string.ascii_uppercase
        if self.use_digits.get(): 
            pool += string.digits
        if self.use_special.get(): 
            pool += string.punctuation

        if not pool:
            messagebox.showwarning("Selection Error", "Please select at least one character type!")
            return

        length = self.length_var.get()

        password = "".join(secrets.choice(pool) for _ in range(length))
        
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

    def copy_to_clip(self):
        password = self.result_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Copied to clipboard!")

if __name__ == "__main__":
    window = tk.Tk()
    app = PasswordGenerator(window)
    window.mainloop()