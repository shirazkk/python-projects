# 2. Accessing Elements
# Write a function that:
# - Accepts a list and an index as inputs.
# - Returns the element at the specified index.
# - If the index is out of range, returns an appropriate message.

my_list = [42, "apple", 3.14, "banana", 100]

def access_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of range"

user_access=int(input("Enter the index you want to access: "))
print(access_element(my_list, user_access))

# 3. Modifying Elements
# Write a function that:
# - Accepts a list, an index, and a new value as inputs.
# - Replaces the element at the specified index with the new value.
# - If the index is out of range, returns an appropriate message.

my_list = [42, "apple", 3.14, "banana", 100]
def modify_list(my_list,index,new_value):
  try:
    my_list[index]=new_value
    return my_list
  except IndexError:
    return "Index out of range"

user_index=int(input("Enter the index you want to modify: "))
user_new_value=input("Enter the new value: ")

print(modify_list(my_list,user_index,user_new_value))


# 4. Slicing the List
# Write a function that:
# - Accepts a list, a start index, and an end index as inputs.
# - Returns a new list containing the elements from the start index up to (but not including) the end index.
# - Handles cases where the indices are out of range.

def slice_list(my_list,start_index,end_index):
  try:
    return my_list[start_index:end_index]
  except IndexError:
    return "Index out of range"

user_start_index=int(input("Enter the start index: "))
user_end_index=int(input("Enter the end index: "))

print(slice_list(my_list,user_start_index,user_end_index))


# 5. Game Interaction
# Create a simple text-based game that:
# - Prompts the user to select an operation (`access`, `modify`, or `slice`).
# - Asks for the necessary inputs (index, new value, etc.).
# - Displays the result and the updated list.

my_list = [42, "apple", 3.14, "banana", 100]
def game_interaction(my_list):
    while True:
        print("\nAvailable Operations: access | modify | slice | exit")
        user_choice = input("Select an operation: ").strip().lower()

        if user_choice == "access":
            user_access = int(input("Enter the index you want to access: "))
            print(access_element(my_list, user_access))
        elif user_choice == "modify":
            user_index = int(input("Enter the index you want to modify: "))
            user_new_value = input("Enter the new value: ")
            print(modify_list(my_list, user_index, user_new_value))
        elif user_choice == "slice":
            user_start_index = int(input("Enter the start index: "))
            user_end_index = int(input("Enter the end index: "))
            print(slice_list(my_list, user_start_index, user_end_index))
        elif user_choice == "exit":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

game_interaction(my_list)