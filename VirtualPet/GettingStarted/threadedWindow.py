__author__ = 'Adam Clemons'

#Importing Python Standard Library Modules for Python 3.4. Importing as for compatibility with code written for 2.7
import tkinter as tk
import logging as logger
import _thread as thread
from time import sleep
import queue as Queue

#This queue's actions so that two threads don't try to access something at the same time
request_queue = Queue.Queue()
result_queue = Queue.Queue()
#This makes a global variable 't'. Pay attention to indentation.
t = None

#This puts things into the Request Queue and then pulls the next thing in the queue
#This is a global function
def submit_to_tkinter(callable, *args, **kwargs):
    request_queue.put((callable, args, kwargs))
    return result_queue.get()


#Thread main is where all the work will get done.
#This is a global function
def threadmain():
    #This makes global t available in threadmain():
    global t

    #Defining a function inside of a function, to use that function to do manythings at the same time.
    def timertick():
        try:
            callable, args, kwargs = request_queue.get_nowait()
        except Queue.Empty:
            pass
        else:
            print("something in queue")
            #Gets an action from the queue and executes it, and puts the result in another queue. If you want to read the results back later
            retval = callable(*args, **kwargs)
            result_queue.put(retval)
        #Tells timertick to repeat itself every 500 milliseconds
        t.after(500, timertick)

    #creates a window to put widgets in
    t = tk.Tk()
    #Sets the size of the window
    t.configure(width=640, height=480)
    #Adds a button to the window
    b = tk.Button(text='test', name='button', command=exit)
    #Gives the button explicit coordinates
    b.place(x=0, y=0)
    #this calls timer tick (inception). It'll get something from the queue and do it.
    timertick()
    #Th
    t.mainloop()


def setTitle():
    t.title("Hello world")

def setButtonText(button_text):
    #This will change the text of the child of 't' named 'button'
    t.children["button"].configure(text=button_text)

def getButtonText():
    #this will return the 'text' data from the child of 't' named 'button'
    return t.children["button"]["text"]


#This is where our program starts. This is main.
if __name__ == '__main__':
    #Starting a new thread.
    thread.start_new_thread(threadmain, ())

    secondsPassed = 0
    while 1:
        secondsPassed += 1
        print(str(secondsPassed) +" Seconds passed")

        if secondsPassed == 3:
            #Adds the set-title action to the queue
            submit_to_tkinter(setTitle)

        if secondsPassed == 5:
            #Changes the button text to "too slow"
            submit_to_tkinter(setButtonText, "Too Slow... ")

        if secondsPassed == 7:
            #prints the text that's in the button.
            print(submit_to_tkinter(getButtonText))

        sleep(1)