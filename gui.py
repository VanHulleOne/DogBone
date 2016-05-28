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

    e = Entry(root)
    e.pack()
    
    
    
    root.mainloop()    