'''Adam Clemons 5-16-2014
Written for Python 3.4 x86 on Windows 7 Pro x64
This is a TKinter interface for the VirtualPet object class. This UI will interact with the object
'''

__author__ = 'Adam Clemons'

from tkinter import *
from tkinter import ttk

#from virtualPet import *


class PetView:

    def __init__(self, window):
        # TODO: Check that the UI meets the design requirements
        # TODO: document UI with figures
        # Create the Mainframe object and set it up.
        self.mainframe = ttk.Frame(window, padding="3,3,12,12")
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
        ttk.Label(self.mainframe, text="Hunger").grid(column=1, row=1, sticky=(W))
        ttk.Label(self.mainframe, text="Happiness").grid(column = 1, row=2, sticky=(W))
        ttk.Label(self.mainframe, text="Size").grid(column = 1, row=3, sticky=(W))
        ttk.Label(self.mainframe, textvariable=self.petHunger).grid(column=2, row=1, sticky=(W, E))
        ttk.Label(self.mainframe, textvariable=self.petHappiness).grid(column=2, row = 2, sticky=(W, E))
        ttk.Label(self.mainframe, textvariable=self.petSize).grid(column=2, row=3, sticky=(W, E))


