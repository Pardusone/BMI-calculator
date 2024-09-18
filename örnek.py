import tkinter
from tkinter import Entry

def Bmi_hesapla():
    # Kilo ve boyu kullanıcıdan al
    kg = my_entry.get().strip()  # Kullanıcının kilo girişi
    height = my_entry2.get().strip()  # Kullanıcının boy girişi

    # Boş girişler için kontrol
    if not kg or not height:
        result_label.config(text="Lütfen boş bırakmayınız.")  # Eğer boş bırakılmışsa uyarı mesajı göster
        return

    try:
        # Kilo ve boyu sayıya dönüştür
        kg = float(kg)
        height = float(height)

        # BMI formülü
        bmi = kg / (height ** 2)

        # BMI değerine göre sonuçları göster
        if bmi < 18.5:
            result_label.config(text="Zayıf")
        elif 18.5 <= bmi < 24.9:
            result_label.config(text="Normal")
        elif 25 <= bmi < 29.9:
            result_label.config(text="Kilolu")
        elif bmi >= 30:
            result_label.config(text="Obez")

    except ValueError:
        # Eğer sayı yerine başka bir şey girildiyse
        result_label.config(text="Lütfen geçerli bir sayı giriniz.")

# Ana pencereyi oluştur
window = tkinter.Tk()
window.title("BMI")
window.minsize(width=500, height=450)

# Kilo için etiket ve giriş
my_label = tkinter.Label(text="Enter Your Kg:", font=('Arial', 10, "italic"))
my_label.config(fg="black")
my_label.pack()

my_entry = tkinter.Entry(width=20)
my_entry.pack()

# Boy için etiket ve giriş
my_label2 = tkinter.Label(text="Enter your height (in meters):", font=('Arial', 10, "italic"))
my_label2.config(fg="black")
my_label2.pack()

my_entry2 = tkinter.Entry(width=20)
my_entry2.pack()

# Hesapla butonu
my_button = tkinter.Button(text="Calculate", command=Bmi_hesapla)
my_button.pack(pady=10)

# Sonuçları göstermek için etiket
result_label = tkinter.Label()
result_label.pack(pady=10)

# Pencereyi başlat
window.mainloop()
