"""
Problem Statement

Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
"""

def get_first_element(list_items=None):
    
    list_items = []

    while True:
        try:
            n = int(input("How many elements do you want to enter? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for _ in range(n):
        user_input = input("Please enter an element for the list: ")
        list_items.append(user_input)

    if list_items:
        print("First element in the list:", list_items[0])
    else:
        print("The list is empty!")

    print("Final list:", list_items)

get_first_element()




