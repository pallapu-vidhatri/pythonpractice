username = "admin"
password = "admin123"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")