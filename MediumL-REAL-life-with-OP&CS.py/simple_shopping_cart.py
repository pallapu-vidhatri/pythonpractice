price = 0

print("Welcome to the Simple Shopping Cart!")
print("1. Add Item")
print("2. View Total Price")
print("3. Checkout")
print("4. Exit")

while True:

    choice = int(input("Please select an option (1-4): "))

    if choice == 1:
        item_price = float(input("Enter the price of the item to add: "))
        price += item_price
        print(f"Item added. Current total price: {price}")
    elif choice == 2:
        print(f"Total price of items in cart: {price}")
    elif choice == 3:
        print(f"Checking out. Total amount to pay: {price}")
        price = 0  # Reset cart after checkout
    elif choice == 4:
        print("Thank you for shopping with us. Goodbye!")
        break
    else:
        print("Invalid option selected.")