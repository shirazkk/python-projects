
"""
Problem Statement

This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
"""

user_list = []
num_dict = {}

def get_user_input():
    while True:
        try:
            user_input = input("Enter a number: ")
            if not user_input:
                break
            user_list.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter a number.")

    for num in user_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    for num1 in num_dict:
        print(f"{num1} appears {num_dict[num1]} times.")

get_user_input()
