# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:15:41 2021

@author: rimes
"""


from Zombies.Zombie import Zombie
import random

class inTheMomentZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.numTimes = random.randint(1,4)
        self.name = "In the Moment Zombie"
        
    def takeTurn(self):
        print("In the Moment Zombie is up.")
        j = 0
        while j < self.numTimes and self.shotgun < 2:
            if not self.firstRoll:
                print("In the Moment Shotgun Zombie decides to go again!")
            self.firstRoll = False
            j += 1
            self.turn.getDice()
            result = self.turn.rollDice("In the Moment Zombie")
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        print("Looks like In the Moment Zombie is unlucky.")
                        return 0
                else:
                    self.brains += 1
        print("In the Moment Zombie decided not to go again.")
        temp = self.reset()
        self.numTimes = random.randint(1,4)
        return temp