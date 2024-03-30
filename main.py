from tkinter import *

class Aplicacao:
    def __init__(self, master=None):
        self.menu = Frame(master)
        self.menu.pack()
        self.msg = Label(self.menu, text = "Menu")
        self.msg.pack()
        self.incio = Button(self.menu)
        
    
        pass

root = Tk()
Aplicacao(root)
root.mainloop()