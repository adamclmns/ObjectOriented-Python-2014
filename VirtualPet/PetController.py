__author__ = 'AdamClmns'

#Import Custom View and Model
from Pet import Pet
from PetView import PetView


class PetController():

    def __init__(self, parent):
        self.parent=parent
        self.model=Pet("Name",self)
        self.view=PetView(self)
        # TODO: setup the model
        # TODO: Set up the view
        self.view.petHunger.set(self.model.hunger)
        self.view.petCleanliness.set(self.model.cleanliness)
        self.view.petHappiness.set(self.model.happiness)

    #Event hanlders - for buttons in view
    def feedPressed(self):
        self.model.hunger += 5
        self.model.setTimeSinceFeed(0)
        self.view.Feed()
        self.view.petHunger.set(self.model.hunger)

    def cleanPressed(self):
        self.model.cleanliness+=5
        self.model.setTimeSinceClean(0)
        self.view.Clean()
        self.view.petCleanliness.set(self.model.cleanliness)

    def playPressed(self):
        self.model.happiness+=5
        self.model.setTimeSincePlay(0)
        self.view.Play()
        self.view.petHappiness.set(self.model.happiness)

    def update(self):
        if self.model.happiness > 0:
            self.model.setTimeSincePlay(self.model.timeSincePlay + 1)
            if self.model.timeSincePlay > 4:
                self.model.setHappiness(self.model.hunger - 1)

        if self.model.cleanliness > 0:
            self.model.setTimeSinceClean(self.model.timeSinceClean + 1)
            if self.model.timeSinceClean > 4:
                self.model.setHunger(self.model.hunger - 1)

        if self.model.hunger >0:
            self.model.setTimeSinceFeed(self.model.timeSinceFeed + 1)
            if self.model.timeSinceFeed > 4:
                self.model.setHunger(self.model.hunger - 1)

        self.view.update()

    def modelDidChangeDelegate(self):
        print("Model Updated")
        self.view.petHunger.set(self.model.hunger)
        self.view.petCleanliness.set(self.model.cleanliness)
        self.view.petHappiness.set(self.model.happiness)
