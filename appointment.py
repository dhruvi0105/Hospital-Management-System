from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database.
conn = sqlite3.connect('database.db')
# cursor to move around the database
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightgreen', padx=10, pady=10)
        self.left.pack(side=LEFT, fill=BOTH, expand=True)

        self.right = Frame(master, width=400, height=720, bg='steelblue', padx=10, pady=10)
        self.right.pack(side=RIGHT, fill=BOTH, expand=True)

        # labels for the window
        self.heading = Label(self.left, text="ABC Hospital Appointments", font=('Helvetica', 30, 'bold'), fg='black', bg='lightgreen')
        self.heading.grid(row=0, column=0, columnspan=2, pady=20)

        # patients name
        self.name = Label(self.left, text="Patient's Name", font=('Helvetica', 18), fg='black', bg='lightgreen')
        self.name.grid(row=1, column=0, pady=10, sticky=W)

        # age
        self.age = Label(self.left, text="Age", font=('Helvetica', 18), fg='black', bg='lightgreen')
        self.age.grid(row=2, column=0, pady=10, sticky=W)

        # gender
        self.gender = Label(self.left, text="Gender", font=('Helvetica', 18), fg='black', bg='lightgreen')
        self.gender.grid(row=3, column=0, pady=10, sticky=W)

        # location
        self.location = Label(self.left, text="Location", font=('Helvetica', 18), fg='black', bg='lightgreen')
        self.location.grid(row=4, column=0, pady=10, sticky=W)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('Helvetica', 18), fg='black', bg='lightgreen')
        self.time.grid(row=5, column=0, pady=10, sticky=W)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('Helvetica', 18), fg='black', bg='lightgreen')
        self.phone.grid(row=6, column=0, pady=10, sticky=W)

        # Entries for all labels
        self.name_ent = Entry(self.left, width=30, font=('Helvetica', 16))
        self.name_ent.grid(row=1, column=1, pady=10)

        self.age_ent = Entry(self.left, width=30, font=('Helvetica', 16))
        self.age_ent.grid(row=2, column=1, pady=10)

        self.gender_ent = Entry(self.left, width=30, font=('Helvetica', 16))
        self.gender_ent.grid(row=3, column=1, pady=10)

        self.location_ent = Entry(self.left, width=30, font=('Helvetica', 16))
        self.location_ent.grid(row=4, column=1, pady=10)

        self.time_ent = Entry(self.left, width=30, font=('Helvetica', 16))
        self.time_ent.grid(row=5, column=1, pady=10)

        self.phone_ent = Entry(self.left, width=30, font=('Helvetica', 16))
        self.phone_ent.grid(row=6, column=1, pady=10)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', fg='white', font=('Helvetica', 16), command=self.add_appointment)
        self.submit.grid(row=7, column=1, pady=20)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[-1] if self.new else 0

        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('Helvetica', 28, 'bold'), fg='white', bg='steelblue')
        self.logs.pack(anchor=N, pady=20)

        self.box = Text(self.right, width=50, height=30, font=('Helvetica', 14))
        self.box.pack(pady=20)
        self.update_logs()

    # function to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created")

            # get the last inserted ID
            self.final_id = c.lastrowid

            # update the logs
            self.update_logs()

    def update_logs(self):
        self.box.delete(1.0, END)
        self.box.insert(END, "Total Appointments till now: " + str(self.final_id))

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
