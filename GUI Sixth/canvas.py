#tkinter program to make screen a the center of window
from tkinter import *

class Main:
    def __init__(self):
        self.tk = Tk()
        #these are the window height and width
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        #we find out the center co ordinates
        y = (height - 600)//2
        x = (width - 600)//2
        #place the window at the center co ordinate
        self.tk.geometry('600x600+'+str(x)+'+'+str(y)+'')

        #these lines of code are for placing picture as background
        self.can = Canvas(self.tk,height=600,width=600,bg="red")
        self.can.pack()
        self.img = PhotoImage(file='./images/obama.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
       
        self.fr = Frame(self.tk,height=200,width=200)
        #we make resizable false to restrict user from resizing the window
        self.fr.place(x=200,y=200)
        self.tk.resizable(height=False,width=False)
        self.tk.mainloop()
        
   
d = Main()







