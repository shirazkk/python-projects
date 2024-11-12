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

def Guess_Number():
    wins = 0
    losses = 0
    
    def play_game():
        computer_generated = random.randint(0, 5)
        chances = 5
        while chances > 0:
            print(f"You have only {chances} chances to guess a number.\n")
            try:
                user_guess = int(input(f"Guess a number between 0 to 5.\n"))
                
                if user_guess > computer_generated:
                    print("Your guess is too high.\n")
                elif user_guess < computer_generated:
                    print("Your guess is too low.\n")
                else:
                    print(f"Congrats! You win! The number was: {computer_generated}\n")
                    return True
                chances -= 1

                if chances == 0:
                    print(f"Sorry! You've run out of chances. The correct number was: {computer_generated}\n")
                    return False
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 5.\n")
        
    while True:
        play_game_result = play_game()
        if play_game_result:
            wins += 1
        else:
            losses += 1
        
        print(f"\nGames Played: Wins: {wins}, Losses: {losses}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

Guess_Number()
