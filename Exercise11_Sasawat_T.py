#Answer1
number = int(input("Number: "))
for x in range(number):
    print(" "*(number-(x-1)) + "*"*int((x+1)+x))

#Answer2
number = int(input("Number: "))
for x in range(number):
    star = ""
    for y in range((x+1)+x):
        star += "*"
    print(" "*(number-(x-1)) + star)