__author__ = 'AdamClmns'

from Tkinter import *
import time

root = Tk()
time1 = ''
numberOfTicks = 0
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
count = Label(root, bg='white')
count.pack()

def changeColor(color):
    clock.configure(bg=color)

def resetCount():
    numberOfTicks=0

button2=Button(text="reset Count", command=resetCount)
button2.pack()
button=Button(text="Change Background Color", command=lambda: changeColor('orange'))
button.pack()


def tick():
    global time1
    global numberOfTicks
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        numberOfTicks +=1
        clock.config(text=time2)
        count.config(text=numberOfTicks)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

tick()
root.mainloop()