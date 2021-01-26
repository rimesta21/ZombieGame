# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:34:28 2021

@author: rimes
"""


class Turn:
    colors = ["red", "yellow", "green"]
    
    def __init__(self):
        self.cup = {"red" : 3, "yellow" : 3, "green" : 3}
        self.onHand = []
        self.result = []
        
    def getDice(self, diceNum):
        for i in range(diceNum, 3):
            