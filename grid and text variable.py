from tkinter import *

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.geometry('300x300')
        self.mainframe = Frame(self.tk,height=300,width=300,)

        self.gridframe = Frame(self.mainframe,height=100,width=100)

        self.l1 = StringVar(self.gridframe)
        self.l2 = StringVar(self.gridframe)
        self.l3 = StringVar(self.gridframe)
        self.l4 = StringVar(self.gridframe)
        self.label = Label(self.gridframe,text="Label1",)
        self.label.grid(row=0,column=0)
        self.label = Label(self.gridframe,text="Label2",)
        self.label.grid(row=1,column=0)
        self.label = Label(self.gridframe,text="Label3",)
        self.label.grid(row=2,column=0)
        self.label = Label(self.gridframe,text="Label4",)
        self.label.grid(row=3,column=0)

        self.entry = Entry(self.gridframe,text="Entry1",textvariable = self.l1)
        self.entry.grid(row=0,column=1)
        self.entry = Entry(self.gridframe,text="Entry2",textvariable = self.l2)
        self.entry.grid(row=1,column=1)
        self.entry = Entry(self.gridframe,text="Entry3",textvariable = self.l3)
        self.entry.grid(row=2,column=1)
        self.entry = Entry(self.gridframe,text="Entry4",textvariable = self.l4)
        self.entry.grid(row=3,column=1)

        self.btn = Button(self.gridframe,text="Click Me",command = self.hello)
        self.btn.grid(row=4,column=1)


        self.gridframe.place(x=80,y=80)
        self.mainframe.place(x=0,y=0)
        self.tk.mainloop()
    def hello(self):
        print(self.l1.get(),self.l2.get(),self.l3.get(),self.l4.get())

        

d = Main()
