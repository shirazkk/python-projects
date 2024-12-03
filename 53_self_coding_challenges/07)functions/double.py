"""
Problem Statement
Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
"""
def double(num:float) -> float:
    return num * 2

def main():
    num = float(input("Enter a number to double: "))
    result = double(num)
    print(f"The result of doubling {num} is: {result}")

if __name__ == "__main__":
    main()
