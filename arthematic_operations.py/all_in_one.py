a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /, //, %, **): ")

if operation == '+':
    result = a + b
    print("The sum of", a, "and", b, "is:", result)

elif operation == '-':
    result = a - b
    print("The difference of", a, "and", b, "is:", result)

elif operation == '*':
    result = a * b
    print("The product of", a, "and", b, "is:", result)

elif operation == '/':
    result = a / b
    print("The quotient of", a, "and", b, "is:", result)

elif operation == '//':
    result = a // b
    print("The floor division of", a, "and", b, "is:", result)

elif operation == '%':
    result = a % b
    print("The remainder of", a, "and", b, "is:", result)
    
elif operation == '**':
    result = a ** b
    print("The power of", a, "raised to", b, "is:", result)