__author__ = 'Adam'

class virtualPet:
#Defining Initiation method - Sets up defaults when new object is created
    def __init__(self, name):
        self.name=name
        self.size=1
        self.color="blue"
        self.hunger=5
        self.happiness=5


#Getters for Properties
    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getColor(self):
        return self.color

    def getHunger(self):
        return self.hunger

    def getHappiness(self):
        return self.happiness

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
            return
        else:
            return

    def grow(self):
        ''' your pet can get bigger'''
        self.size +=1
        return

    def play(self):
        '''play with your pet, they will use up some of their hunger, so be sure to feed them'''
        if(self.hunger > 0):
            self.hunger -= 1
            self.happiness += 1
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

