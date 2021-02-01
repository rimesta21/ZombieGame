# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:28:48 2021

@author: rimes
"""

from Zombies.randomZombie import randomZombie
from Zombies.inTheMomentZombie import inTheMomentZombie
from Zombies.carefulZombie import carefulZombie
from Zombies.twoBrainZombie import twoBrainZombie
from Zombies.twoShotgunZombie import twoShotgunZombie
from Zombies.userZombie import userZombie
import time

def printScores(scores, counter):
    if not counter:
        print("Final scores are: ")
    else:
        print("Scores at the end of round " + str(counter) + " are:")
    for i in list(scores.keys()):
        print(i.name + ": " + str(scores[i]))
    time.sleep(8)
    print()

if __name__ == "__main__":
    randZom = randomZombie()
    inMomentZom = inTheMomentZombie()
    carfulZom = carefulZombie()
    twoBrainZom = twoBrainZombie()
    twoShotZom = twoShotgunZombie()
    name = input("Please enter your Zombie name.\n")
    print()
    user = userZombie(name)
    scores = {randZom: 0, inMomentZom : 0, carfulZom : 0, twoBrainZom : 0,
              twoShotZom : 0, user : 0}
    maxScore = 0
    winner = None
    counter = 1
    while maxScore < 13:
        for i in list(scores.keys()):
            temp = i.takeTurn()
            scores[i] += temp
            print(i.name + " ended their turn with a score of " + str(temp) + ".")
            if i != user:
                time.sleep(8)
            else:
                time.sleep(2)
            print()
            if scores[i] > maxScore:
                maxScore = scores[i]
                winner = i
        printScores(scores, counter)
        counter += 1
            
    print("Looks like " + winner.name + " got to 13 first. Everyone else has one more chance!")
    
    for i in list(scores.keys()):
        if i == winner:
            continue
        temp = i.takeTurn()
        scores[i] += temp
        print(i.name + " ended their turn with a score of " + str(temp) + ".")
        time.sleep(8)
        print()
     
    winners = [winner]
    for i in list(scores.keys()):
        if scores[i] > maxScore:
            maxScore = scores[i]
            winners = [i]
        elif scores[i] == maxScore and i not in winners:
            winners.append(i)
    
    if len(winners) > 1:
        print("Looks like we have a tie!", end =" ")
        for i in winners:
            print(i.name, end = ", ")
        print("will go again.")
        maxScore = 0
        winner = None
        for i in winners:
            temp = i.takeTurn()
            scores[i] += temp
            print(i.name + " ended their turn with a score of " + str(temp) + ".")
            time.sleep(8)
            print()
            if temp > maxScore:
                maxScore = scores[i]
                winner = i
    print("We have a winner! Congratulations " + winner.name + "!! Looks like" +
          " you're the most fit zombie.")   
    
    printScores(scores, False)
    
    
    

    