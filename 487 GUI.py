#====================
#   Imports
#====================
import tkinter as tk
from tkinter import ttk

# Create Instance
win = tk.Tk()

# Title Field
win.title("Administrator GUI")

# Functions
def login():
    if user.get() == "admin" and password.get() == "admin":
        login_button.configure(text="Successful Login")
    else:
        incorrectLabel.grid(column=0,row=1)
    
# Frame Creation
Frame1 = ttk.LabelFrame(win, text="Administrator Login")
Frame1.grid(column=0, row=0, padx=30, pady=30)

# Labels
adminLabel = ttk.Label(Frame1, text="Admin User: ")
adminLabel.grid(column=0, row=0, padx=20, pady=(20,10))

passwordLabel = ttk.Label(Frame1, text="Password: ")
passwordLabel.grid(column=0, row=1, pady=(0,10))

incorrectLabel = ttk.Label(win, text="Incorrect Password")

# Text Boxes
user = tk.StringVar()
user_field = ttk.Entry(Frame1, width=15, textvariable=user)
user_field.grid(column=1, row=0, padx=(0,20), pady=(20,10))

password = tk.StringVar()
password_field = ttk.Entry(Frame1, width=15, textvariable=password)
password_field.grid(column=1, row=1, padx=(0,20), pady=(0,10))

# Buttons
login_button = ttk.Button(win, text="Login", command=login)
login_button.grid(column=0, row=2, pady=(0,20))

# Focus
user_field.focus()

#====================
#   Start GUI
#====================
win.mainloop()
