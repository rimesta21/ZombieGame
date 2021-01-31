# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:30:10 2021

@author: rimes
"""


from abc import ABC
from Zombies.Turn import Turn

class Zombie(ABC):
    def __init__(self):
        self.shotgun = 0
        self.brains = 0
        self.turn = Turn()
        self.firstRoll = True
        
    def takeTurn(self):
        pass
    
    def reset(self):
        self.firstRoll = True
        self.shotgun = 0
        self.brains, temp = 0, self.brains 
        self.turn.reset()
        return temp
    
    
    def printInfo(self):
        print("Shotguns: " + str(self.shotgun))
        print("Brains: " + str(self.brains))
    