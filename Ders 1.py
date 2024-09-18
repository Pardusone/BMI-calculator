import tkinter

windows = tkinter.Tk()
windows.title("Python Tkinter")
windows.minsize(width= 450 , height= 300)


def click_button():

    user_input = my_entry.get()
    print(user_input)
#label

my_label = tkinter.Label(text= "this is a label" , font=('Arial',30,"italic"))
my_label.config(bg = "black", fg = "white")
#my_label.pack(side = "left") #sola ya da farklı yönlere de koyabiliriz bu şekilde

#button

my_button = tkinter.Button(text = "this is a button",command = click_button)
#my_button.pack()


#entry

my_entry = tkinter.Entry(width=50)
#my_entry.pack()

#spesifik konumlama

my_label.place(x = 50 , y = 50 )


#konumları öğrenmek için
my_label.update()
print(my_label.winfo_height())
print(my_label.winfo_width())


#grid kolon ve satırları kullanarak istediğimiz ızgaraya koyabiliriz

my_label.grid(row = 0 , column = 0)
my_button.grid(row = 1 , column = 1)
my_entry.grid(row = 0  , column = 2)

windows.mainloop()