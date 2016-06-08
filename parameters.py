# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:52:29 2015
Contains all of the print parameters and the if __name__ == '__main__': logic
so the whole program can be run from here after making parameter changes.
Below is the command for NotePad++ to run this file.
C:\Anaconda3\python.exe -i "$(FULL_CURRENT_PATH)"
@author: lvanhulle
"""
import math
from collections import namedtuple
import constants as c
import doneShapes as ds
import figura as fg
import time
import itertools
import os
import numpy as np
import json

class param:
    
    

    """
    Part Parameters
    """
    outline = ds.regularDogBone() # The shape we will be printing
    solidityRatio = [1.09]#12]#, 0.1, 0.05] solidityRatio = PathArea/beadArea
    printSpeed = [2000] #mm/min head travel speed
    shiftX = [10, 50] # amount to shift part from printer origin in X
    shiftY = [10, 35, 60] # amount to shift part from printer origin in Y
    firstLayerShiftZ = 0 #correct for bed leveling
    numLayers = [8] #number of layers to make
    pattern = None
    # pattern = lg.LineGroup()
    # pattern.addLinesFromCoordinateList([[0,0],[2,2],[4,0]])
    designType = 0
    
    """
    Layer Parameters
    """
    infillAngleDegrees = [0, -45, 90, 45, 45, 90, -45] #degrees infill angle 90 is in Y direction 0 is in X direction
    pathWidth = [0.5] #mm distance between centerline of paths
    layerHeight = [0.4] #mm height per layer
    infillShiftX = [0]
    infillShiftY = [0]
    #flipLayer = [0] No longer implimented
    numShells = [13,1,1,0,0,1,1] # the number of shells max is 13 if 0.4999 path width is used
    trimAdjust = [2*c.EPSILON]
    
    data = {}
    
    def __init__(self, parameter):
        with open(parameter, 'r') as fp:
            data = json.load(fp)
            
        """
        File Parameters
        """
        self.outputFileName = 'ZigZag.gcode' #the name of the file you want output. git will ignore all .gcode unless they start with SAVE
        self.currPath = os.path.dirname(os.path.realpath(__file__))
        self.outputSubDirectory = self.currPath + '\\Gcode'
        self.startEndSubDirectory = self.currPath + '\\Start_End_Gcode'
        
        """
        Misc Parameters
        """
        self.filamentDiameter = 3.0 #mm dia of incoming filament
        self.filamentArea = math.pi*self.filamentDiameter**2/4.0
        self.nozzleDiameter = 0.5 #mm                                                   
           
        """
        Standard printing settings
        """
        self.RAPID = 4000 #mm/min
        self.TRAVERSE_RETRACT = 0.5 #mm of filament to retract when traversing longer distances
        self.MAX_FEED_TRAVERSE = 10 # max mm to move without lifting the head
        self.MAX_EXTRUDE_SPEED = 100 #mm/min max speed to move filament
        self.Z_CLEARANCE = 10.0 #mm to move Z up
        self.APPROACH_FR = 1500 #mm/min aproach feedrate
    
    def zipVariables_gen(inputLists, repeat=False):
        if iter(inputLists) is iter(inputLists):
            # Tests if inputLists is a generator
            iterType = tuple
        else:
            iterType = type(inputLists)
        variableGenerators = list(map(itertools.cycle, inputLists))
            
        while 1:
            for _ in max(inputLists, key=len):
                try:
                     # This is the logic for a namedtuple
                    yield iterType(*list(map(next, variableGenerators)))
                except Exception:
                    yield iterType(list(map(next, variableGenerators)))
            if not repeat:
                break
    
    for key, value in data.items():
            setattr(self, key, value)    
    
    LayerParams = namedtuple('LayerParams', 'infillShiftX infillShiftY infillAngle \
                                            numShells layerHeight pathWidth trimAdjust')            
    _layerParameters = LayerParams(infillShiftX, infillShiftY, infillAngleDegrees, numShells,
                       layerHeight, pathWidth, trimAdjust)
    
    def layerParameters():
        return zipVariables_gen(_layerParameters, repeat=True)
    
    PartParams = namedtuple('PartParams', 'solidityRatio printSpeed shiftX shiftY numLayers')
    everyPartsParameters = zipVariables_gen(PartParams(
                              solidityRatio, printSpeed, shiftX, shiftY,
                              numLayers))
    
    def run(self):
        startTime = time.time()
        print('\nGenerating code, please wait...')
        
        fig = fg.Figura(self.outline)
        
        with open(self.outputSubDirectory+'\\'+self.outputFileName, 'w') as f:      
            for string in fig.masterGcode_gen():
                f.write(string)
        
        endTime = time.time()
        print('\nCode generated.')
        print('Done writting: ' + self.outputFileName + '\n')
        print('{:.2f} total time'.format(endTime - startTime))
        
        if c.LOG_LEVEL < c.logging.WARN:
            with open(self.outputSubDirectory+'\\'+self.outputFileName, 'r') as test,\
                 open(self.outputSubDirectory+'\\SAVE_master.gcode') as master:
                testLines = test.readlines()
                masterLines = master.readlines()
                i = 0
                numDiffs = 0
                for t,m in zip(testLines, masterLines):
                    i += 1
                    if t != m:
                        numDiffs += 1
                        if i%10**round(np.log10(i*2)-1)<1:
                            print('Diff at line: ', i)
                            print('Test: ' + t)
                            print('Master: ' + m)
                            print('---------------------------\n')
            print('\nTotal number of differences: ', numDiffs)
        
     
                              
if __name__ == '__main__':
    param.run()
    
 
    