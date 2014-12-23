'''Adam Clemons 12-22-2014
Written for Python 2.7.9 x86 on Windows 7 Pro x64
This is a TKinter interface for the VirtualPet object class. This UI will interact with the object
'''

__author__ = 'Adam'

from Tkinter import *
from ttk import *


#from petClass import *


class uiClass:

    def __init__(self, pet):
        #Assign properties and variables
        self.pet = pet
        self.root = Tk()
        self.root.title("Virtual Python Pet")
        #self.root.after(10000, self.timedUpdate)
        
        #Create the Mainframe object and set it up.
        self.mainframe = Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        #Create the variables for the labels.
        self.petHunger = StringVar()
        self.petHappiness = StringVar()
        self.petSize=StringVar()
        #self.petCleanliness=StringVar()

        #Set variables for the UI
        self.petHunger.set(self.pet.getHunger())
        self.petHappiness.set(self.pet.getHappiness())
        self.petSize.set(self.pet.getSize())

        #Adding the Labels
        Label(self.mainframe, text="Hunger").grid(column=1, row=1, sticky=(W))
        Label(self.mainframe, text="Happiness").grid(column = 1, row=2, sticky=(W))
        Label(self.mainframe, text="Size").grid(column = 1, row=3, sticky=(W))
        Label(self.mainframe, textvariable=self.petHunger).grid(column=2, row=1, sticky=(W,E))
        Label(self.mainframe, textvariable=self.petHappiness).grid(column=2, row = 2, sticky=(W,E))
        Label(self.mainframe, textvariable=self.petSize).grid(column=2, row=3, sticky=(W,E))

        #Adding buttons
        Button(self.mainframe, text="Feed", command=self.feed).grid(column=2, row=4, sticky=(W, E))
        Button(self.mainframe, text="Play", command=self.play).grid(column=2, row=5, sticky=(W,E))

    #Functions to interface with PetClass.
    def feed(self):
        self.pet.feed()
        self.petHunger.set(self.pet.getHunger())
        return

    def play(self):
        self.pet.play()
        self.petHappiness.set(self.pet.getHappiness())
        self.petHunger.set(self.pet.getHunger())
        return

    def timedUpdate(self):
        #Update function for cleanliness, hunger, happiness, and boredom will

        return