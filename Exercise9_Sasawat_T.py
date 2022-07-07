username_input = input("Username: ")
password_input = input("Password: ")

while username_input != "admin" or password_input != "1234":
    print("Try agian")
    username_input = input("Username: ")
    password_input = input("Password: ")
print("Welcome")