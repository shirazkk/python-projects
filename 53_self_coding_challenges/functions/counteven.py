def count_even():
    """
    This function asks the user to enter integers, stores them in a list,
    and then counts and prints the number of even numbers.
    """
    numbers = []  # To store the integers

    # Get input from the user
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop if input is empty
            break
        numbers.append(int(user_input))  # Add the number to the list

    # Count even numbers
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1

    print(f"The number of even numbers is: {even_count}")

count_even()