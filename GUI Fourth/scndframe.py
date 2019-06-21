from tkinter import *

class scndframe:
    def __init__(self,win):
        self.win = win
        self.mainframe = Frame(self.win,height=600,width=600,bg="green")
        self.title = Label(self.mainframe,text="Second Frame",font=('chiller',40))
        self.title.place(x=0,y=0)
        self.mainframe.place(x=0,y=0)
