def VatCalc(x):
    Result = x * 7 / 100
    return Result

Price = int(input("Input Price (THB) : "))
print("Vat is :", VatCalc(Price), "THB")