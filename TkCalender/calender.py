#pip install tkcalendar

#to import calender from a library
from tkcalendar import DateEntry, Calendar
from tkinter import *
class Main:
    def __init__(self):

        self.tk = Tk()

        #it is used to pick the date from the claender
        self.dob = DateEntry(self.tk,font=('Comic Sans MS',13), bg='darkblue',
                    fg='white', borderwidth=2)
        self.dob.place(x=0,y=0)
        self.dob.config(width=31)

        self.tk.mainloop()


d = Main()
