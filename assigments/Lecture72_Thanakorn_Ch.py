MenuList = []

def ShowBill():
    TotalPrice = 0
    print("---- The Food ----")
    for i in range(len(MenuList)):
        print(MenuList[i])
        TotalPrice += MenuList[i][1]
    print("Total price :", TotalPrice)

while True:
    MenuName = input("Enter menu : ")
    if MenuName.lower() == "exit":
        break
    else:
        MenuPrice = int(input("Enter price : "))
        MenuList.append([MenuName, MenuPrice])
ShowBill()