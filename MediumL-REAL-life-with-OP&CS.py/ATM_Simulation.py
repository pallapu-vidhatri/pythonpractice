balance=5000

print("Welcome to the ATM Simulation")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")
print("4. Exit")
choice = int(input("Please select an option (1-4): "))
if choice == 1:
    print("Your current balance is:", balance)
elif choice == 2:
    withdraw_amount = int(input("Enter amount to withdraw: "))
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance.")
    print("Your updated balance is:", balance)
elif choice == 3:
    deposit_amount = int(input("Enter amount to deposit: "))
    balance += deposit_amount
    print("Your updated balance is:", balance)
elif choice == 4:
    print("Thank you for using the ATM. Goodbye!")
else:
    print("Invalid option selected.")
