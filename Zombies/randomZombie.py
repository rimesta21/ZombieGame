# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:51:42 2021

@author: rimes
"""


from Zombies.Zombie import Zombie
import random

class randomZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.firstRoll = True
    
    
    def takeTurn(self):
        while self.firstRoll or random.randint(0,1) == 1:
            self.firstRoll = False
            self.turn.getDice()
            result = self.turn.rollDice()
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        return 0
                else:
                    self.brains += 1
        self.firstRoll = True
        self.shotgun = 0
        self.brains, temp = 0, self.brains 
        return temp
            
            
            