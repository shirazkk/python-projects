# Problem #1: List Practice
Now practice writing code with lists! Implement the functionality described in the comments below.

def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

- Print the length of the list.


- Add 'mango' at the end of the list.


- Print the updated list.


# Problem #2: Index Game

## Objective
Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

---

## Instructions

### 1. Initialize a List
- Create a list with at least 5 different elements.  
- These elements can be numbers, strings, or a mix of both.

### 2. Accessing Elements
Write a function that:
- Accepts a list and an index as inputs.
- Returns the element at the specified index.
- If the index is out of range, returns an appropriate message.

### 3. Modifying Elements
Write a function that:
- Accepts a list, an index, and a new value as inputs.
- Replaces the element at the specified index with the new value.
- If the index is out of range, returns an appropriate message.

### 4. Slicing the List
Write a function that:
- Accepts a list, a start index, and an end index as inputs.
- Returns a new list containing the elements from the start index up to (but not including) the end index.
- Handles cases where the indices are out of range.

### 5. Game Interaction
Create a simple text-based game that:
- Prompts the user to select an operation (`access`, `modify`, or `slice`).
- Asks for the necessary inputs (index, new value, etc.).
- Displays the result and the updated list.

---

## Example Use Case
- The user initializes a list: `[10, 20, 30, 40, 50]`.
- They select "access" and input `2`. The program returns `30`.
- They select "modify", input `3` and `99`. The updated list becomes `[10, 20, 30, 99, 50]`.
- They select "slice", input `1` and `4`. The program returns `[20, 30, 99]`.

Happy Coding! 🚀
