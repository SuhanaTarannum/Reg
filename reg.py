import tkinter as tk
from tkinter import messagebox

def submit_form():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if not username or not email or not password:
        messagebox.showwarning("Input Error", "All fields are required")
        return
    
    # Here you can add code to save data to a file or database
    # For simplicity, we'll just display it in a message box
    messagebox.showinfo("Registration Successful", f"Username: {username}\nEmail: {email}")
    
    # Clear the form
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entries for the form
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()
