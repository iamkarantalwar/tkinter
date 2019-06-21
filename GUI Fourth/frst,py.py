from tkinter import *
import scndframe
class Main:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('600x600')
        #this is used to initialize the Menu
        self.menu = Menu(self.win)
        #these are used to make menus in the window
        self.menu.add_cascade(label="File",command=self.change)
        self.menu.add_cascade(label="Edit")
        #to make a main frame
        self.main_frame = Frame(self.win,height=600,width=600,bg="red")
        self.title = Label(self.main_frame,text="First Frame",font=('chiller',40))
        self.title.place(x=0,y=0)
        self.main_frame.place(x=0,y=0)
        #this is used to configure the menu inside the window        
        self.win.config(menu=self.menu)
        self.win.mainloop()

    def change(self):
        self.main_frame.destroy()
        x = scndframe.scndframe(self.win)
        

d = Main()
