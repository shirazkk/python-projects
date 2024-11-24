
"""
Problem Statement

Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

Here's two sample runs (user input is in bold italics):

How tall are you? 100

You're tall enough to ride!

How tall are you? 10

You're not tall enough to ride, but maybe next year!

(For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)
"""

MIN_HEIGHT = 50
def tall_enough_to_ride():
    while True:
        user_input = input("How tall are you?: ")
        try:
            user_height = float(user_input) 
            if user_height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
                break
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function
tall_enough_to_ride()
