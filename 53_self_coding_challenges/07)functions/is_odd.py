"""
Problem Statement
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd
"""

def even_odd_sequence():
    
    for num in range(10, 20):  # Iterate from 10 to 19
        if num % 2 == 0:  # Check if the number is even
            print(f"{num} even", end=" ")
        else:  # Otherwise, it's odd
            print(f"{num} odd", end=" ")

# Call the function
even_odd_sequence()
