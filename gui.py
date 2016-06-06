# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:39:58 2016
@author: alexd
"""

from tkinter import *    #GUI module
import json

#global variables 
text_variable = {} #dictionary with variable name as key and StringVar as value

#methods
def set_labels(all_labels, texts):
    for x in range(0, len(texts)):
        all_labels[x] = Label(root, text=texts[x]).grid(row=x,column=0)
        
def set_entries(all_entries, texts, default_values):
    global text_variable
    for x in range(0, len(texts)):
        text_variable[texts[x]] = StringVar(root, value=default_values[x])
    for x in range(0, len(texts)):
        all_entries[x] = Entry(root, textvariable=text_variable[texts[x]]).grid(row=x,column=2)
    return 

#function to make an entry widget
#def make_entry(parent, caption):
#    print(fill)
    
#def print_content():
#    print(e.get())
    
def save():
    global text_variable
    data = {}
    for key in text_variable:
        data[key] = text_variable[key].get()
    with open('data4.json', 'w') as fp:
        json.dump(data, fp)
        
def upload():
    global text_variable
    data = {}
    with open('data3.json', 'r') as fp:
        data = json.load(fp)
    for key in data:
        text_variable[key].set(data[key])
    
#only works if program is used as the main program, not as a module    
#if __name__ == '__main__':

#set up variables and arrays

#initialize Labels and Entries

#Part Parameters
label_outline = None
label_solidityRatio = None
label_printSpeed = None
label_shiftX = None
label_shiftY = None
label_firstLayerShiftZ = None 
label_numLayers = None
label_pattern = None
label_designType = None

entry_outline = None
entry_solidityRatio = None
entry_printSpeed = None
entry_shiftX = None
entry_shiftY = None
entry_firstLayerShiftZ = None 
entry_numLayers = None
entry_pattern = None
entry_designType = None

#Layer Parameters
label_inFillAngleDegrees = None 
label_pathWidth = None
label_layerHeight = None
label_inFillShiftX = None 
label_inFillShiftY = None
label_numShells = None
label_trimAdjust = None

entry_inFillAngleDegrees = None 
entry_pathWidth = None
entry_layerHeight = None
entry_inFillShiftX = None 
entry_inFillShiftY = None
entry_numShells = None
entry_trimAdjust = None

#File Parameters
label_outputFileName = None 
label_startGcodeFileName = None
label_endGcodeFileName = None
label_outputSubDirectory = None
label_startEndSubDirectory = None

entry_outputFileName = None 
entry_startGcodeFileName = None
entry_endGcodeFileName = None
entry_outputSubDirectory = None
entry_startEndSubDirectory = None


#array of Labels
labels = [label_outline, label_solidityRatio, label_printSpeed, label_shiftX,
          label_shiftY, label_firstLayerShiftZ, label_numLayers, label_trimAdjust,
          label_pattern, label_designType, label_inFillAngleDegrees, label_pathWidth,
          label_layerHeight, label_inFillShiftX, label_inFillShiftY,
          label_numShells, label_outputFileName, label_startGcodeFileName,
          label_endGcodeFileName, label_outputSubDirectory,
          label_startEndSubDirectory]

#array of Entries
entries = [entry_outline, entry_solidityRatio, entry_printSpeed, entry_shiftX, 
           entry_shiftY, entry_firstLayerShiftZ, entry_numLayers, entry_pattern, 
           entry_designType, entry_inFillAngleDegrees, entry_pathWidth,
           entry_layerHeight, entry_inFillShiftX, entry_inFillShiftY, entry_numShells,
           entry_trimAdjust, entry_outputFileName, entry_startGcodeFileName,
           entry_endGcodeFileName, entry_outputSubDirectory, entry_startEndSubDirectory]

#array of Strings of the variables
all_text = ["outline", "solidityRatio", "printSpeed", "shiftX", "shiftY", "firstLayerShiftZ",
              "numLayers", "trimAdjust", "pattern", "designType", "inFillAngleDegrees",
              "pathWidth", "layerHeight", "inFillShiftX", "inFillShiftY", "numShells", "outputFileName",
              "start_Gcode_Filename", "end_Gcode_FileName", "outputSubdirectory", "startEndSubDirectory"]
              
#array of Strings of the default values
defaults = ["ds.regularDogBone()", "[1.09]", "[2000]", "[10, 50]", "[10, 35, 60]", "0", "[8]", "None", 
           "0", "[0, -45, 90, 45, 45, 90, -45]", "[0.5]", "[0.4]", "[0]", "[0]", "[13,1,1,0,0,1,1]",
            "[2*c.EPSILON]", "'ZigZag.gcode'", "'Start_Gcodee_Tazt.txt'", "'End_Gcode_Taz5.txt'", 
            "os.path.dirname(os.path.realpath(__file__))", "currPath + '\\Gcode'", 
            "currPath + '\\Start_End_Gcode'"]

#set up GUI    
root = Tk()         #creates GUI
root.title("3D Printer Parameter Setter")
root.geometry("400x500+100+100")

set_labels(labels, all_text)
set_entries(entries, all_text, defaults)
buttonSave = Button(root,text="Save",command=save).grid(row=len(all_text),column=2)
buttonUpload = Button(root,text="Upload",command=upload).grid(row=len(all_text),column=3)

root.mainloop()    