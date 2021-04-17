#dShop Program
#Login part
UsernameInput = input("Username : ")
PasswordInput = input("Password : ")
if UsernameInput == "admin" and PasswordInput == "1234":
    # ---imposed Unit Price---
    UnitPrice_Pencil = 5
    UnitPrice_Pen = 7
    UnitPrice_Eraser = 10
    UnitPrice_Ruler = 11
    #---List and Goods Selection part---
    print("Welcome! admin")
    print("Please, select goods NUMBER from the list.")
    print("----- dShop Goods List -----")
    print("1) Pencil",UnitPrice_Pencil,"THB/ea.")
    print("2) Pen",UnitPrice_Pen,"THB/ea.")
    print("3) Eraser",UnitPrice_Eraser,"THB/ea.")
    print("4) Ruler",UnitPrice_Ruler,"THB/ea.")
    print("----------------------------")
    Selected = input("Select Goods NUMBER : ")
    Quantity = int(input("Quantity : "))
    #---Calculator---
    if Selected == "1":
        Price = UnitPrice_Pencil * Quantity
        print("Price : ",Price,"THB")
    elif Selected == "2":
        Price = UnitPrice_Pen * Quantity
        print("Price : ",Price,"THB")
    elif Selected == "3":
        Price = UnitPrice_Eraser * Quantity
        print("Price : ",Price,"THB")
    elif Selected == "4":
        Price = UnitPrice_Ruler * Quantity
        print("Price : ",Price,"THB")
    else:
        print("There's no selected Goods NUMBER in the List.")
else:
    print("Incorrect Username or Password!")
    print("Please, Try again.")