age = int(input("Enter your age: "))
ticketprice = 250
if age<= 10:
    ticketprice = ticketprice - (ticketprice * 0.5)
    print("Your ticket price is:",ticketprice)
elif age >= 60:
    ticketprice = ticketprice - (ticketprice * 0.3)
    print("Your ticket price is:",ticketprice)
else:
    print("Your ticket price is:",ticketprice)
    