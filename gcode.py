# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 10:30:44 2015

Used creating all of the lines of Gcode.

@author: lvanhulle
"""

class Gcode:    
    
    def __init__(self, data):
        print("step 5")
        for key in data:
            setattr(self, key, data[key])

    def feedMove(endPoint, ommitZ, extrudeTo, printSpeed):
        if ommitZ:
            tempString = ('X{:.3f} Y{:.3f} E{:.3f}'.format(endPoint.x,
                          endPoint.y, extrudeTo))
        else:
            tempString = ('X{:.3f} Y{:.3f} Z{:.3f} E{:.3f}\n'.format(endPoint.x,
                          endPoint.y, endPoint.z, extrudeTo))
    
        return 'G01 ' + tempString + ' F{:.0f}\n'.format(printSpeed)                
    
    def rapidMove(endPoint, ommitZ):
        if ommitZ:
            return ('G00 X{:.3f} Y{:.3f} F{:.0f}\n'.format(endPoint.x, endPoint.y,
                    RAPID))
        else:
            return ('G00 X{:.3f} Y{:.3f} Z{:.3f} F{:.3f}\n'.format(endPoint.x, endPoint.y, endPoint.z,
                    RAPID))
                    
    def retractLayer(currentE, currentPoint):
        tempString = 'G1 E{:.3f} F{:.0f}\n'.format(currentE-TRAVERSE_RETRACT, MAX_EXTRUDE_SPEED)
        tempString += 'G00 Z{:.3f} F{:.0f}\n'.format(currentPoint.z+Z_CLEARANCE, RAPID)
        return tempString
        
    def approachLayer(lastE, startPoint):
        tempString = 'G1 Z{:.3f} F{:.0f} E{:.3f}\n'.format(startPoint.z+Z_CLEARANCE/2.0,
                        RAPID, lastE-TRAVERSE_RETRACT*0.75)
        tempString += 'G1 Z{:.3f} F{:.0f} E{:.3f}\n'.format(startPoint.z,
                        APPROACH_FR, lastE)
        return tempString
    
    def firstApproach(lastE, startPoint):
        return 'G1 Z{:.3f} F{:.0f} E{:.3f}\n'.format(startPoint.z, APPROACH_FR, lastE)
        
    def newPart(self):
        return 'G92 E0\n'
    
    def startGcode(self):
        with open(self.startEndSubDirectory + '\\' + self.start_Gcode_FileName) as startFile:
            lines = startFile.readlines()   
        tempString = ''
        for line in lines:
            tempString += str(line)
        return tempString
    
    def endGcode(self):
        with open(self.startEndSubDirectory + '\\' + self.end_Gcode_FileName) as endFile:
            lines = endFile.readlines()       
        tempString = ''
        for line in lines:
            tempString += str(line)
        return tempString