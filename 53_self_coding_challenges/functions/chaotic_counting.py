"""
Problem Statement
Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.
"""

import random

# Likelihood that the done() function will return True
DONE_LIKELIHOOD = 0.2

def done() -> bool:
    """
    Returns True with a likelihood of DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Counts from 1 to 10, but stops prematurely if done() returns True.
    """
    for i in range(1, 11):  # Loop from 1 to 10
        if done():
            return  # Exit the function if done() returns True
        print(i, end=" ")  # Print the current number

def main():
    """
    Main function to demonstrate chaotic counting.
    """
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Run the main function
if __name__ == "__main__":
    main()
