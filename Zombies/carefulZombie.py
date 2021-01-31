# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:16:32 2021

@author: rimes
"""


from Zombies.Zombie import Zombie

class carefulZombie(Zombie):
    def __init__(self):
        super().__init__()
        
    def takeTurn(self):
        print("Careful Zombie is up.")
        while self.shotguns <= self.brains:
            if not self.firstRoll:
                print("Careful Zombie decides to go again!") 
            self.firstRoll = False
            self.turn.getDice()
            result = self.turn.rollDice("Careful Zombie")
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        print("Looks like Careful Zombie is unlucky.")
                        return 0
                else:
                    self.brains += 1
        print("Careful Zombie decided not to go again.")
        temp = self.reset()
        return temp