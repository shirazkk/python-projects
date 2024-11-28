"""
Problem Statement
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128
"""

MAXIMUM_NUMBER: int = 100

def double_it():
    while True:  # Keep prompting until a valid number is entered
        try:
            user_number: int = int(input("Enter a number to start doubling: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nStarting with {user_number}, doubling until it reaches {MAXIMUM_NUMBER} or more:\n")
    
    while user_number < MAXIMUM_NUMBER:
        doubled_number: int = user_number * 2
        print(f"Doubled value: {doubled_number}")
        user_number = doubled_number
    
    print("\nDoubling process complete. Exceeded or reached the maximum limit!")

# Call the function
double_it()
