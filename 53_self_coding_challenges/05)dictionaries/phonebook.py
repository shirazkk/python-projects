"""
Problem Statement

In this program we show an example of using dictionaries to keep track of information in a phonebook.

"""

print("Welcome to the Phonebook Program!")
print("Enter names and phone numbers. To stop, leave the name blank and press Enter.\n")

phonebook = {}
def PhoneBook():
    while True:
        try:
            name = input("Enter a name: ").strip()
            if not name:
                break
            if not name.isalpha():
                raise ValueError("Name must only contain alphabetic characters.")
            
            number = input(f"Enter the phone number for {name}: ").strip()
            if not number.isdigit():
                raise ValueError("Phone number must only contain digits.")
            
            phonebook[name] = int(number)
            print(f"{name} added with phone number {number}.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} --> {number}")

PhoneBook()
