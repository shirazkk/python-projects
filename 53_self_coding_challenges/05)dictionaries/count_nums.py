

from collections import Counter

def get_user_input():
    user_list = []
    while True:
        try:
            user_input = input("Enter a number: ")
            if not user_input:
                break
            user_list.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter a number.")

    num_counts = Counter(user_list)
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

get_user_input()