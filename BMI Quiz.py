import tkinter
from tkinter import Entry


def Bmi_hesapla():

    kg = my_entry.get().strip()
    height = my_entry2.get().strip()


    if not kg or not height:
        result_label.config(text="Lütfen boş bırakmayınız.")
        return



    try:
        kg = float(kg)
        height = float(height) / 100
        bmi = kg / (height ** 2)
        if (bmi < 18.5):
            result_label.config(text ="Zayıf")

        elif(bmi > 18.5 and bmi < 24.9):
            result_label.config(text="Normal")

        elif (bmi > 25 and bmi < 29.9):
            result_label.config(text="Kilolu")

        elif (bmi > 30 ):
            result_label.config(text="Obez")
    except ValueError:
        # Eğer sayı yerine başka bir şey girildiyse
        result_label.config(text="Lütfen geçerli bir sayı giriniz.")




window = tkinter.Tk()
window.title("BMI")
window.minsize(width = 500 , height = 450)

my_label = tkinter.Label(text= "Enter Your Kg:" , font=('Arial',10,"italic"))
my_label.config( fg = "black")
my_label.pack()

my_entry = tkinter.Entry(width=20)
my_entry.pack()

my_label2 = tkinter.Label(text= "Enter your height:" , font=('Arial',10,"italic"))
my_label2.config( fg = "black")
my_label2.pack()

my_entry2 = tkinter.Entry(width=20)
my_entry2.pack()


my_button = tkinter.Button(text = "Calculate",command = Bmi_hesapla)
my_button.place(x = 25 , y = 25)
my_button.pack()

result_label = tkinter.Label()
result_label.pack(pady = 10)

print(my_label.winfo_height())
print(my_label.winfo_width())
window.mainloop()