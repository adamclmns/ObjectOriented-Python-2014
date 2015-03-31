__author__ = 'Adam Clemons'

class Pet:
#Defining Initiation method - Sets up defaults when new object is created
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.cleanliness = 5
        self.hungerRate = 2
        self.happinessRate = 2
        self.cleanlinessRate = 2

##-------------------------------------------------------------OVER HEAD CODE ------------------------------------##
#Getters for Attributes - Not required for Python
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

#Setters for Attributes - Not required for Python
    def setName(self, param):
        self.name = param

    def setHunger(self, param):
        self.hunger = param

    def setHappiness(self, param):
        self.happiness = param

    def setCleanliness(self, param):
         self.cleanliness = param

    def setHungerDecayRate(self, param):
        self.hungerRate = param

    def setHappinessDecayRate(self, param):
        self.happinessRate = param

    def setCleanlinessDecayRate(self, param):
        self.cleanlinessRate = param

##-------------------------------------------------------------OVER HEAD CODE ------------------------------------##

