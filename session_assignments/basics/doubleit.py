"""
Problem Statement

Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128

Note that:

2 doubled is 4

4 doubled is 8

8 doubled is 16

and so on.

We stop at 128 because that value is greater than 100.
"""

def double_it():
  try:
    user_input:int = int(input("Enter a number: "))
   
    

    if user_input <=0:
        print("Invalid input. Please enter a positive number.")
    elif user_input > 100:
        print("Number is too large. Please enter a number less than or equal to 100.")
        return
    

    while user_input <= 100:
     print(user_input)
     user_input *= 2
     
  except ValueError:
    print("Invalid input. Please enter a number.")

double_it()