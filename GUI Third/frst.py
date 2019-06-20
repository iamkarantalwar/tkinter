from tkinter import *

class Main:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('600x600')
        #we draw a frame with the same height of the window
        self.main_frame = Frame(self.win,height=600,width=600,bg="red")
        #these widgets are considered under the main frame so we give the first parameter of the frame variable
        self.title = Label(self.main_frame,text="Hello world",font=('chiller',50),bg="red")
        self.title.place(x=0,y=0)
        self.ent = Entry(self.main_frame,show="#")
        self.ent.place(x=0,y=70)
        
        #command is used to call the function with the click of button
        self.btn = Button(self.main_frame,text="Switch me",command=self.ClickMe)
        self.btn.place(x=0,y=100)
        self.main_frame.place(x=0,y=0)
        self.win.mainloop()

    def ClickMe(self):
        #this function is invoked after the click of the click me buttonm
        print("Hello world")
        #the below piece of code will destroy this window
        self.win.destroy()
        #the below piece of code will execute the code inside the scnd.py
        import scnd

d = Main()
