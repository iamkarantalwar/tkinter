from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import getdata
class Window:
    def __init__(self):

        self.tk = Tk()
        self.tk.geometry('500x500')
        fetch= (getdata.fetch())
        self.tree = Treeview(self.tk,columns=("#1","#2","#3","#4"))
        self.tree.heading("#0",text="user id")
        self.tree.column("#0",width=60)
        self.tree.heading("#1",text="User Name")
        self.tree.heading("#2",text="Password")
        self.tree.heading("#3",text="Update")
        self.tree.heading("#4",text="Delete")
        
        for i in fetch:
            self.tree.insert('','end',text=i[0],values=(i[1],i[2],"Update","Delete"))
        self.tree.place(x=0,y=0)

        self.tree.bind("<Double-Button-1>",self.trigger)








        

        #self.tree.bind("<Double-Button-1>",self.popupdata)

        #self.tk.bind("<Control-o>",self.trigger)

        self.tk.mainloop()

    def popupdata(self,e):
        print(e)
        d = self.tree.focus()
        print(self.tree.item(d))
        
        

    def trigger(self,e):
        #e will identify from where the function has been triggered
        print(e)
        #d will store the object of focused element in the treeview
        d = self.tree.focus()
        #x will identify the item
        x = (self.tree.item(d))
        #col will identify the focused column
        col = self.tree.identify_column(e.x)
        if col=="#3":
            print("Update")
        elif col == "#4":
            print("delete")
        
        
        

        



d = Window()

