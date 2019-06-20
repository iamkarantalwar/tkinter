from tkinter import *
class Main:
    def __init__(self):
        #main root window
        self.root = Tk()
        
        #to make title of window
        self.root.title("Second Day")
        
        #write text by taking it into a variable
        #fg is use to change the text color
        #font is used to incease and decrease the size of the label
        #bg is used to change the background of the label
        self.title = Label(self.root,text="Welcome",fg="red",font=('',20),bg="blue")

        #placing the text in the window
        self.title.place(x=20,y=60)
        
        #to make window in loop
        self.root.mainloop()

#to make object of the class
d = Main()
    
