__author__ = 'Adam Clemons'
# Built in Classes
import tkinter as tk
from tkinter import ttk
import _thread as thread
import queue
from time import sleep

# Custom Classes
from Pet import Pet
from PetView import PetView

# TODO: add logging to entire project

# Functions that we need to perform actions to our Pet

class PetController():
    def __init__(self):
        #Initialize Window, without putting a value in it yet
        self.window = None
        self.view = PetView(self.window)
        self.model = Pet("Honey Badger")
        # This queue's actions so that two threads don't try to access something at the same time
        self.request_queue = queue.Queue()
        self.result_queue = queue.Queue()

        # Adding buttons/Controls to the View window
        # TODO: Use Lambdas instead of wrapper functions
        ttk.Button(self.view.mainframe, text="Feed", command=self.threadedFeed).grid(column=2, row=4)
        ttk.Button(self.view.mainframe, text="Play", command=self.threadedPlay).grid(column=2, row=5)
        ttk.Button(self.view.mainframe, text="Clean", command=self.threadedClean).grid(column=2, row=6)

# --------------------------THREADING CODE ------------------------------------------ #

    # Remember this? - Copied and Pasted
    # Thread main is where all the work will get done.
    def submitAction(self, action, *arguments, **keyWordArguments):
        self.request_queue.put((action, arguments, keyWordArguments))
        print(action)
        print("submitted successfully")
        return self.result_queue.get()

    def threadmain(self):
        def timertick():
            try:
                action, arguments, keyWordArguments = self.request_queue.get_nowait()
            except queue.Empty:
                pass
            else:
                print("something in queue")

                print("Hunger: "+str(self.model.hunger))
                print("Happiness: "+str(self.model.happiness))
                print("Cleanliness: "+str(self.model.cleanliness))


                retval = action(*arguments, **keyWordArguments)
                self.result_queue.put(retval)
            self.window.after(500, timertick)

        self.window = tk.Tk()
        timertick()
        self.window.mainloop()

# -------------------------/THREADING CODE ------------------------------------------ #

# Actions to be performed by the controller
    def feed(self):
        if self.model.hunger > 10:
            self.model.hunger += self.model.hungerRate

    def play(self):
        if self.model.hunger > 0:
            if self.model.happiness < 10:
                self.model.hunger -= 1
                self.model.happiness += 1

    def clean(self):
        if self.model.cleanliness > 0:
            self.model.cleanliness -= 1

# Actions on timer
    def feedDecay(self):
        if self.model.hunger > 0:
            self.model.hunger -= 1

    def happinessDecay(self):
        if self.model.happiness > 0:
            self.model.happiness -= 1

    def cleanDecay(self):
        if self.model.cleanliness > 0:
            self.model.cleanliness -= 1

    def update(self):
        self.feedDecay()
        self.happinessDecay()
        self.cleanDecay()

    def updateValues(self):
        # Set variables for the UI
        self.view.petHunger.set(self.model.getHunger())
        self.view.petHappiness.set(self.model.getHappiness())
        self.view.petCleanliness.set(self.model.getCleanliness())

# Threaded wrapping functions to use our super cool threads
    def threadedFeed(self):
        self.submitAction(self.feed)

    def threadedPlay(self):
        self.submitAction(self.play)

    def threadedClean(self):
        self.submitAction(self.clean)

    def threadedFeedDecay(self):
        self.submitAction(self.feedDecay)

    def threadedHappinessDecay(self):
        self.submitAction(self.happinessDecay)

    def threadedCleanDecay(self):
        self.submitAction(self.cleanDecay)

    def threadedUpdate(self):
        self.submitAction(self.update)

# END OF SETTING IT UP

    def run(self):
        thread.start_new_thread(self.threadmain, ())
        secondsPassed = 0
        while True:
            secondsPassed += 1
            self.threadedUpdate()
            sleep(1)