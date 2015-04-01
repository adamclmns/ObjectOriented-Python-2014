__author__ = 'Adam Clemons'
import _thread as thread
from PetController import PetController
from time import sleep

# TODO: Will call the controller and create all objects here. This launcher will contain just a main function


# This is where our program starts. This is main.
if __name__ == '__main__':
    Controller = PetController()
    # Starting a new thread.
    thread.start_new_thread(Controller.threadmain, ())
    secondsPassed = 0
    while 1:
        secondsPassed += 1
        Controller.threadedUpdate()
        sleep(1)

