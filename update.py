from tkinter import *
import tkinter.messagebox
import sqlite3

# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Update Appointments")

        # heading label
        self.heading = Label(master, text="Update Appointments", fg='steelblue', font=('Helvetica', 40, 'bold'))
        self.heading.grid(row=0, column=0, columnspan=2, pady=20)

        # search criteria --> name
        self.name_label = Label(master, text="Enter Patient's Name", font=('Helvetica', 18))
        self.name_label.grid(row=1, column=0, padx=20, pady=10, sticky=E)

        # entry for the name
        self.name_entry = Entry(master, width=30, font=('Helvetica', 16))
        self.name_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # search button
        self.search_button = Button(master, text="Search", width=12, height=1, bg='steelblue', fg='white', font=('Helvetica', 14, 'bold'), command=self.search_db)
        self.search_button.grid(row=1, column=2, padx=20, pady=10)

    # function to search
    def search_db(self):
        self.input = self.name_entry.get()
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        
        # clear previous entries if any
        self.clear_entries()

        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]

        # creating the update form
        self.uname_label = Label(self.master, text="Patient's Name", font=('Helvetica', 18))
        self.uname_label.grid(row=2, column=0, padx=20, pady=10, sticky=E)

        self.uage_label = Label(self.master, text="Age", font=('Helvetica', 18))
        self.uage_label.grid(row=3, column=0, padx=20, pady=10, sticky=E)

        self.ugender_label = Label(self.master, text="Gender", font=('Helvetica', 18))
        self.ugender_label.grid(row=4, column=0, padx=20, pady=10, sticky=E)

        self.ulocation_label = Label(self.master, text="Location", font=('Helvetica', 18))
        self.ulocation_label.grid(row=5, column=0, padx=20, pady=10, sticky=E)

        self.utime_label = Label(self.master, text="Appointment Time", font=('Helvetica', 18))
        self.utime_label.grid(row=6, column=0, padx=20, pady=10, sticky=E)

        self.uphone_label = Label(self.master, text="Phone Number", font=('Helvetica', 18))
        self.uphone_label.grid(row=7, column=0, padx=20, pady=10, sticky=E)

        # entries for each label
        self.uname_entry = Entry(self.master, width=30, font=('Helvetica', 16))
        self.uname_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)
        self.uname_entry.insert(END, str(self.name1))

        self.uage_entry = Entry(self.master, width=30, font=('Helvetica', 16))
        self.uage_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)
        self.uage_entry.insert(END, str(self.age))

        self.ugender_entry = Entry(self.master, width=30, font=('Helvetica', 16))
        self.ugender_entry.grid(row=4, column=1, padx=20, pady=10, sticky=W)
        self.ugender_entry.insert(END, str(self.gender))

        self.ulocation_entry = Entry(self.master, width=30, font=('Helvetica', 16))
        self.ulocation_entry.grid(row=5, column=1, padx=20, pady=10, sticky=W)
        self.ulocation_entry.insert(END, str(self.location))

        self.utime_entry = Entry(self.master, width=30, font=('Helvetica', 16))
        self.utime_entry.grid(row=6, column=1, padx=20, pady=10, sticky=W)
        self.utime_entry.insert(END, str(self.time))

        self.uphone_entry = Entry(self.master, width=30, font=('Helvetica', 16))
        self.uphone_entry.grid(row=7, column=1, padx=20, pady=10, sticky=W)
        self.uphone_entry.insert(END, str(self.phone))

        # button to execute update
        self.update_button = Button(self.master, text="Update", width=15, height=2, bg='lightblue', fg='black', font=('Helvetica', 14, 'bold'), command=self.update_db)
        self.update_button.grid(row=8, column=1, pady=20, sticky=W)

        # button to delete
        self.delete_button = Button(self.master, text="Delete", width=15, height=2, bg='red', fg='white', font=('Helvetica', 14, 'bold'), command=self.delete_db)
        self.delete_button.grid(row=8, column=1, pady=20, padx=150, sticky=W)

    def clear_entries(self):
        for widget in self.master.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()

    def update_db(self):
        # declaring the variables to update
        self.var1 = self.uname_entry.get()  # updated name
        self.var2 = self.uage_entry.get()  # updated age
        self.var3 = self.ugender_entry.get()  # updated gender
        self.var4 = self.ulocation_entry.get()  # updated location
        self.var5 = self.uphone_entry.get()  # updated phone
        self.var6 = self.utime_entry.get()  # updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.name_entry.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")

    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.name_entry.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.clear_entries()

# creating the object
root = Tk()
b = Application(root)
root.geometry("800x600")
root.resizable(False, False)
root.mainloop()
