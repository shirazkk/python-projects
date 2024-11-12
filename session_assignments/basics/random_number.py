"""
Problem Statement

Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers

81 76 70 1 27 63 96 100 32 92
"""

import random

def print_random_numbers():
    for _ in range(10):
        
        print(random.randint(1, 100), end=' ')

print_random_numbers()