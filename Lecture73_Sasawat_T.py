systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
    total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], "THB")
        total += int(menuList[number][1])
    print("---------------")
    print("Total ", total, "THB")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()