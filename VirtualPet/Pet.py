__author__ = 'Adam Clemons'

class Pet():
# Defining Initiation method - Sets up defaults when new object is created
    def __init__(self, name, callback):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 50
        self.hungerRate = 2
        self.happinessRate = 2
        self.cleanlinessRate = 2
        # Time since action performed
        self.timeSinceFeed = 0
        self.timeSincePlay = 0
        self.timeSinceClean = 0
        # A variable to check for changes to see if we need to update anything
        self.callback = callback

    # This is for the Model/View/Controller Layout
    def modelDidChange(self):
        self.callback.modelDidChangeDelegate

    def getModel(self):
        return self.Pet

# Getters for Attributes - Not required in Python, but helpful to understand what's happening, or to port to other languages
    def getName(self):
        return self.name

    def getHunger(self):
        return self.hunger

    def getHappiness(self):
        return self.happiness

    def getCleanliness(self):
        return self.cleanliness

    def getHungerDecayRate(self):
        return self.hungerRate

    def getHappinessDecayRate(self):
        return self.happinessRate

    def getCleanlinessDecayRate(self):
        return self.cleanlinessRate

    def getTimeSinceFeed(self):
        return self.timeSinceFeed

    def getTimeSincePlay(self):
        return self.timeSincePlay

    def getTimeSinceClean(self):
        return self.timeSinceClean

# Setters for Attributes
    def setName(self, param):
        self.name = param
        self.modelDidChange()

    def setHunger(self, param):
        self.hunger = param
        self.modelDidChange()

    def setHappiness(self, param):
        self.happiness = param
        self.modelDidChange()

    def setCleanliness(self, param):
        self.cleanliness = param
        self.modelDidChange()

    def setHungerDecayRate(self, param):
        self.hungerRate = param
        self.modelDidChange()

    def setHappinessDecayRate(self, param):
        self.happinessRate = param
        self.modelDidChange()

    def setCleanlinessDecayRate(self, param):
        self.cleanlinessRate = param
        self.modelDidChange()

    def setTimeSinceFeed(self, param):
        self.timeSinceFeed = param
        self.modelDidChagne()

    def setTimeSincePlay(self, param):
        self.timeSincePlay = param
        self.modelDidChange()

    def setTimeSinceClean(self, param):
        self.timeSinceClean = param
        self.modelDidChange()