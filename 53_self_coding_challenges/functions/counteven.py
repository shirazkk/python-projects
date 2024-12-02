"""
Problem Statement
Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!
"""

def count_even():
    """
    This function populates a list with integers entered by the user
    and then counts and prints the number of even numbers in the list.
    """
    numbers = []  # List to store user-entered integers

    # Populate the list with user input
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Exit loop if the input is empty
            break
        try:
            number = int(user_input)  # Convert input to an integer
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Handle non-integer inputs

    # Count even numbers
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"The number of even numbers in the list is: {even_count}")

count_even()