import time
fruits: dict[str, float] = {
    "apple": 1.0,
    "banana": 2.0,
    "orange": 2.4,
    "grape": 1.5,
    "mango": 1.1
}
def Pop_Up_Shop():
    total_cost:float = 0.0
    print("Welcome to the Fruit Shop!")
    print("Here is the price of each fruit (per unit):")
    for fruit, price in fruits.items():
        print(f". {fruit.title()}: ${price:.2f}")

    print("\nPlease enter the quantity for each fruit:")
    for fruit, price in fruits.items():
        while True:
            try:
                quantity:int=int(input(f"Enter the quantity of {fruit.title()} (${price:.2f} per unit): ").strip())
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                total_amount:float=price * quantity
                total_cost += total_amount
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid quantity.")

    print(f"\nYour total cost is: ${total_cost:.2f}")

    # Payment method selection
    while True:
        print("\nHow would you like to pay?")
        print("1. Cash")
        print("2. Card")
        payment_method:str =str(input("Enter 1 for Cash or 2 for Card: ").strip())

        if payment_method == "1":
            while True:
                try:
                    cash_given:float = float(input("Enter the amount of cash you are giving: ").strip())
                    if cash_given < total_cost:
                        print(f"Insufficient amount! You need ${total_cost - cash_given:.2f} more.")
                    else:
                        change = cash_given - total_cost
                        print(f"Payment successful! Your change is ${change:.2f}. Thank you!")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            break
        elif payment_method == "2":
            print("Processing card payment...")
            time.sleep(5)
            print("Payment successful! Thank you for shopping with us!")
            break
        else:
            print("Invalid option. Please select 1 for Cash or 2 for Card.")

Pop_Up_Shop()