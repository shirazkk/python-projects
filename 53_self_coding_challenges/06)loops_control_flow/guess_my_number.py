"""
Problem Statement

Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48
"""

import random
def guess_my_number():
    random_number = random.randint(0, 99)
    # print(random_number)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 99. Can you guess it?")
    
    while True:
        try:
            # Input validation and error handling
            user_input = input("Enter your guess (or type 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                print("Thanks for playing! Goodbye!")
                break
            
            user_guess = int(user_input)
            if user_guess < 0 or user_guess > 99:
                print("Please enter a number between 0 and 99.")
                continue
            
            # Compare guess with the random number
            if user_guess < random_number:
                print("Your guess is too low. Try again!")
            elif user_guess > random_number:
                print("Your guess is too high. Try again!")
            else:
                print(f"Congrats! You guessed the number: {random_number}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'quit' to exit.")

guess_my_number()
