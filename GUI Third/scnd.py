from tkinter import *

class Main:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('600x600')
        self.main_frame = Frame(self.win,height=600,width=600,bg="green")
        self.title = Label(self.main_frame,text="Hello world",font=('chiller',50),bg="green")
        self.title.place(x=0,y=0)
        self.ent = Entry(self.main_frame,show="#")
        self.ent.place(x=0,y=70)
        self.main_frame.place(x=0,y=0)
        self.win.mainloop()

d = Main()
