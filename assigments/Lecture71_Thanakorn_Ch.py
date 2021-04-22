MenuList = []
PriceList = []

def ShowBill():
    TotalPrice = 0
    print("---- The Food ----")
    for i in range(len(MenuList)):
        print(MenuList[i],PriceList[i])
        TotalPrice += int(PriceList[i])
    print("Total price :", TotalPrice)

while True:
    MenuName = input("Enter menu : ")
    if MenuName.lower() == "exit":
        break
    else:
        MenuPrice = input("Enter price : ")
        MenuList.append(MenuName)
        PriceList.append(MenuPrice)
ShowBill()