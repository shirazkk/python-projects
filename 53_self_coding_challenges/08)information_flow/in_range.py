"""
Problem Statement
Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n:int, low:int, high:int)-> int:
    return low <= n <= high

# Example usage
def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))
    if in_range(n, low, high):
        print(f"{n} is in the range {low} to {high}.")
    else:
        print(f"{n} is not in the range {low} to {high}.")

if __name__ == "__main__":
    main()
