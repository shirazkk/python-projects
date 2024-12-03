"""
Problem Statement
Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
"""
def double(num):
    """
    This function returns the result of multiplying the input number by 2.
    """
    return num * 2

def main():
    """
    Main function to get input from the user, call double(), and print the result.
    """
    num = float(input("Enter a number to double: "))
    result = double(num)
    print(f"The result of doubling {num} is: {result}")

# Call the main function
if __name__ == "__main__":
    main()
