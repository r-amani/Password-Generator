import tkinter as tk
from tkinter import messagebox
import random
import string



def generate_password():
    length = length_slider.get()

    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    password = "".join(random.choice(chars) for _ in range(length))

    entry.delete(0, tk.END)
    entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")



root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#1e1e1e")


tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)


entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10, padx=20, fill="x")


length_slider = tk.Scale(root, from_=6, to=32, orient="horizontal", label="Password Length", bg="#1e1e1e", fg="white")
length_slider.set(12)
length_slider.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper,bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower, bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)

tk.Checkbutton(root, text="Numbers (0-9)", variable=var_digits, bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)

tk.Checkbutton(root, text="Symbols (!@#)", variable=var_symbols, bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)


tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

tk.Button(root, text="Copy", command=copy_password, bg="#2196F3", fg="white").pack(pady=5)

root.mainloop()