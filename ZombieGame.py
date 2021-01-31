# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:28:48 2021

@author: rimes
"""

from Zombies.randomZombie import randomZombie

if __name__ == "__main__":
    randZombie = randomZombie()
    print(randZombie.takeTurn())
    randZombie.printInfo()

    