'''Adam Clemons 5-16-2014
Written for Python 3.4 x86 on Windows 7 Pro x64
This is a TKinter interface for the VirtualPet object class. This UI will interact with the object
'''

__author__ = 'Adam Clemons'
import tkinter as tk
import os



class PetView(tk.Frame):

    def __init__(self, CallbackController):
        # TODO: put the root in main program when finished.
        # TODO: Check that the UI meets the design requirements
        # Create the Mainframe object and set it up.
        self.mainframe = tk.Frame()
        self.mainframe.grid(column=0, row=0)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        # This is for talking to the Controller
        self.ControllerCallback = CallbackController
        # Create the variables for the labels.
        self.petHunger = tk.StringVar()
        self.petHappiness = tk.StringVar()
        self.petCleanliness = tk.StringVar()
        #Set starting values of the labels
        self.petHappiness.set(str(14))
        self.petHunger.set(str(14))
        self.petCleanliness.set(str(14))
        # Adding values to track how long the picture has been changed
        self.timeSincePictureChange = 0
        self.pictureChanged = False
    #
    # THIS IS WHERE THE VIEW IS SETUP AND STYLED You COULD make this a different function
    # TODO: Make View setup a new function loadElements()
    #
        # Adding the Labels
        tk.Label(self.mainframe, text="Hunger ").grid(column=2, row=5)
        tk.Label(self.mainframe, text="Happiness ").grid(column=2, row=6)
        tk.Label(self.mainframe, text="Size ").grid(column=2, row=7)
        tk.Label(self.mainframe, textvariable=self.petHunger).grid(column=3, row=5)
        tk.Label(self.mainframe, textvariable=self.petHappiness).grid(column=3, row=6)
        tk.Label(self.mainframe, textvariable=self.petCleanliness).grid(column=3, row=7)
        # Adding a picture Label
        # TODO: Demonstrate the Python Console
        # print(os.getcwd())
        path=os.getcwd()
        self.RestBadger = tk.PhotoImage(file=path+"\Images\RestingBadger-small.png")
        self.PlayBadger = tk.PhotoImage(file=path+"\Images\PlayBadger-small.png")
        self.EatBadger = tk.PhotoImage(file=path+"\Images\EatBadger-small.png")
        self.CleanBadger = tk.PhotoImage(file=path+"\Images\CleanBadger-small.png")
        # Setting up the picture for changing.
        # TODO: Explain why this is different
        self.petPicture = tk.Label(self.mainframe, image=self.RestBadger)
        self.petPicture.grid(column=1, row=1, columnspan=6, rowspan=4)
        # Adding a placeholder label to put some empty space at the bottom of the window
        tk.Label(self.mainframe, text=' ').grid(column=3, row=8)
         # Adding buttons
        # TODO: Demonstrate how to use Lambdas instead of wrapper functions
        # tk.Button(self.mainframe, text="Feed", name="feed").grid(column=5, row=4)
        # tk.Button(self.mainframe, text="Play", name="play").grid(column=5, row=5)
        # tk.Button(self.mainframe, text="Clean", name="clean").grid(column=5, row=6)
        tk.Button(self.mainframe, text="Feed", name="feed", command=self.ControllerCallback.feedPressed).grid(column=5, row=5)
        tk.Button(self.mainframe, text="Play", name="play", command=self.ControllerCallback.playPressed).grid(column=5, row=6)
        tk.Button(self.mainframe, text="Clean", name="clean", command=self.ControllerCallback.cleanPressed).grid(column=5, row=7)
        tk.Button(self.mainframe, text="Quit")

    def setHappiness(self, value):
        self.petHappiness.set(value)

    def setHunger(self, value):
        self.petHunger.set(value)

    def setCleanliness(self, value):
        self.petCleanliness.set(value)

    # Create functions
    def ResetImage(self):
        self.timeSincePictureChange = 0
        self.pictureChanged=False
        self.petPicture.configure(image=self.RestBadger)

    def Feed(self):
        self.timeSincePictureChange = 0
        self.pictureChanged=True
        self.petPicture.configure(image=self.EatBadger)

    def Clean(self):
        self.timeSincePictureChange = 0
        self.pictureChanged=True
        self.petPicture.configure(image=self.CleanBadger)

    def Play(self):
        self.timeSincePictureChange = 0
        self.pictureChanged=True
        self.petPicture.configure(image=self.PlayBadger)

    def update(self):
        if self.timeSincePictureChange > 3:
            self.ResetImage()
        else:
            self.timeSincePictureChange += 1
