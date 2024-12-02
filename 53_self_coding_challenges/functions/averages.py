def find_average(num1: float, num2: float) -> float:
    """
    This function takes two numbers as input and returns their average.
    """
    average = (num1 + num2) / 2
    return average

# Example usage:
number1: float = float(input("Enter the first number: "))
number2: float = float(input("Enter the second number: "))

average: float = find_average(number1, number2)
print(f"The average of {number1} and {number2} is {average}.")
