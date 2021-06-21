# Yamkela Mathontsi Class1

from tkinter import *
from tkinter import messagebox
import rsaidnumber
import datetime
from datetime import *
import re
import random

root = Tk()
root.title("images")
root.geometry("1000x500")
root.config(bg="yellow")
root.resizable(False, False)

now = datetime.now()

# lotto image
photo = PhotoImage(file="flog.png")
pic_label = Label(root, image=photo)
pic_label.place(x=10, y=10)

#  clearing function
def clear_text():
    name.delete(0, END)
    email.delete(0, END)
    id_num.delete(0, END)

#  exiting function
def destroy():
    msg = messagebox.askquestion("THANK YOU FOR YOU USING OUR APP ? ", "Are You Sure You Would Like To Exit ?")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()  # CLOSE CURRENT WINDOW


# Name Label
name = Label(root, text="Name:", bg="yellow")
name.place(x=220, y=250)
# email label
email = Label(root, text="Email Address:", bg="yellow")
email.place(x=220, y=300)
#  identity number label
id_num = Label(root, text="ID Number", bg="yellow")
id_num.place(x=220, y=350)


# name Entry
name = Entry(root, text="", width=50)
name.place(x=330, y=250)
# email entry
email = Entry(root, text="", width=50)
email.place(x=330, y=300)
#  identity number entry
id_num = Entry(root, text="", width=50)
id_num.place(x=330, y=350)


# verification and storing of email
def verify():
    #  verification and txt file
    w = open("storage.txt", "a+")
    w.write("Name: " +
            email.get() + " " + "Email Address:" + " " + name.get() + " " + "ID Number:" + " " + id_num.get() + " " + "Logged in "
                                                                                                                         "to play "
                                                                                                                         "Lotto at:"
            + str(now) +
            "\n")
    w.close()
    try:
        id_number = rsaidnumber.parse(id_num.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        if int(age) >= 18:
            messagebox.showinfo("Access Granted ", "Let's Go Win")

            root.destroy()
            import lotto_screen
        else:
            messagebox.showinfo("INVALID", "You Have To Be Over 18 to Play")
    except ValueError:

        messagebox.showinfo("INVALID", "Please Enter A Valid 13 Digit ID Number")

    mail = email.get()
    if re.search(reverify, mail):
        messagebox.showinfo("SUCCESS", "Valid Email")
    else:
        messagebox.showinfo("INVALID", "Invalid Email")

#  verify button
verify = Button(root, width=10, bg="black",text="Log In", command=verify, fg="white")
verify.place(x=450, y=450)
#  clear button
clear_btn = Button(root, text='Clear', bg="black", command=clear_text, fg="white")
clear_btn.place(x=420, y=400)
#  exit button
exit = Button(root, text='Exit', bg="black", command=destroy, fg="white")
exit.place(x=520, y=400)


reverify = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


root.mainloop()

