# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:57:12 2016

@author: adiebold
"""

from tkinter import *
from tkinter import ttk

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.animation as animation


data = []

with open("data_points.txt", 'r') as f:
    for line in f:
        data.append(line)   
   
for x in range(0,len(data)):   
    data[x] = data[x].replace("[", "")
    data[x] = data[x].replace("]", "")
    data[x] = data[x].replace("'", "")
    data[x] = data[x].replace(" ", "")
    data[x] = data[x].replace("\n", "")
    data[x] = data[x].split(",")
    for y in range(0,len(data[x])):
        data[x][y] = float(data[x][y])

x = []
y = []
z = []
for entry in data:
    tempx = []
    tempy = []
    tempz = []
    tempx.append(entry[0])
    tempx.append(entry[3])
    tempy.append(entry[1])
    tempy.append(entry[4])
    tempz.append(entry[2])
    tempz.append(entry[5])
    x.append(tempx)
    y.append(tempy)
    z.append(tempz)
    
class Three_D:
    
    def __init__(self, start, end, x, y, z):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.xar = x
        self.yar = y
        self.zar = z
        
        self.colors = []
        
        color_num = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        color_num2 = ['0','8']
        for one in color_num:
            for two in color_num2:
                for three in color_num2:
                    for four in color_num2:
                        for five in color_num2:
                            for six in color_num:
                                curr_color = '#' + one + two + three + four + five + six
                                self.colors.append(curr_color)
            
        for num in range(start, end):
            num_color = num%len(self.colors)
            self.ax.plot_wireframe(self.xar[num], self.yar[num], self.zar[num], color=self.colors[num_color])
            
        plt.show()
        
    def update(self, start, end):
        
        ax.clear()
        
        for num in range(start, end):
            num_color = num%len(colors)
            self.ax.plot_wireframe(self.xar[num], self.yar[num], self.zar[num], color=self.colors[num_color])
        
class SceneView(openglGUI.glGuiPanel):
    def __init__(self, parent):
        super(SceneView, self).__init__(parent)        
    
    
def error_box():
        
    popup = Tk()
    popup.title("Error")
    
    msg = Label(popup, text="Error: End value cannot be less than Start value")
    msg.pack(side="top", fill="x", pady=10)
    
    buttonDismiss = Button(popup, text="Dismiss", command = popup.destroy)
    buttonDismiss.pack()
    
    popup.mainloop()
        
def create_plot(start, end, x, y, z):
    if(end >= start):
        model = Three_D(start, end, x, y, z)
    else:
        error_box()

root = Tk()

root.title('3D Model')

labelPoints = Label(root, text="Choose the start and end numbers of the graph")
labelPoints.pack()

labelStart = Label(root, text="Start")
labelStart.pack(side=LEFT)

scaleStart = Scale(root, from_=0, to=len(x), length=500, tickinterval=100)
scaleStart.pack(side=LEFT)

labelEnd = Label(root, text="End")
labelEnd.pack(side=LEFT)

scaleEnd = Scale(root, from_=0, to=len(x), length=500, tickinterval=100)
scaleEnd.pack(side=LEFT)

buttonSubmit = Button(root, text="Create Graph", command=lambda: create_plot(scaleStart.get(), scaleEnd.get(), x, y, z))
buttonSubmit.pack()

#buttonUpdate = Button(text="Update Graph", command=lambda: )

root.mainloop()
