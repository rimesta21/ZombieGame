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
        self.name = "Random Zombie"
        
    
    def takeTurn(self):
        print("Random Zombie is up.")
        while self.firstRoll or random.randint(0,1) == 1:
            if not self.firstRoll:
                print("Random Zombie decides to go again!")                
            self.firstRoll = False
            self.turn.getDice()
            result = self.turn.rollDice("Random Zombie")
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        print("Looks like Random Zombie is unlucky.")
                        return 0
                else:
                    self.brains += 1
        print("Random Zombie decided not to go again.")
        temp = self.reset()
        return temp
            
            
            