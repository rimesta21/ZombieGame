# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:34:28 2021

@author: rimes
"""

import random
from Zombies.Dice.greenDie import greenDie
from Zombies.Dice.redDie import redDie
from Zombies.Dice.yellowDie import yellowDie

class Turn:
        
    def __init__(self):
        self.cup = {"red" : 3, "yellow" : 3, "green" : 3}
        self.onHand = []
                    
        
    def getDice(self):
        while len(self.onHand) < 3:
            color = list(self.cup.keys())[random.randint(0,2)]
            if(self.cup[color] != 0):
                self.cup[color] -= 1
                self.onHand.append(color)
    
    def rollDice(self, zombie):
        result = []
        temp = list(self.onHand)
        for i in temp:
            if i == "red":
                die = redDie()
            elif i == "yellow":
                die = yellowDie()
            else:
                die = greenDie()
            face = die.getFace()
            print(zombie + " got a " + i + " die and rolled " + face + ".")
            if face != "footstep":
                self.onHand.remove(i)
                result.append(face)
        return result
                
    def reset(self):
        self.cup = {"red" : 3, "yellow" : 3, "green" : 3}
        self.onHand = []
                
        