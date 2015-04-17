__author__ = 'Adam Clemons'

class Pet():
# Defining Initiation method - Sets up defaults when new object is created
    def __init__(self, controller):
        # Object Attributes
        self.name = ''
        self.hunger = 40
        self.happiness = 40
        self.cleanliness = 40
        # Time since action performed
        self.timeSinceFeed = 0
        self.timeSincePlay = 0
        self.timeSinceClean = 0
        # callback to the controller
        self.controller = controller


    # This is for the Model/View/Controller Layout - In other languages this is called the 'Service Layer'
    def modelUpdated(self):
        self.controller.modelUpdated()

    #Every Setter executes the callback to the controller
    def setName(self, param):
        self.name=param
        self.modelUpdated()

    def setHunger(self, param):
        self.hunger=param
        self.modelUpdated()

    def setHappiness(self, param):
        self.happiness=param
        self.modelUpdated()

    def setCleanliness(self, param):
        self.cleanliness=param
        self.modelUpdated()

    def setTimeSinceHungerIncrease(self, param):
        self.timeSinceFeed=param
        self.modelUpdated()

    def setTimeSinceHappinessIncrease(self, param):
        self.timeSincePlay=param
        self.modelUpdated()

    def setTimeSinceCleanlinessIncrease(self, param):
        self.timeSinceClean=param
        self.modelUpdated()

    def tick(self):
        self.timeSinceFeed += 1
        self.timeSincePlay += 1
        self.timeSinceClean += 1