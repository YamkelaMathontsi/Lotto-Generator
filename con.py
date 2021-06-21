# Yamkela Mathontsi
from tkinter import *
import requests
from tkinter import messagebox


root = Tk()
root.title("Currency Converter")
root.geometry("900x700")
root.config(bg="red")
root.resizable(False, False)

# image
photo = PhotoImage(file="currency.png")
pic_label = Label(root, image=photo)
pic_label.place(x=50, y=10)
# image
photo2 = PhotoImage(file="small.png")
pic2_label = Label(root, image=photo2)
pic2_label.place(x=10, y=400)
# image
photo3 = PhotoImage(file="small.png")
pic3_label = Label(root, image=photo3)
pic3_label.place(x=550, y=400)


value = IntVar()

# currency conversions
information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']


# entry for the results
value_entry = Entry(root, textvariable=value, width=40)
value_entry.config(bg="orange")
value_entry.place(x=280, y=370)


convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.config(bg="tan")
    convert_list.place(x=350, y=400)

convert_label = Label(root, font=("Serif", 20))
convert_label.place(x=220, y=150, width=400)


def convert_curr():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans

#
convert_btn = Button(root, command=convert_curr, text="Convert", font=("Serif", 20), width=20)
convert_btn.config(bg="black", fg="white")
convert_btn.place(x=250, y=590)

def clear():
    value_entry.delete(0, END)
    convert_label.delete(0, END)

def destroy():
    msg_box = messagebox.askquestion("You are now closing the program", " Are You Sure")
    root.destroy()

clear_btn = Button(root, text='Clear', bg="black", fg="white", command=clear)
clear_btn.place(x=300, y=650)
exit = Button(root, text='Exit', bg="black", fg="white", command=destroy)
exit.place(x=500, y=650)



root.mainloop()
