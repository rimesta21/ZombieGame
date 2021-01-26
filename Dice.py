# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:39:16 2021

@author: rimes
"""


from abs import ABC
import random


class Dice(ABC):
    def __init__(self):
        self.faces = {}
        
    def getFace(self):
        return self.faces[random.randint(0, 6)]