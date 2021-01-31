# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:52:33 2021

@author: rimes
"""

from Zombies.Dice.baseDice import baseDice

class greenDie(baseDice):
    def __init__(self):
        baseDice.__init__(self, ["footstep", "shotgun", "brains", "footstep", "brains", "brains"])