# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:51:21 2021

@author: rimes
"""

from Zombies.Dice.baseDice import baseDice

class yellowDie(baseDice):
    def __init__(self):
        baseDice.__init__(self, ["footstep", "shotgun", "brains", "footstep", "shotgun", "brains"])