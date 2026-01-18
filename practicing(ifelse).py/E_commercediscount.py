amount = int(input("Enter the total purchase amount: "))
membership = input("Are you a member? (yes/no): ").strip().lower()
if membership == 'yes':
    discount = 0.10
else:
    discount = 0.05
final_amount = amount * (1 - discount)
print(f"The final amount after discount is: ${final_amount:.2f}")
