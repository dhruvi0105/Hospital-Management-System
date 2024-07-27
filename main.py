import tkinter as tk
from tkinter import ttk
import subprocess

# Function to open the appointment script
def new_appointment():
    subprocess.Popen(['python', 'appointment.py'])

# Function to open the display script
def display_appointment():
    subprocess.Popen(['python', 'display.py'])

# Function to open the update script
def update_appointment():
    subprocess.Popen(['python', 'update.py'])

# Create the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry('400x300')

# Create a style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)

# Create the title label
title_label = tk.Label(root, text="Hospital Management System", font=('Helvetica', 16, 'bold'))
title_label.pack(pady=20)

# Create the buttons and assign functions
new_appointment_button = ttk.Button(root, text="New Appointment", command=new_appointment)
display_appointment_button = ttk.Button(root, text="Display Appointments", command=display_appointment)
update_appointment_button = ttk.Button(root, text="Update Appointment", command=update_appointment)

# Place the buttons on the window
new_appointment_button.pack(pady=10)
display_appointment_button.pack(pady=10)
update_appointment_button.pack(pady=10)

# Run the main loop
root.mainloop()
