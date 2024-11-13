"""
Problem Statement

Simulate rolling two dice, three times. Prints the results of each die roll. 
This program is used to show how variable scope works.
"""

import random
def roll_dice():
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  
    return die1, die2

def simulate_rolls():
    for i in range(3): #roll dice three times
        die1, die2 = roll_dice()
        print(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}")

simulate_rolls()
