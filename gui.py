# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:39:58 2016
@author: alexd
"""

from tkinter import *    #GUI module
import json

##################
#global variables#
##################

#name of JSON file to be saved
textSave = StringVar(root)

#name of JSON file to be uploaded
textUpload = StringVar(root)

#dictionary with variable name as key and StringVar as value
text_variable = {} 

#dictionary with variable name as key and Label as value        
labels = {}
           
#dictionary with variable name as key and Entry as value
entries = {}

#part parameters = outline(0) - designType(8)
#layer parameters = inFilleAngleDegrees(9) - trimAdust(15)
#file parameters = outputFileName(16) - startEndSubDirectory(20)

#array of Strings of the variables
texts = ["outline", "solidityRatio", "printSpeed", "shiftX",                #part parameters
         "shiftY", "firstLayerShiftZ", "numLayers",  "trimAdjust",          #part parameters
         "pattern", "designType"                                            #part parameters
         "inFillAngleDegrees", "pathWidth", "layerHeight",                  #layer parameters
         "inFillShiftX", "inFillShiftY", "numShells",                       #layer parameters
         "outputFileName","start_Gcode_Filename", "end_Gcode_FileName",     #file parameters
         "currPath", "outputSubdirectory",                                  #file parameters
         "startEndSubDirectory"]                                            #file parameters
              
#array of Strings of the default values
defaults = ["ds.regularDogBone()", "[1.09]", "[2000]", "[10, 50]",                  #part parameters
            "[10, 35, 60]", "0", "[8]", "[2*c.EPSILON]",                            #part parameters
            "None", "0",                                                            #part parameters
            "[0, -45, 90, 45, 45, 90, -45]", "[0.5]", "[0.4]",                      #layer parameters
            "[0]", "[0]", "[13,1,1,0,0,1,1]",                                       #layer parameters
            "'ZigZag.gcode'", "'Start_Gcodee_Taz5.txt'", "'End_Gcode_Taz5.txt'",    #file parameters
            "os.path.dirname(os.path.realpath(__file__))", "currPath + '\\Gcode'",  #file parameters
            "currPath + '\\Start_End_Gcode'"]                                       #file parameters
            
#########
#methods#
#########
            
#initial creation of labels
def set_labels():
    global labels       #dictionary of labels
    global texts        #array of variable names
    
    for x in range(0, len(texts)):
        #create label
        labels[texts[x]] = Label(root, text=texts[x])
        #use grid() after creating label or dictionary value will be "NoneType"
        labels[texts[x]].grid(row=x+1,column=0)   
        
    return   
        
#initial creation of entries
def set_entries():
    global text_variable    #dictionary of StringVar() with default text as the value
    global entries          #dictionary of entries
    global texts            #array of variable names
    global defaults         #array of default values
    
    for x in range(0, len(texts)):
        #set textvariable to StringVar with default text as value
        text_variable[texts[x]] = StringVar(root, value=defaults[x])
        
    for x in range(0, len(texts)):
        #create entry 
        entries[texts[x]] = Entry(root, textvariable=text_variable[texts[x]])
        #use grid() after creating entry or dictionary value will be "NoneType"
        entries[texts[x]].grid(row=x+1,column=1)
        
    return 
    
#saves the dictionary of the StringVars to a JSON file    
def save():
    global text_variable    #dictionary of StringVar with current values from user
    global textSave         #StringVar with name to save JSON file as
    filename = textSave + ".json"    #adds .json to name
    
    with open(filename, 'w') as fp:
        json.dump(text_variable, fp)    #save JSON file
        
    return 

#uploads dictionary from JSON file to replace current StringVar values       
def upload():
    global text_variable    #dictionary of StringVar of the entry values
    global textUpload       #StringBar with name of JSON file to upload
    data = {}               #new dictionary that will be replaced with dictionary from JSON file
    filename = textUpload + ".json"     #adds .json to name
    
    with open(filename, 'r') as fp:
        data = json.load(fp)    #upload JSON file
        
    for key in data:
        text_variable[key].set(data[key])   #replace current StringVar values with data from JSON file
        
    return
    
#switch to tab with all parameters    
def use_all():
    global labels       #dictionary with labels as values
    global entries      #dictionary with entries as values
    
    for x in range(0, len(labels)):
        labels[texts[x]].grid(row=x+1,column=0)    #show labels
        entries[texts[x]].grid(row=x+1,column=2)   #show entries
        
    return
    
#switch to tab with only part parameters
def use_parts():
    global labels       #dictionary with labels as values
    global entries      #dictionary with entries as values
    global texts        #array of variable names
    
    for x in range(0,9):
        labels[texts[x]].grid(row=x+1,column=0)   #show labels
        entries[texts[x]].grid(row=x+1,column=2)  #show entries
        
    for x in range(9, len(texts)):
        labels[texts[x]].grid_forget()    #hide labels
        entries[texts[x]].grid_forget()   #hide entries
        
    return
  
#switch to tab with only layer parameters  
def use_layers():
    global labels       #dictionary with labels as values
    global entries      #dictionary with entries as values
    global texts        #array of variable names
    
    for x in range(9,16):
        labels[texts[x]].grid(row=x+1,column=0)     #show labels
        entries[texts[x]].grid(row=x+1,column=2)    #show entries
        
    for x in range(16, len(labels)):
        labels[texts[x]].grid_forget()      #hide labels
        entries[texts[x]].grid_forget()     #hide entries
        
    for x in range(0,9):
        labels[texts[x]].grid_forget()      #hide labels
        entries[texts[x]].grid_forget()     #hide entries
        
    return
  
#switch to tabe with only file parameters  
def use_files():
    global labels       #dictionary with labels as values
    global entries      #dictionary with entries as values
    global texts        #array of variable names
        
    for x in range(16,len(labels)):
        labels[texts[x]].grid(row=x+1,column=0)     #show labels
        entries[texts[x]].grid(row=x+1,column=2)    #show entries
        
    for x in range(0,16):
        labels[texts[x]].grid_forget()      #hide labels
        entries[texts[x]].grid_forget()     #hide entries
    
    return
    
#creates label, entry, and button for saving all values
def save_option():
    global textSave     #StringVar with name to save JSON file as
    global texts        #array of variable names, only needed to reference length
    
    #create label
    labelSave = Label(root, text="Enter filename to save as (no .json):")
    labelSave.grid(row=len(texts)+1,column=0)
    
    #create entry
    entrySave = Entry(root, textvariable=textSave)
    entrySave.grid(row=len(texts)+1,column=1)
    
    #create button
    buttonSave = Button(root,text="Save",command=save).grid(row=len(texts)+1,column=2)

#creates label, entry, and button for uploading all values    
def upload_option():
    global textUpload   #StringVar with name to save JSON file as
    global texts        #array of variable names, only needed to reference length
    
    #create label
    labelUpload = Label(root, text="Enter filename to upload (no .json):")
    labelUpload.grid(row=len(texts)+2,column=0)
    
    #create entry
    entryUpload = Entry(root, textvariable=textUpload)
    entryUpload.grid(row=len(texts)+2,column=1)
    
    #create button
    buttonUpload = Button(root,text="Upload",command=upload).grid(row=len(texts)+2,column=2)
    
#only works if program is used as the main program, not as a module    
#if __name__ == '__main__':

##############
#GUI creation#
##############

#create window    
root = Tk()

#set window title
root.title("3D Printer Parameter Setter")
#format window size -- width=400, height=500, 100px from left of screen, 100px from top of screen
root.geometry("500x550+100+100")

#initial creation of labels and entries
set_labels()
set_entries()

#set up save option
save_option()

#set up upload option
upload_option()

#tab buttons (all parameters, part parameters, layer parameters, file parameters)
buttonAll = Button(root,text="All",command=use_all).grid(row=0,column=0)
buttonParts = Button(root,text="Parts",command=use_parts).grid(row=0,column=1)
buttonLayers = Button(root,text="Layers",command=use_layers).grid(row=0,column=2)
buttonFiles = Button(root,text="Files",command=use_files).grid(row=0,column=3)

#keeps GUI open, always necessary
root.mainloop() 