'''Adam Clemons 5-16-2014
Written for Python 3.4 x86 on Windows 7 Pro x64
This is a TKinter interface for the VirtualPet object class. This UI will interact with the object
'''

__author__ = 'Adam Clemons'
import Tkinter as tk


class PetView(tk.Frame):

    def __init__(self, vc):
        # TODO: put the root in main program when finished.
        # TODO: Check that the UI meets the design requirements
        # Create the Mainframe object and set it up.
        self.mainframe = tk.Frame()
        self.mainframe.grid(column=0, row=0)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # This is for talking to the Controller
        self.vc = vc

        # Create the variables for the labels.
        self.petHunger = tk.StringVar()
        self.petHappiness = tk.StringVar()
        self.petCleanliness = tk.StringVar()

        #Set starting values of the labels
        self.petHappiness.set(str(14))
        self.petHunger.set(str(14))
        self.petCleanliness.set(str(14))

    #
    # THIS IS WHERE THE VIEW IS SETUP AND STYLED You COULD make this a different function
    # TODO: Make View setup a new function loadElements()
    #
        # Adding the Labels
        tk.Label(self.mainframe, text="Hunger ").grid(column=2, row=4)
        tk.Label(self.mainframe, text="Happiness ").grid(column=2, row=5)
        tk.Label(self.mainframe, text="Size ").grid(column=2, row=6)
        tk.Label(self.mainframe, textvariable=self.petHunger).grid(column=3, row=4)
        tk.Label(self.mainframe, textvariable=self.petHappiness).grid(column=3, row=5)
        tk.Label(self.mainframe, textvariable=self.petCleanliness).grid(column=3, row=6)
        # Adding a picture Label

        # Adding buttons
        # TODO: Add Actions to the Buttons
        # TODO: Use Lambdas instead of wrapper functions
        # tk.Button(self.mainframe, text="Feed", name="feed").grid(column=5, row=4)
        # tk.Button(self.mainframe, text="Play", name="play").grid(column=5, row=5)
        # tk.Button(self.mainframe, text="Clean", name="clean").grid(column=5, row=6)

        tk.Button(self.mainframe, text="Feed", name="feed", command=self.vc.feedPressed).grid(column=5, row=4)
        tk.Button(self.mainframe, text="Play", name="play", command=self.vc.playPressed).grid(column=5, row=5)
        tk.Button(self.mainframe, text="Clean", name="clean", command=self.vc.cleanPressed).grid(column=5, row=6)

    # TODO: Create Action Setting functions here for passing to the Controller
    def setHappiness(self, value):
        self.petHappiness.set(value)

    def setHunger(self, value):
        self.petHunger.set(value)

    def setCleanliness(self, value):
        self.petCleanliness.set(value)




