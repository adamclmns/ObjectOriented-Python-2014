__author__ = 'AdamClmns'

#import Model
from model import model
#import View
from view import view

class controller():
    def __init__(self, parent):
        self.parent = parent
        self.model= model(self)
        self.view=view(self)

        # Set view values to the values in the model

    def modelUpdated(self):
        print("Model has been updated")
        self.view.exampleValueDisplay.set(self.model.exampleValue)

    def exampleActionPerformed(self):
        #Change the value in the model
        self.model.setExampleValue(0)
        self.model.setTimeSinceExampleValueUpdate(0)

    def timerUpdate(self):
        if(self.model.timeSinceExampleValueUpdate > 5):
            self.model.setExampleValue(self.model.exampleValue +1)
        self.model.setTimeSinceExampleValueUpdate(self.model.timeSinceExampleValueUpdate +1)