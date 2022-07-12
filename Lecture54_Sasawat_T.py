def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Welcome")
        return showMenu()
    else:
        print("Invalid username or password")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator(int(input("Product Price: ")))
    elif userSelected == 2:
        return priceCalculator()
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = str(totalPrice + (totalPrice * vat / 100)) + " " + "THB"
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1+price2
    return vatCalculator(totalPrice)

print(login())
print(menuSelect())
