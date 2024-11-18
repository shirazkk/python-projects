"""
Problem Statement
Simulate rolling two dice, and prints results of each roll as well as the total.

"""

import random

number_of_sides: int = 6

def roll_dice():
    first_roll = random.randint(1, number_of_sides)
    second_roll = random.randint(1, number_of_sides)
    print(f"Dice have {number_of_sides} sides each.")
    print(f"First die: {first_roll}")
    print(f"Second die: {second_roll}")
    print(f"Total of two dice: {first_roll + second_roll}")

roll_dice()