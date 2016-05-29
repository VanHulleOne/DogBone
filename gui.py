# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:39:58 2016

@author: alexd
"""

from tkinter import *    #GUI module

#function to make an entry widget
def make_entry(parent, caption):
    print(fill)
    
def print_content():
    print(e.get())
    
#only works if program is used as the main program, not as a module    
if __name__ == '__main__':    
    root = Tk()         #creates GUI
    root.title("3D Printer Parameter Setter")
    root.geometry("500x500+100+100")
    
    labeltext = StringVar()
    labeltext.set("Enter here")
    label1 = Label(root, textvariable = labeltext, height = 4)
    e = Entry(root, textvariable = labeltext)
    label1.pack(side=LEFT)
    e.pack(side=RIGHT)
    
    
    root.mainloop()    