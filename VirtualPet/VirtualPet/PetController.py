__author__ = 'AdamClmns'

# Import Custom View and Model
from Pet import Pet
from PetView import PetView


class PetController():

    def __init__(self, parent):
        self.parent=parent
        self.model=Pet(self)
        self.view=PetView(self)
        # TODO: setup the model
        # TODO: Set up the view
        self.view.petHunger.set(self.model.hunger)
        self.view.petCleanliness.set(self.model.cleanliness)
        self.view.petHappiness.set(self.model.happiness)

    def modelUpdated(self):
        # Update the view with new values
        self.view.petHunger.set(self.model.hunger)
        self.view.petHappiness.set(self.model.happiness)
        self.view.petCleanliness.set(self.model.cleanliness)




    # These functions are mapped to the buttons in the View
    def feedActionPerformed(self):
        if (self.model.hunger + 5) <= 50:
            self.view.feed()
            self.model.setHunger(self.model.hunger + 5)
            self.model.timeSinceFeed = 0

    def playActionPerformed(self):
        if (self.model.happiness + 5) <= 50:
            self.view.play()
            self.model.setHappiness(self.model.happiness + 5)
            self.model.timeSincePlay = 0


    def cleanActionPerformed(self):
        if (self.model.cleanliness + 5) <= 50:
            self.view.clean()
            self.model.setCleanliness(self.model.cleanliness + 5)
            self.model.timeSinceClean = 0

    # This function is going to be a part of the loop and determine when and how to reduce the attribute values
    # This is not the most efficient way to do this...
    def timedUpdate(self):
        self.view.tick()
        self.model.tick()
        if self.model.hunger > 0:
            if self.model.timeSinceFeed > 5:
                self.model.setHunger(self.model.hunger - 1)

        if self.model.happiness > 0:
            if self.model.timeSincePlay > 5:
                self.model.setHappiness(self.model.happiness -1)

        if self.model.cleanliness >0:
            if self.model.timeSinceClean > 5:
                self.model.setCleanliness(self.model.cleanliness - 1)


    #Doing this one differently so it doesn't take as long
