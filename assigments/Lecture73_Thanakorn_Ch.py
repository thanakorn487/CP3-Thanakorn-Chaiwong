SystemMenu = {"a":50, "b":30, "c":20, "d":10}
MenuList = []

def ShowBill():
    TotalPrice = 0
    print("---- The Food ----")
    for i in range(len(MenuList)):
        print(MenuList[i][0], MenuList[i][1])
        TotalPrice += MenuList[i][1]
    print("Total price :", TotalPrice)

while True:
    MenuName = input("Enter menu : ")
    if MenuName.lower() == "exit":
        break
    else:
       MenuList.append([MenuName, SystemMenu[MenuName]])
ShowBill()