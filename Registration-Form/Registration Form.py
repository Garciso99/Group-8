import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if name and email and password:
        messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x250")

# Labels and Entry Fields
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

# Run the application
root.mainloop()
