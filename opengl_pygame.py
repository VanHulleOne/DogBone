# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:29:57 2016

@author: adiebold
"""

#attempt at using opengl and pygame

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

data = []
counter = 0
layer_part = []

with open('data_points.txt', 'r') as f:
    for line in f:
        if 'start' in line:
            print('start ', counter)
            start = counter
        elif 'layer_number' in line:
            print(line)
            print(counter)
            layer_part.append([line.split(':')[1], line.split(':')[3], start, counter])
        else:
            data.append(line)      
            data[counter] = data[counter].split(',')
            for y in range(0,len(data[counter])):
                data[counter][y] = float(data[counter][y])
            data[counter] = [tuple(data[counter][0:3]), tuple(data[counter][3:])]
            counter += 1
            
#print(data[0])
#print(type(data[0][0]))
    

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )
    
edges = (
    (0,1),    
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

#edges = []
#
#for x, line in enumerate(data):
#    edges.append()
    
def Cube():
    glBegin(GL_LINES)
#    for edge in edges:
#        print('line')
#        for vertex in edge:
#            glVertex3fv(vertices[vertex])
#            print(vertices[vertex])
    for line in data:
#        print('line')
        for point in line:
            glVertex3f(point[0], point[1], point[2])
#            print(point)
    glEnd()
    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0) #187
    
    glTranslatef(-112.0,-40.0, -500)
    
    glRotatef(0, 0, 1, 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-15,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(15,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,15,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-15,0)
                if event.key == pygame.K_a:
                    glRotatef(15,0,1,0)
                if event.key == pygame.K_d:
                    glRotatef(-15,0,1,0)
                if event.key == pygame.K_w:
                    glRotatef(15,1,0,0)
                if event.key == pygame.K_s:
                    glRotatef(-15,1,0,0)
                if event.key == pygame.K_q:
                    glRotatef(15,0,0,1)
                if event.key == pygame.K_e:
                    glRotatef(-15,0,0,1)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,15.0)
                if event.button == 5:
                    glTranslatef(0,0,-15.0)
        
        glRotatef(0,0,0,0)        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)
        
main()