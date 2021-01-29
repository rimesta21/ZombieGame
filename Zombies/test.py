# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:26:44 2021

@author: rimes
"""


from Dice.redDie import redDie
from Dice.greenDie import greenDie
from Dice.baseDice import baseDice

if __name__ == "__main__":
    red = greenDie()
    print(red.getFace())