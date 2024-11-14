"""
Milestone #1: Generate the random numbers
Generate the random numbers for you and the computer. For now, print both of them out to help you test the logic in later milestones.
"""

import random

print("""Welcome to the High-Low Game!
--------------------------------""")

user_number:int=random.randint(1,100)
computer_number:int=random.randint(1,100)
print(f"Your number is {user_number}")
print(f"The computer's number is {computer_number}")
