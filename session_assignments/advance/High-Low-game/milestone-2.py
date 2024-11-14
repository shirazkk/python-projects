"""
Milestone #2: Get the user choice
Get user input for their choice of whether they think their number is higher or lower than the computer's number.
"""

import random

print("""Welcome to the High-Low Game!
--------------------------------""")

user_number:int=random.randint(1,100)
computer_number:int=random.randint(1,100)
print(f"Your number is {user_number}")
print(f"The computer's number is {computer_number}")
user_guess=input("Do you think your number is higher or lower than the computers(high/low)?: ")