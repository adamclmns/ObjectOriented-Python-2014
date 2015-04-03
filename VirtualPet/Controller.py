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

    #Event hanlders - for buttons in view
    def feedPressed(self):
        self.model.hunger+=1
        self.view.petHunger.set(self.model.hunger)

    def cleanPressed(self):
        self.model.cleanliness+=1
        self.view.petCleanliness.set(self.model.cleanliness)

    def playPressed(self):
        self.model.happiness+=1
        self.view.petHappiness.set(self.model.happiness)

    def updateDecay(self):
        if self.model.happiness > 0:
            self.model.happiness-=1
            self.view.petHappiness.set(self.model.happiness)

        if self.model.cleanliness >0:
            self.model.cleanliness-=1
            self.view.petCleanliness.set(self.model.cleanliness)

        if self.model.hunger >0:
            self.model.hunger-=1
            self.view.petHunger.set(self.model.hunger)

    def modelDidChangeDelegate(self):
        print("Model Updated")
