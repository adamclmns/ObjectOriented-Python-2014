from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#(1)adding the model 2014-May-28 with convenience method
class MyModel():
    def __init__(self,vc):
        self.vc = vc
        self.myList = []
        self.count = 0
#(2)Delegate goes here. Model would call this on internal change
    def modelDidChange(self):
        self.vc.modelDidChangeDelegate()
# Setters and getters for the model
    def getList(self):
        return self.myList
    def addToList(self,item):
        myItem = item
        myList = self.myList
        myList.append(myItem)
        self.myList=myList
        self.modelDidChange()
    def getItemAtIndex(self,index):
        return self.myList[index]
# other methods
    def addRecordToList(self,penguin,action):
        self.addToList([penguin,action])

