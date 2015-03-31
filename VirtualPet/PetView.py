'''Adam Clemons 5-16-2014
Written for Python 3.4 x86 on Windows 7 Pro x64
This is a TKinter interface for the VirtualPet object class. This UI will interact with the object
'''

__author__ = 'Adam Clemons'

from tkinter import *
from tkinter import tk

#from virtualPet import *


class PetView:

    def __init__(self, model):
        # Assign properties and variables
        self.viewModel = model
        self.frame = Tk.frame(master)
        self.frame.title("Virtual Python Pet")
        # self.root.after(10000, self.timedUpdate)
        
        # Create the Mainframe object and set it up.
        self.mainframe = tk.Frame(self.frame, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # Create the variables for the labels.
        self.petHunger = StringVar()
        self.petHappiness = StringVar()
        self.petCleanliness = StringVar()

        # Set variables for the UI
        self.petHunger.set(self.viewModel.getHunger())
        self.petHappiness.set(self.viewModel.getHappiness())

        # Adding the Labels
        tk.Label(self.mainframe, text="Hunger").grid(column=1, row=1, sticky=(W))
        tk.Label(self.mainframe, text="Happiness").grid(column = 1, row=2, sticky=(W))
        tk.Label(self.mainframe, text="Size").grid(column = 1, row=3, sticky=(W))
        tk.Label(self.mainframe, textvariable=self.petHunger).grid(column=2, row=1, sticky=(W,E))
        tk.Label(self.mainframe, textvariable=self.petHappiness).grid(column=2, row = 2, sticky=(W,E))
        tk.Label(self.mainframe, textvariable=self.petSize).grid(column=2, row=3, sticky=(W,E))

        # Adding buttons
        tk.Button(self.mainframe, text="Feed", command=self.feed).grid(column=2, row=4, sticky=(W, E))
        tk.Button(self.mainframe, text="Play", command=self.play).grid(column=2, row=5, sticky=(W,E))

    # Functions to interface with PetClass.
    def feed(self):
        self.viewModel.feed()
        self.petHunger.set(self.viewModel.getHunger()+3)
        return

    def play(self):
        self.viewModel.play()
        self.petHappiness.set(self.viewModel.getHappiness()+3)
        self.petHunger.set(self.viewModel.getHunger()+3)
        return

    def clean(self):
        self.viewModel.clean()
        self.petHappiness.set(self.viewModel.getHappiness())

    def timedUpdate(self):
        # Update function for cleanliness, hunger, happiness, and boredom will

        return