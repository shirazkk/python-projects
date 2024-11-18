"""
Problem Statement

Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]
"""



def get_doubled_list(numbers: list[int]) -> list[int]:
    doubled_numbers = []
    for num in numbers:
        doubled_numbers.append(num * 2)
    return doubled_numbers

def main():
    list_of_numbers: list[int] = [1, 2, 3, 4, 5]
    doubled_list = get_doubled_list(list_of_numbers)
    print(doubled_list)

if __name__ == '__main__':
    main()



