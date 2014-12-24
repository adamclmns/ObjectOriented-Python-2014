'''Adam Clemons 12-22-2014
Written for Python 2.7.9 x86 on Windows 7 Pro x64
This is a TKinter interface for the VirtualPet object class. This UI will interact with the object
'''

__author__ = 'Adam'

from Tkinter import *
from ttk import *
from PIL import Image, ImageTk

'''
Requires Pillow from  http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil for Python 2.7 win32
in order to embed images in Tkinter
'''

#from petClass import *


class uiClass:

    def __init__(self, pet):
        #Assign properties and variables
        self.pet = pet
        self.root = Tk()
        self.root.title("Virtual Python Pet")
        self.root.wm_geometry("440x380")
        #self.root.after(10000, self.timedUpdate)
        
        #Create the Mainframe object and set it up.
        self.mainframe = Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        #Create the variables for the labels.
        self.petHunger = StringVar()
        self.petHappiness = StringVar()
        self.petDirtiness=StringVar()

        #Set variables for the UI
        self.petHunger.set(self.pet.getHunger())
        self.petHappiness.set(self.pet.getHappiness())
        self.petDirtiness.set(self.pet.getDirtiness())

        #Adding the Labels for the left column
        Label(self.mainframe, text="Hunger").grid(column=1, row=1, sticky=(W))
        Label(self.mainframe, text="Happiness").grid(column = 1, row=2, sticky=(W))
        Label(self.mainframe, text="Dirtiness").grid(column=1, row=3, sticky=(W))

        #Interactive Labels with variables that will change for the middle column
        Label(self.mainframe, textvariable=self.petHunger).grid(column=2, row=1, sticky=(W,E))
        Label(self.mainframe, textvariable=self.petHappiness).grid(column=2, row = 2, sticky=(W,E))
        Label(self.mainframe, textvariable=self.petDirtiness).grid(column=2, row=3, sticky=(W,E))

        #Adding buttons for the far right column
        Button(self.mainframe, text="Feed", command=self.feed).grid(column=4, row=1, sticky=(E))
        Button(self.mainframe, text="Play", command=self.play).grid(column=4, row=2, sticky=(E))
        Button(self.mainframe, text="Clean", command=self.clean).grid(column=4, row=3, sticky=(E))

        #adding image variables to put into UI
        self.happyPet = ImageTk.PhotoImage(file=".\\images\\happyPet.png")
        self.sadPet = ImageTk.PhotoImage(file=".\\images\\sadPet.png")
        self.playPet = ImageTk.PhotoImage(file=".\\images\\playPet.png")
        self.feedPet = ImageTk.PhotoImage(file=".\\images\\feedPet.png")

        #Setting a default starting image
        self.icon = Label(image=self.happyPet)
        self.icon.grid(column=0, row=4, columnspan=5, rowspan=5)
        self.icon.image = self.happyPet


    #Functions to interface with PetClass.
    def changeImage(self, photoImage):
        self.icon = Label(image=photoImage)
        self.icon.grid(column=0, row=4, columnspan=5, rowspan=5)
        self.icon.image = photoImage

    def feed(self):
        self.pet.feed()
        self.refreshData()
        self.changeImage(self.feedPet)
        return

    def play(self):
        self.pet.play()
        self.refreshData()
        self.changeImage(self.playPet)
        return

    def clean(self):
        self.pet.clean()
        self.refreshData()

    def timedUpdate(self):
        #Update function for cleanliness, hunger, happiness, and boredom will

        return

    def refreshData(self):
        self.petDirtiness.set(self.pet.getDirtiness())
        self.petHappiness.set(self.pet.getHappiness())
        self.petHunger.set(self.pet.getHunger())
