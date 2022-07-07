#Answer1
number = int(input("Number: "))
for x in range(number):
    print(" "*(number-(x-1)) + "*"*int((x+1)+x))