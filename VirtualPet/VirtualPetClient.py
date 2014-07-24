#VirtuaPetClient


__author__ = 'Adam'
from virtualPet import virtualPet
from VirtualPet.PetInterface import userInterface


pet=virtualPet.virtualPet("Bob")
UI=userInterface(pet)
UI.root.mainloop()


