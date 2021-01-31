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
        print("Two Brain Zombie is up.")
        while self.brains < 2:
            if not self.firstRoll:
                print("Two Brain Shotgun Zombie decides to go again!")
            self.firstRoll = False
            self.turn.getDice()
            result = self.turn.rollDice("Two Brain Zombie")
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        print("Looks like Two Brain Zombie is unlucky.")
                        return 0
                else:
                    self.brains += 1
        print("Two Brain Zombie decided not to go again.")
        temp = self.reset()
        return temp