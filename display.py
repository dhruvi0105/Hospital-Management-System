from tkinter import *
import sqlite3
import pyttsx3

# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        
        # heading
        self.heading = Label(master, text="Appointments", font=('Helvetica', 50, 'bold'), fg='green')
        self.heading.pack(pady=20)

        # button to change patients
        self.change = Button(master, text="Next Patient", width=20, height=2, bg='steelblue', fg='white', font=('Helvetica', 14, 'bold'), command=self.func)
        self.change.pack(pady=20)

        # empty text labels to later config
        self.n = Label(master, text="", font=('Helvetica', 150, 'bold'))
        self.n.pack(pady=20)

        self.pname = Label(master, text="", font=('Helvetica', 50, 'bold'))
        self.pname.pack(pady=20)
        
    # function to speak the text and update the text
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1

# Creating the main window
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)

# Starting the main loop
root.mainloop()
