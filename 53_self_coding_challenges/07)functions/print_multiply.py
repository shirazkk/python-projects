"""
Problem Statement
Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

Here's a sample run of the program (user input is in blue):

Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!
"""

def print_multiple(message, repeats):
    """
    This function prints the given message the specified number of times.
    """
    for _ in range(repeats):
        print(message)

def main():
    """
    Main function to prompt the user for a message and number of repeats,
    then call print_multiple() to print the message.
    """
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

# Call the main function
if __name__ == "__main__":
    main()
