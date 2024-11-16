import random

NUM_ROUNDS = 5

def play_game():
    print("""Welcome to the High-Low Guessing Game!
-----------------------------------------""")

    while True:
        player_score = 0

        for round_number in range(1, NUM_ROUNDS + 1):
            print(f"Round {round_number} of {NUM_ROUNDS}")
            print("-" * 30)

            player_number = random.randint(1, 100)
            computer_number = random.randint(1, 100)

            print(f"Your randomly selected number is: {player_number}")

            while True:
                player_guess = input("Do you think your number is higher or lower than the computer's number? Type 'higher' or 'lower': ").strip().lower()
                if player_guess in ["higher", "lower"]:
                    break
                else:
                    print("Invalid input! Please type 'higher' or 'lower' to make a guess.")

            if (player_number > computer_number and player_guess == "higher") or (player_number < computer_number and player_guess == "lower"):
                print(f"Congratulations! You guessed correctly; you win! The computer's number was {computer_number}.")
                player_score += 1
            else:
                print(f"Sorry, your guess was incorrect; you lose! The computer's number was {computer_number}.")

            print(f"Your current score: {player_score}")
            print()

        print("Game Over!")
        print(f"Your final score: {player_score}")

        if player_score == NUM_ROUNDS:
            print("Wow! You played perfectly!")
        elif player_score >= NUM_ROUNDS // 2:
            print("Good job, you played really well!")
        else:
            print("Better luck next time!")

        play_again = input("Do you want to play again? Type 'yes' or 'no': ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

play_game()
