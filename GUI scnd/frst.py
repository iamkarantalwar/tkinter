from tkinter import *
class Main:
    def __init__(self):
        #main root window
        self.root = Tk()
        #to make title of window
        self.root.title("Second Day")
        #write text by taking it into a variable
        self.title = Label(self.root,text="Welcome")
        #placing the text in the window according to the x axis and y axis
        self.title.place(x=20,y=60)
        #to make window in loop
        self.root.mainloop()

#to make object of the class
d = Main()
    
