
"""
Problem Statement

Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
"""

MAX_LENGTH = 3
def shorten_list(input_list=None):
    if input_list is None:
        input_list = ["a", "b", "c", "d", "e", 2, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"List before shortening: {input_list}")

    while len(input_list) > MAX_LENGTH:
        removed_element = input_list.pop()
        print(f"Removed element: {removed_element}")

    print(f"Final shortened list: {input_list}")

shorten_list()
