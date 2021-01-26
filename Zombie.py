# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:30:10 2021

@author: rimes
"""


from abc import ABC, abstractmethod
import Turn

class Zombie(ABC):
    def __init__(self):
        self.footsteps = 0
        self.shotguns = 0
        self.brains = 0
        self.turn = Turn()
        
    def takeTurn(self):
        pass
    
    
        
    