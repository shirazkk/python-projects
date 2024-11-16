
import random

def play_game():
    print("""Welcome to the High-Low Guessing Game!
-----------------------------------------""")

    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your randomly selected number is: {player_number}")

    while True:
        player_guess = input("Do you think your number is higher or lower than the computer's number? Type 'higher' or 'lower': ").lower()
        if player_guess in ["higher", "lower"]:
            break  
        else:
            print("Invalid input! Please type 'higher' or 'lower' to make a guess.")

    if (player_number > computer_number and player_guess == "higher") or (player_number < computer_number and player_guess == "lower"):
        print(f"Congratulations! You guessed correctly; you win! The computer's number was {computer_number}.")
    else:
        print(f"Sorry, your guess was incorrect; you lose! The computer's number was {computer_number}.")


play_game()