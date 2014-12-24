__author__ = 'Adam'

class petClass:
#Defining Initiation method - Sets up defaults when new object is created
    def __init__(self, name):
        self.name=name
        self.hunger=5
        self.happiness=5
        self.dirtiness=0


#Getters for Properties
    def getName(self):
        return self.name

    def getHunger(self):
        return self.hunger

    def getHappiness(self):
        return self.happiness

    def getDirtiness(self):
        return self.dirtiness

#Functions that change or update property values
    def setName(self,name):
        '''Rename your pet'''
        if(self.name!=name):
            self.name = name
            return
        else:
            return

    def feed(self):
        '''Feed your pet to increase it's 'hunger' '''
        if(self.hunger < 10):
            self.hunger +=1
            self.dirtiness +=1
            return
        else:
            return

    def play(self):
        '''play with your pet, they will use up some of their hunger, so be sure to feed them'''
        if(self.hunger > 0):
            self.hunger -= 1
            self.happiness += 1
            self.dirtiness +=1
            return
        else:
            return

    def bored(self):
        '''be sure to play with your pet, or they'll get bored and slowly become unhappy'''
        if (self.happiness>0):
            self.happiness -=1
            return
        else:
            return

    def clean(self):
        self.dirtiness=0
        self.happiness +=1


