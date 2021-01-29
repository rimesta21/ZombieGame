# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:41:38 2021

@author: rimes
"""


from Dice.baseDice import baseDice

class redDie(baseDice):
    def __init__(self):
        baseDice.__init__(self, ["footstep", "shotgun", "brains", "footstep", "shotgun", "shotgun"])
        
    
