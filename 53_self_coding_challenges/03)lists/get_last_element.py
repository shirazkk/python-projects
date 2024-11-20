
"""
Problem Statement

Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""


def get_last_element(list_items=None):
    
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
        print("last element in the list:", list_items[-1])
    else:
        print("The list is empty!")

    print("Final list:", list_items)

get_last_element()

