# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:34:28 2021

@author: rimes
"""

import random
from Dice import redDie, yellowDie, greenDie

class Turn:
        
    def __init__(self):
        self.cup = {"red" : 3, "yellow" : 3, "green" : 3}
        self.onHand = []
             
        
    def getDice(self, diceNum):
        while len(self.onHand) <= 3:
            color = list(self.cup.keys())[random.randint(0,2)]
            if(self.cup[color] != 0):
                self.cup[color] -= 1
                self.onHand.append(color)
    
    def rollDice(self):
        result = []
        for i in self.onHand:
            if i == "red":
                die = redDie()
            elif i == "yellow":
                die = yellowDie()
            else:
                die = greenDie()
                
            face = die.getFace()
            if face != "footstep":
                self.onHand.remove(i)
                result.append(i)
                
        return result