# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:08:21 2021

@author: rimes
"""


from Zombies.Zombie import Zombie

class twoBrainZombie(Zombie):
    def __init__(self):
        super().__init__()
        
    def takeTurn(self):
        while self.brains < 2:
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
        return temp