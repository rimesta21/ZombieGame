# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:15:41 2021

@author: rimes
"""


from Zombies.Zombie import Zombie
import random

class inTheMomementZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.numTimes = random.randint(1,4)
        
    def takeTurn(self):
        i = 0
        while i < self.numTimes and self.shotguns < 2:
            i += 1
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
            
        self.shotgun = 0
        self.brains, temp = 0, self.brains 
        self.numTimes = random.randint(1,4)
        return temp