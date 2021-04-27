from tkinter import *
import math

def BmiCalc(event):
    BmiValue = float(Entry_Weight.get()) / math.pow(float(Entry_Height.get())/100, 2)
    Lbl_Bmi.configure(text = "BMI : " + str('%.2f' %BmiValue))
    if BmiValue <= 18.5:
        BmiDesc = "อยู่ในเกณฑ์น้ำหนักน้อย / ผอม"
    elif BmiValue <= 22.9:
        BmiDesc = "อยู่ในเกณฑ์ปกติ (สุขภาพดี)"
    elif BmiValue <= 24.9:
        BmiDesc = "อยู่ในเกณฑ์ท้วม / โรคอ้วนระดับ 1"
    elif BmiValue <= 29.9:
        BmiDesc = "อยู่ในเกณฑ์อ้วน / โรคอ้วนระดับ 2"
    elif BmiValue > 29.9:
        BmiDesc = "อยู่ในเกณฑ์อ้วนมาก / โรคอ้วนระดับ 3"
    Lbl_Desc.configure(text = BmiDesc)

Window_Main = Tk()
Lbl_Topic = Label(Window_Main, text = "BMI Calculator")
Lbl_Topic.grid(row = 1, column = 1)
Lbl_Weight = Label(Window_Main, text = "Weight (kg) : ")
Lbl_Weight.grid(row = 2, column = 1)
Entry_Weight = Entry(Window_Main, bd = 3)
Entry_Weight.grid(row = 2, column = 2)
Lbl_Height = Label(Window_Main, text = "Heigth (cm) : ")
Lbl_Height.grid(row = 3, column = 1)
Entry_Height = Entry(Window_Main, bd = 3)
Entry_Height.grid(row = 3, column = 2)
Btn_Calc = Button(Window_Main, text = "Calculate")
Btn_Calc.bind('<Button-1>', BmiCalc)
Btn_Calc.grid(row = 4, column = 1)
Lbl_Bmi = Label(Window_Main, text = "BMI Value")
Lbl_Bmi.grid(row = 4, column = 2)
Lbl_Desc = Label(Window_Main, text = "Description")
Lbl_Desc.grid(row = 5, column = 2)
Window_Main.mainloop()