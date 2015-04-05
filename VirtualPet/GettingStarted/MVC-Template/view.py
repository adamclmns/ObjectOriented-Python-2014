__author__ = 'AdamClmns'

import tkinter as tk

class view():
    def __init__(self, controller):
        self.frame=tk.Frame()
        self.frame.grid(column=0, row=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.controller = controller
        #String variable to update
        self.exampleValueDisplay = tk.StringVar()
        # Label for displaying stringvar
        tk.Label(self.frame, textvariable=self.exampleValueDisplay).grid(column=1, row=1)
        tk.Button(self.frame, text="ExampleUpdate", name="exampleUpdate", command=lambda: self.controller.exampleActionPerformed()).grid(column=2, row=1)
        tk.Label(self.frame, text="Press the button to increase the value by one")




