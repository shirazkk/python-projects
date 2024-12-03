"""
Problem Statement
Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

"""

def print_ones_digit(num:int):
  
    ones_digit = num % 10  # Use module to get the ones digit
    print(f"The ones digit is {ones_digit}")

def main():

    num:int = int(input("Enter a number: "))  # Prompt the user for an integer
    print_ones_digit(num)  # Call the function to print the ones digit

# Call the main function
if __name__ == "__main__":
    main()
