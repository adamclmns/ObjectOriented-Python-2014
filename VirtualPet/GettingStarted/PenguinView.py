from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class MyView(Frame):
#Change parent to callback and add a frame 2014 May 26 a
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row=0,column=0)
        self.vc = vc
 
        #properties of the view
        self.labelText = StringVar()
        self.labelText.set("Popper's Penguins Ready")
        self.penguinType = StringVar()
        self.penguinType.set('Penguin Type')
        self.penguinAction = StringVar()
        self.penguinAction.set('Penguin Action')
#remove self.callback here as callback calls this, not the othere way around.   2014 May 26
#       self.callback = MyViewController(self)
        self.loadView()
        self.makeStyle()
 
#Handlers -- our pseudo-controller
#(3)removed from application 2014-May-26
 
#added setters and getters for the properties 2014-May 26
    def setLabelText(self,newText):
        self.labelText.set(newText)
    def getLabelText(self):
        return self.labelText.get()
    def setPenguinType(self,newType):
        self.penguinType.set(newType)
    def getPenguinType(self):
        return self.penguinType.get()
    def setPenguinAction(self,newAction):
        self.penguinAction.set(newAction)
    def getPenguinAction(self):
        return self.penguinAction.get()
 
#Style Sheet
    def makeStyle(self):
        self.s = ttk.Style()
        self.s.configure('TFrame',background = '#5555ff')
        self.s.configure('TButton',background = 'blue', foreground = '#eeeeff', font = ('Sans','14','bold'), sticky = EW)
        self.s.configure('TLabel',font=('Sans','16','bold'),background = '#5555ff', foreground = '#eeeeff')
        self.s.map('TButton', foreground = [('hover','#5555ff'), ('focus', 'yellow')])
        self.s.map('TButton', background = [('hover', '#eeeeff'),('focus','orange')])
        self.s.configure('TCombobox',background = '#5555ff',foreground ='#3333ff',font = ('Sans',18))
 
#loading the view
#changed the command= to refer to the view controller 2014-May-26
    # self.addPressed now is self.callback.addPressed
    # self.quitPressed now is self.callback.quitPressed
    def loadView(self):
        #label
        status_label = ttk.Label(self.frame, textvariable = self.labelText)
        #status_label.configure(font=('Sans','16','bold'),background = 'blue', foreground = '#eeeeff')
        status_label.grid(row=0,column=0,columnspan=4,sticky=EW)
 
        add_button = ttk.Button(self.frame,command= self.vc.addPressed,text = 'Add')
        add_button.grid(row = 2, column = 0)
        quit_button = ttk.Button(self.frame, command = self.vc.quitPressed, text = 'Quit')
        quit_button.grid(row = 2, column = 3)
 
        penguinType_values = ['Adele','Emperor','King','Blackfoot','Humboldt','Galapagos','Macaroni','Tux','Oswald Cobblepot','Flippy Slippy']
        penguinType_combobox = ttk.Combobox(values = penguinType_values, textvariable = self.penguinType)
        penguinType_combobox.grid(row =1, column = 0)
 
        penguinAction_values = ['Happy','Sad','Angry','Standing','Swimming','Eating','Sleeping','On Belly','Plotting Evil','Singing','Dancing','Being Cute']
        penguinAction_combobox = ttk.Combobox(values = penguinAction_values, textvariable = self.penguinAction)
        penguinAction_combobox.grid(row=1, column = 3)
 