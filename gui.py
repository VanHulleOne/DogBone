# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:39:58 2016

@author: alexd
"""

from tkinter import *    #GUI module

def set_labels(all_labels, texts):
    for x in range(0, texts.length):
        all_labels[x] = Label(root, text=texts[x]).grid(row=x,column=0)

#function to make an entry widget
#def make_entry(parent, caption):
#    print(fill)
    
#def print_content():
#    print(e.get())
    
def save():
    label4 = Label(root,text='success').grid(row=4,column=2)
    
#only works if program is used as the main program, not as a module    
#if __name__ == '__main__':

#set up variables and arrays
labels = [label_outline, label_solidityRatio, label_printSpeed, label_shiftX,
          label_shiftY, label_firstLayerShiftZ, label_numLayers, label_trimAdjust,
          label_pattern, label_designType, label_inFillAngleDegrees, label_pathWidth,
          label_layerHeight, label_inFillShiftX, label_inFillShiftY,
          label_numShells, label_outputFileName, label_startGcodeFileName,
          label_endGcodeFileName, label_outputSubDirectory,
          label_startEndSubDirectory]

label_text = ["outline", "solidityRatio", "printSpeed", "shiftX", "shiftY", "firstLayerShiftZ",
              "numLayers", "trimAdjust", "pattern", "designType", "inFillAngleDegrees",
              "pathWidth", "layerHeight", "inFillShiftX", "inFillShiftY", "numShells", "outputFileName",
              "start_Gcode_Filename", "end_Gcode_FileName", "outputSubdirectory", "startEndSubDirectory"]

#GUI    
root = Tk()         #creates GUI
root.title("3D Printer Parameter Setter")
root.geometry("400x400+100+100")

#one=StringVar()
#two=StringVar()

#labeltext = StringVar()
#labeltext.set("Enter here")
#label1 = Label(root, text = "Enter here:", height = 4).grid(row=0,column=2)
#label2 = Label(root, text = "Enter:", height = 4).grid(row=1,column=0)
#label3 = Label(root, text =  "here:", height = 4).grid(row=2,column=0)#

#e1 = Entry(root, textvariable=one).grid(row=1,column=2)
#e2 = Entry(root, textvariable=two).grid(row=2,column=2)

#button1=Button(root,text="Submit",command=save).grid(row=3,column=2)

#set_labels(labels, label_text)
for x in range(0, texts.length):
    all_labels[x] = Label(root, text=texts[x]).grid(row=x,column=0)

root.mainloop()    