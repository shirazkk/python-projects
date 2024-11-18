
"""
Problem Statement
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""


INCHES_PER_FOOT = 12 
def convert_feet_to_inches(feet:float)->float:
    inches = feet * INCHES_PER_FOOT
    return inches

feet_input:float = float(input("Enter the number of feet to convert into inches: "))
resulting_inches:float = convert_feet_to_inches(feet_input)

print(f"{feet_input} feet is equal to {resulting_inches} inches.")
