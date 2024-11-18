"""
Problem Statement

Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
"""

def calculate_quotient_and_remainder():
    dividend: int = int(input("Enter the dividend (the number to be divided): "))
    divisor: int = int(input("Enter the divisor (the number to divide by): "))

    remainder: int = dividend % divisor
    quotient: int = dividend // divisor
    
    print(f"The remainder when {dividend} is divided by {divisor} is {remainder}.")
    print(f"The quotient when {dividend} is divided by {divisor} is {quotient}.")

calculate_quotient_and_remainder()
