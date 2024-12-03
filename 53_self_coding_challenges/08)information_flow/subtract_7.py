"""
Problem Statement

Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
"""

def subtract_seven(num:int)-> int:
    return num - 7  # Subtract 7 from the number

def main():
    num = int(input("Enter a number: "))  # Get the number from the user
    result = subtract_seven(num)  # Call the subtract_seven function
    print(f"Result after subtracting 7: {result}")  # Print the result

if __name__ == "__main__":
    main()
