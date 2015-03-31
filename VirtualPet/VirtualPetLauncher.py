__author__ = 'Adam Clemons'


from Pet import virtualPet
from VirtualPet.PetView import userInterface


pet=virtualPet("Bob")
UI=userInterface(pet)
UI.root.mainloop()


