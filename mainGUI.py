# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:30:29 2016

@author: lvanhulle
"""

import Tkinter

class mainGUI(Tkinter.Tk):
    def __inti__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        pass
    
if __name__ == "__main__":
    app = mainGUI(None)
    app.title('Hello World')
    app.mainloop()