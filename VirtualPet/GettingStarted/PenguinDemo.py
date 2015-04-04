# poppers_penguins_MVC_02
#MVC Version 2014 May 28
#Change: Implements the Model according to the MVC template
 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PenguinController import MyViewController


def main():
    root = Tk()
#(8) Set up the main loop 2014 May 26
    frame = Frame(root, background="#5555ff", takefocus = 0)
    root.title("Popper's Penguins")
    app = MyViewController(root)
    root.mainloop()

if __name__ == '__main__':
    main()