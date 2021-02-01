# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:27:53 2021

@author: rimes
"""


from Zombies.Zombie import Zombie
import time

class userZombie(Zombie):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def takeTurn(self):
        print(self.name + " Zombie is up.")
        cont = 'y'
        while cont == 'y':
            if not self.firstRoll:
                print(self.name + " Zombie decides to go again!")
            self.firstRoll = False
            self.turn.getDice()
            result = self.turn.rollDice(self.name + " Zombie")
            for i in result:
                if i == "shotgun":
                    self.shotgun += 1
                    if self.shotgun == 3:
                        self.shotgun = 0
                        self.firstRoll = True
                        self.brains = 0
                        print("Looks like " + self.name + " Zombie is unlucky.")
                        return 0
                else:
                    self.brains += 1
            print("So far you ended with " + str(self.brains) + " brains and " +
                  str(self.shotgun) + " shotguns.")
            time.sleep(3)
            cont = input("You you like to go again? Press y for yes and anything else for no.\n")
        temp = self.reset()
        return temp