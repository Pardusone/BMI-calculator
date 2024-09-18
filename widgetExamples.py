from tabnanny import check
from tkinter import * #bu şekilde içerideki her şeyi import etmiş olduk

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600 , height = 600)
window.config(padx=20,pady=20) #x ve y ekseninde boşluk bırakır

#label
label = Label( text = "my label")
label.config(bg = "black" , fg= "white")
label.pack()
#text
text = Text(width=30,height=10)
text.pack()
text.focus() #imleç buradan başlar

#button
def button_clicked():
    print("Button clicked!!!")
    print(text.get("1.0",END)) #1. satırdan ve 0. karakterden başla sonuna kadar git

button = Button(text = "button",command = button_clicked)
button.config(padx=10,pady = 10)
button.pack()
#entry
entry = Entry(width=20)
entry.pack()

#widget örnekleri


#scale
def scale_selected(value):
    print(my_scale.get())

my_scale = Scale(from_  = 0 , to = 50, command = scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_ = 0 , to = 50,command = spinbox_selected)
my_spinbox.pack()


#checkbutton

def checkButton():
    print(check_state.get())
check_state = IntVar()
my_checkbutton = Checkbutton(text = "check", variable=check_state,command =checkButton() )
my_checkbutton.pack()



#radio button

from tkinter import *

def radio_selected():
    print(radio_checked_state.get())

window = Tk()

radio_checked_state = IntVar()  # IntVar() olarak nesne oluşturmalısınız
my_radiobutton = Radiobutton(text="1. option", value=10, variable=radio_checked_state, command=radio_selected)
my_radiobutton2 = Radiobutton(text="2. option", value=20, variable=radio_checked_state, command=radio_selected)
my_radiobutton3 = Radiobutton(text="3. option", value=30, variable=radio_checked_state, command=radio_selected)

my_radiobutton.pack()
my_radiobutton2.pack()
my_radiobutton3.pack()

#listbox
def listbox_selected(event): 
    print(my_listbox.get(my_listbox.curselection())) #seçilen elemanı bastır

my_listbox = Listbox()
name_list = ["atil","abc","marka","merhaba"]

for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])


my_listbox.bind("<<ListboxSelect>>", listbox_selected) #fonksiyon ile listboxu bağladık bu kullanım şekli bu yapıya özel
my_listbox.pack()



window.mainloop()