amount = int(input("Enter the principal amount: "))

is_member = input("Are you a member? (yes/no): ")

if amount <= 1000:
    discount = 0
elif amount <= 5000:
    discount = amount * 0.05
else:
    discount = amount * 0.10

print("Your discount amount is:", discount)