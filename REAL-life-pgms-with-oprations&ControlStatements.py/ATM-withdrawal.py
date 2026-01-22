balance = 10000  # Initial balance
withdrawal_amount = float(input("Enter the amount to withdraw: "))

if withdrawal_amount <= balance and withdrawal_amount > 0:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful!")
    print("Remaining balance:", balance)

else:
    print("Insufficient balance or invalid amount entered.")
    print("Current balance:", balance)
    