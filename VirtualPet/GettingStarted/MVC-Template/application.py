__author__ = 'AdamClmns'
import tkinter as tk

from controller import controller

root=tk.Tk()
app = controller(root)

def tick():
    global app
    app.timerUpdate()
    app.view.frame.after(500, tick)

if __name__=='__main__':
    global root
    root.title("Example MVC")
    tick()
    root.mainloop()