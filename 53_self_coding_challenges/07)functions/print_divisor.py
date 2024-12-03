"""
Problem Statement
Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

Here's a sample run (user input is in blue):

Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12
"""

def print_divisors(num):

    divisors = []  # List to store divisors
    
    # Find divisors from 1 to num
    for i in range(1, num + 1):
        if num % i == 0:  # Check if i is a divisor of num
            divisors.append(i)
    
    # Print the divisors
    print("Here are the divisors of", num)
    print(" ".join(map(str, divisors)))

def main():
    """
    Main function to get user input and call print_divisors().
    """
    num = int(input("Enter a number: "))  # Get the number from the user
    print_divisors(num)  # Call the helper function to print divisors

# Call the main function
if __name__ == "__main__":
    main()
