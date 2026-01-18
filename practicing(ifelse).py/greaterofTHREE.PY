a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    greater = a
elif b > c:
    greater = b
else:
    greater = c

print("The greater value is:", greater)