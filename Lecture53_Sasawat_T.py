price = int(input("Price: "))

def VatCalculate(price):
    result = "Total price: " + str(price+(price*0.07))
    return result

print(VatCalculate(price))
