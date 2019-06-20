from tkinter import *
#this is the python class
class Main:
    def __init__(self):
        #self is come along with every variable because we are working in classes and objects
        self.d = Tk()
        #geometry method will resize your image according the given parameters (height x width)
        self.d.geometry('600x600')
        #title is used to give  the title to the window
        self.d.title("First Application")        
        self.d.mainloop()

d = Main()
