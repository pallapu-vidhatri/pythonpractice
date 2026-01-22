amount = int(input("Enter the principal amount: "))

if amount <= 10000:
    interest_rate = 0.03
elif amount <= 50000:
    interest_rate = 0.05
else:
    interest_rate = 0.07

print("The interest rate is:", interest_rate)   