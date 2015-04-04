from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PenguinView import MyView
from PenguinModel import MyModel

class MyViewController():
    def __init__(self,parent):
        self.parent = parent;

#added instantiation of view 2014 May 26
        self.view = MyView(self)
#(3)added instantiation of model 2014 May 28
        self.model = MyModel(self)

    #Handlers -- target action
    def addPressed(self):
#Change getters and setters for the view
        self.view.setLabelText(self.view.getPenguinType()+ ' Penguin '+ self.view.getPenguinAction() + ' Added')
#(5)added true functionality -- this adds the entry to the model. 2014 May 28
        self.model.addRecordToList(self.view.getPenguinType(),self.view.getPenguinAction())
    def quitPressed(self):
#Change getters and setters for the view
        self.view.setLabelText('Quitting')
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:
            self.parent.destroy()
#(4) added a delegate for the model 2014 May 28
    def modelDidChangeDelegate(self):
        print("Gork!!")
        print(self.model.getList())


