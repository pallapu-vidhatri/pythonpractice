age = int(input("Enter your age: "))

if age < 5:
    ticket_price = 0
elif age <= 18:
    ticket_price = 10
elif age <= 60:
    ticket_price = 20
else:
    ticket_price = 15

print("Your ticket price is:",ticket_price)
