units = int(input("Enter the number of electricity units consumed: "))

if units <= 100:
    bill_amount = units * 5
elif units <= 300:
    bill_amount = units * 7
else:
    bill_amount = units * 10

print("Total electricity bill amount: Rs.", bill_amount)