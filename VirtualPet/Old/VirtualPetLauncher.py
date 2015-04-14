__author__ = 'Adam Clemons'

from tkinter import *
from PetController import PetController


from time import sleep
# TODO: Set ticksSincedUpdated for individual values of hunger, happiness, and cleanliness
# TODO: add extensibility template for new functions
# TODO: Add images
# TODO: convert to Python 2.7
#

root=Tk()
root.configure(width=640, height=480)
app=PetController(root)
i = 0

def tick():
    global app
    app.timedUpdate()
    app.view.mainframe.after(500, tick)


def main():
    global root
    root.title("Virtual Pet")

    tick()
    root.mainloop()


# This is where our program starts. This is main.
if __name__ == '__main__':
    main()
