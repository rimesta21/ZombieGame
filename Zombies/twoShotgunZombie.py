# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:13:05 2021

@author: rimes
"""


from Zombies.Zombie import Zombie

class twoShotgunZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.name = "Two Shotgun Zombie"
        
    def takeTurn(self):
        print("Two Shotgun Zombie is up.")
        while self.shotgun < 2:
            if not self.firstRoll:
                print("Two Shotgun Zombie decides to go again!")
            self.firstRoll = False
            self.turn.getDice()
            result = self.turn.rollDice("Two Shotgun Zombie")
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        print("Looks like Two Shotgun Zombie is unlucky.")
                        return 0
                else:
                    self.brains += 1
        print("Two Shotgun Zombie decided not to go again.")
        temp = self.reset()
        return temp