def Login():
    UsernameInput = input("Username : ")
    PasswordInput = input("Password : ")
    if UsernameInput == "admin" and PasswordInput == "1234":
        print("Welcome!")
        Menu()
    else:
        print("Incorrect Username or Password!")
        print("Please, try again.")
        Login()
def Menu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. Exit")
    MenuSelection()
def MenuSelection():
    UserSelection = int(input("Selected Number : "))
    if UserSelection == 1:
        Price = int(input("Price (THB) : "))
        print("7% Vat :",VatCalc(Price),"THB")
        print("Price included 7% Vat :", Price + VatCalc(Price),"THB")
        return Menu()
    elif UserSelection == 2:
        print("Total price included 7% Vat:", PriceCalc(),"THB")
        return Menu()
    elif UserSelection == 3:
        print("Thank you!")
        return  Login()
    else:
        print("Please, select number from the list.")
        return Menu()
def VatCalc(Price):
    Vat = 7
    return Price * Vat / 100
def PriceCalc():
    Price1 = int(input("Price 1 (THB) : "))
    Price2 = int(input("Price 2 (THB) : "))
    TotalPrice = Price1 + Price2
    print("Total price :", TotalPrice, "THB")
    return TotalPrice + VatCalc(TotalPrice)

Login()