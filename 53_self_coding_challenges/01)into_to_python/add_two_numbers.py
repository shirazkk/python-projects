"""
Problem Statement

Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

01: Prompt the user to enter the first number.

02: Read the input and convert it to an integer.

03: Prompt the user to enter the second number.

04: Read the input and convert it to an integer.

05: Calculate the sum of the two numbers.

06: Print the total sum with an appropriate message.
"""

def main():
    input1:str=input("Enter the first number: ")
    input1:int=int(input1)
    input2:str=input("Enter the second number: ")
    input2:int=int(input2)
    sum:int=input1+input2
    return f"{input1} + {input2} = {sum}"
if __name__ == '__main__':
    result=main()
    print(result)