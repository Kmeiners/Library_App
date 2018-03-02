#====================
#   Imports
#====================
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg

# Create Instance
win = tk.Tk()
win.title("Administrator GUI 2")
tabControl = ttk.Notebook(win)
viewTab = ttk.Frame(tabControl)
tabControl.add(viewTab, text="View")
newTab = ttk.Frame(tabControl)
tabControl.add(newTab, text="New")

tabControl.pack(expand=1, fill="both")

# Functions
def search():
    searchBox.delete(0, tk.END)
    searchBox.insert(0, user.get() + "   " + time.get() + "   " + room.get())

def createEntry():
    tabControl.select(newTab)

def editEntry():
    return 0

def deleteEntry():
    answer = msg.askyesno("Warning", "Are you sure you want to delete this entry?")
    if answer == True:
        searchBox.delete(0, tk.END)

def clearNewEntry():
    newUserField.delete(0,END)
    newTimeChosen.current(0)
    newRoomChosen.current(0)
        
#====================
#   Search Tab
#====================

# Frame Creation
Frame1 = ttk.LabelFrame(viewTab, text="Search For Reservations")
Frame1.grid(column=0, row=0, padx=30, pady=(30,0))

Frame2 = ttk.LabelFrame(viewTab)
Frame2.grid(column=0, row=1, padx=30, pady=(0,30))

# Labels
emailLabel = ttk.Label(Frame1, text="E-mail Address:")
emailLabel.grid(column=0, row=0, padx=(20,10), pady=10)

timeLabel = ttk.Label(Frame1, text="Time:")
timeLabel.grid(column=1, row=0, padx=(10,10), pady=10)

roomLabel = ttk.Label(Frame1, text="Room:")
roomLabel.grid(column=2, row=0, padx=(10,20), pady=10)

# Text Boxes
user = tk.StringVar()
user_field = ttk.Entry(Frame1, width=20, textvariable=user)
user_field.grid(column=0, row=1, padx=(20,10), pady=10)

# ListBox

searchBox = Listbox(Frame1, width= 50, height= 10)
searchBox.grid(column= 0, columnspan= 5, padx= 20, pady = 20)

# Drop-Down List
time = tk.StringVar()
time_chosen = ttk.Combobox(Frame1, width=15, textvariable= time, state="readonly")
time_chosen["values"] = ("", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM")
time_chosen.grid(column=1,row=1, padx=(10,10), pady=10)
time_chosen.current(0)

room = tk.StringVar()
room_chosen = ttk.Combobox(Frame1, width=15, textvariable= room, state="readonly")
room_chosen["values"] = ("", "POTOMAC", "SHENANDOAH", "CATOCTIN", "SOUTH MOUNTAIN")
room_chosen.grid(column=2,row=1, padx=(10,10), pady=10)
room_chosen.current(0)


# Buttons
login_button = ttk.Button(Frame1, text="Search", command= search)
login_button.grid(column=4, row=1, padx=(10,20))

new_button = ttk.Button(Frame2, text="New", command= createEntry)
new_button.grid(column=0, row=0, padx=5, pady=5)

manage_button = ttk.Button(Frame2, text= "Edit", command= editEntry)
manage_button.grid(column=1, row=0, padx=5, pady=5)

delete_button = ttk.Button(Frame2, text= "Delete", command= deleteEntry)
delete_button.grid(column=2, row=0, padx=5, pady=5)

#====================
#   Create Tab
#====================

# Frame Creation
newFrame = ttk.LabelFrame(newTab, text="Create a New Reservation")
newFrame.grid(column=0, row=0, padx=30, pady=(30,0))

# Labels
newEmailLabel = ttk.Label(newFrame, text="E-mail Address:")
newEmailLabel.grid(column=0, row=0, padx=(50,5), pady=(30,10), sticky=E)

newTimeLabel = ttk.Label(newFrame, text="Time:")
newTimeLabel.grid(column=0, row=1, padx=(50,5), pady=10, sticky=E)

newRoomLabel = ttk.Label(newFrame, text="Room:")
newRoomLabel.grid(column=0, row=2, padx=(50,5), pady=10, sticky=E)

# Text Boxes
newUser = tk.StringVar()
newUserField = ttk.Entry(newFrame, width=20, textvariable=newUser)
newUserField.grid(column=1, row=0, padx=(5,50), pady=(30,10), sticky=W)

# Drop-Down List
newTime = tk.StringVar()
newTimeChosen = ttk.Combobox(newFrame, width=17, textvariable= newTime, state="readonly")
newTimeChosen["values"] = ("", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM")
newTimeChosen.grid(column=1,row=1, padx=(5,50), pady=10, sticky=W)
time_chosen.current(0)

newRoom = tk.StringVar()
newRoomChosen = ttk.Combobox(newFrame, width=17, textvariable= newRoom, state="readonly")
newRoomChosen["values"] = ("", "POTOMAC", "SHENANDOAH", "CATOCTIN", "SOUTH MOUNTAIN")
newRoomChosen.grid(column=1,row=2, padx=(5,50), pady=10, sticky=W)
newRoomChosen.current(0)

# Buttons
newClearButton = ttk.Button(newFrame, text= "Clear", command= clearNewEntry)
newClearButton.grid(column=1, row=3)

#====================
#   Menu Bar
#====================

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Create Menu and Add Menu Items
file_menu = Menu(menu_bar, tearoff=0)   # File Menu
file_menu.add_command(label="New")
file_menu.add_command(label="Manage")
file_menu.add_command(label="Search")
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

# Focus
user_field.focus()

#====================
#   Start GUI
#====================
win.mainloop()
