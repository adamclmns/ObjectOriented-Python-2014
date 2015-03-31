__author__ = 'Adam Clemons'
#Built in Classes
import tkinter as tk

#Custom Classes
import Pet
import PetView



# Functions that we need to perform actions to our Pet
class PetController:
    def __init__(self):
        self.view = PetView()
        self.model = Pet()
        self.window = tk.Tk()


    def feed(self):
        '''Feed your pet to increase it's 'hunger' '''
        if self.model.hunger < 10:
            self.model.hunger += self.model.hungerRate
            return
        else:
            return


    def play(self, model):
        '''play with your pet, they will use up some of their hunger, so be sure to feed them'''
        if self.model.hunger > 0 :
            self.model.hunger -= 1
            self.model.happiness += 1
            return
        else:
            return

    def bored(self, model):
        '''be sure to play with your pet, or they'll get bored and slowly become unhappy'''
        if self.model.happiness > 0:
            self.model.happiness -= 1
            return
        else:
            return


