# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:12:35 2016

@author: adiebold
"""

import figura as fg
import time
from parameters import Parameters
import json
import os
import doneShapes as ds
import constants as c

class Main:
  
    main_data = {}
    outline_options = {}
    trimAdjust_options = {}
    
    def __init__(self, name):
        with open(name, 'r') as fp:
            self.main_data = json.load(fp)
        self.outline_options["regularDogBone"] = ds.regularDogBone()
        self.trimAdjust_options["EPSILON"] = c.EPSILON
        for key in self.trimAdjust_options:              
            if key in self.main_data["trimAdjust"][0]:
                option = self.trimAdjust_options[key]
                if any(char.isdigit() for char in self.main_data["trimAdjust"][0]):
                    number = int(''.join(t for t in self.main_data["trimAdjust"][0] if t.isdigit()))
                    option *= number
                self.main_data["trimAdjust"][0] = option
            break
        print("step 1")
        self.pr = Parameters(self.main_data)
    
    def run(self):
        print("step 3")
        startTime = time.time()
        print('\nGenerating code, please wait...')
        
        fig = fg.Figura(self.outline_options[self.pr.outline], self.pr.param_data)
        
        with open(self.pr.outputSubDirectory+'\\'+self.pr.outputFileName, 'w') as f:      
            for string in fig.masterGcode_gen():
                f.write(string)
        
        endTime = time.time()
        print('\nCode generated.')
        print('Done writting: ' + self.pr.outputFileName + '\n')
        print('{:.2f} total time'.format(endTime - startTime))
        """
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
        """
            
            