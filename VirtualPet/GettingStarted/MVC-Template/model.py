__author__ = 'AdamClmns'

class model():
    def __init__(self, controller):
        self.exampleValue = 10
        self.timeSinceExampleValueUpdate = 0

        self.controller = controller

    def modelUpdated(self):
        self.controller.modelUpdated()

    def setExampleValue(self, parameter):
        self.exampleValue = parameter
        self.modelUpdated()

    def setTimeSinceExampleValueUpdate(self, parameter):
        self.timeSinceExampleValueUpdate = parameter
        self.modelUpdated()

