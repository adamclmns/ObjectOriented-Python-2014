__author__ = 'Adam Clemons'

class Pet():
# Defining Initiation method - Sets up defaults when new object is created
    def __init__(self, name, vc):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 50
        self.hungerRate = 2
        self.happinessRate = 2
        self.cleanlinessRate = 2
        # A variable to check for changes to see if we need to update anything
        self.vc = vc

    # This is for the Model/View/Controller Layout
    def modelDidChange(self):
        self.vc.modelDidChangeDelegate

    def getModel(self):
        return self.Pet

# Getters for Attributes - Not required for Python
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

# Setters for Attributes - Not required for Python
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
