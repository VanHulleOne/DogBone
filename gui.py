# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:39:58 2016

@author: alexd
"""

from tkinter import *    #GUI module

#function to make an entry widget
#def make_entry(parent, caption):
#    print(fill)
    
#def print_content():
#    print(e.get())
    
def save():
    label4 = Label(root,text='success').grid(row=4,column=2)
    
#only works if program is used as the main program, not as a module    
#if __name__ == '__main__':    
root = Tk()         #creates GUI
root.title("3D Printer Parameter Setter")
root.geometry("400x400+100+100")

one=StringVar()
two=StringVar()

labeltext = StringVar()
labeltext.set("Enter here")
label1 = Label(root, text = "Enter here:", height = 4).grid(row=0,column=2)
label2 = Label(root, text = "Enter:", height = 4).grid(row=1,column=0)
label3 = Label(root, text =  "here:", height = 4).grid(row=2,column=0)

e1 = Entry(root, textvariable=one).grid(row=1,column=2)
e2 = Entry(root, textvariable=two).grid(row=2,column=2)

button1=Button(root,text="Submit",command=save).grid(row=3,column=2)

root.mainloop()    