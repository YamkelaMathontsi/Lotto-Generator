from tkinter import *
from tkinter import messagebox
from playsound import playsound
import random


root = Tk()
root.title("images")
root.geometry("700x700")
root.config(bg="blue")
root.resizable(False, False)
photo = PhotoImage(file="ITHUBA-NATIONAL-LOTTERY.png")
pic_label = Label(root, image=photo)
pic_label.place(x=100, y=10)

#Label and entry
# name = Label(root, text="Name:", bg="blue", fg="white")
# name.place(x=150, y=150)
# name_ent = Entry(root, text="")
# name_ent.place(x=100, y=170)

#Label and entry
# code = Label(root, text="Code:",bg="yellow")
# code.place(x=450, y=150)
# code_ent = Entry(root, text="")
# code_ent.place(x=400, y=170)

# heading label
your_num = Label(root, text="Choose or Enter Your Numbers Below:", bg="yellow")
your_num.place(x=230, y=200)
# sub heading label
the_num = Label(root, text="These Are The Winning Numbers:", bg="yellow")
the_num.place(x=230, y=320)



# spinbox
def pick():
    x1 = random.randint(1, 50)
    randomRef1 = str(x1)
    box1.set(randomRef1)

    x2 = random.randint(1, 50)
    randomRef2 = str(x2)
    box2.set(randomRef2)

    x3 = random.randint(1, 49)
    randomRef3 = str(x3)
    box3.set(randomRef3)

    x4 = random.randint(1, 49)
    randomRef4 = str(x4)
    box4.set(randomRef4)

    x5 = random.randint(1, 49)
    randomRef5 = str(x5)
    box5.set(randomRef5)

    x6 = random.randint(1, 49)
    randomRef6 = str(x6)
    box6.set(randomRef6)

    randomList = [x1, x2, x3, x4, x5, x6]
    inputlist = [int(spinbox1.get()), int(spinbox2.get()), int(spinbox3.get()), int(spinbox4.get()), int(spinbox5.get()), int(spinbox6.get())]
    matchlist = list(set(randomList).intersection(inputlist))
    num_match = len(matchlist)
    print(matchlist)
    print(num_match)
    messagebox.showinfo("!!!! WINNINGS !!!!", "You Got " + str(num_match) + " Winning Balls")
    try:
        if num_match <= 1:
            playsound("audio2.mp3")
            messagebox.showinfo("You Have No Winning Numbers", "You Have Won R0.00")
        elif num_match == 2:
            # playsound("audio1.mp3")
            messagebox.showinfo("You Won!", "You Have Won R20.00")
            win_message = messagebox.askquestion("You've won", "Do you want Claim")
            if win_message == "yes":
                next_window()
        elif num_match == 3:
            messagebox.showinfo("LUCKY", "You Have Won R100.50")
        elif num_match == 4:
            messagebox.showinfo("LUCKY", "You Have Won R2384.00")
        elif num_match == 5:
            messagebox.showinfo("LUCKY", "You Have Won R8584.00")
        else:

            messagebox.showinfo("!!!! JACKPOT !!!!", "YOU HAVE WON 10 000 000 ")
    except ValueError as x:
        messagebox.showerror("ERROR", "ERROR")
    finally:
        btnGen["text"] = "Pressa Push Phanda Play Again"
        clear()


# exit button
def exit():

    root.destroy()

def next_window():
    root.destroy()
    import bank

#  clear button
def clear():
    box1.set("")
    box2.set("")
    box3.set("")
    box4.set("")
    box5.set("")
    box6.set("")
    spinbox1.delete(0, END)
    spinbox2.delete(0, END)
    spinbox3.delete(0, END)
    spinbox4.delete(0, END)
    spinbox5.delete(0, END)
    spinbox6.delete(0, END)


box1 = StringVar()
box2 = StringVar()
box3 = StringVar()
box4 = StringVar()
box5 = StringVar()
box6 = StringVar()

# spinbox
spinbox1 = Spinbox(root, width=2, from_=1, to=49, bg="red", font=("bold", 20), fg="white")
spinbox1.place(x=580, y=250, height=50)
spinbox2 = Spinbox(root, width=2, from_=1, to=49, bg="black", font=("bold", 20), fg="white")
spinbox2.place(x=480, y=250, height=50)
spinbox3 = Spinbox(root, width=2, from_=1, to=49, bg="green", font=("bold", 20), fg="white")
spinbox3.place(x=380, y=250, height=50)
spinbox4 = Spinbox(root, width=2, from_=1, to=49, bg="red", font=("bold", 20), fg="white")
spinbox4.place(x=280, y=250, height=50)
spinbox5 = Spinbox(root, width=2, from_=1, to=49, bg="black", font=("bold", 20), fg="white")
spinbox5.place(x=180, y=250, height=50)
spinbox6 = Spinbox(root, width=2, from_=1, to=49, bg="green", font=("bold", 20), fg="white")
spinbox6.place(x=80, y=250, height=50)

# boxes for numbers generated
textbox1 = Entry(root, textvariable=box1, bd=10, justify="right", bg="black", fg="white", width=2, font=("bold",20))
textbox1.place(x=580, y=360)
textbox2 = Entry(root, textvariable=box2, bd=10, justify="right", bg="blue", fg="white", width=2, font=("bold",20))
textbox2.place(x=480, y=360)
textbox3 = Entry(root, textvariable=box3, bd=10, justify="right", bg="red", fg="white", width=2, font=("bold",20))
textbox3.place(x=380, y=360)
textbox4 = Entry(root, textvariable=box4, bd=10, justify="right", bg="green", fg="white", width=2, font=("bold",20))
textbox4.place(x=280, y=360)
textbox5 = Entry(root, textvariable=box5, bd=10, justify="right", bg="blue", fg="white", width=2, font=("bold",20))
textbox5.place(x=180, y=360)
textbox6 = Entry(root, textvariable=box6, bd=10, justify="right", bg="black", fg="white", width=2, font=("bold",20))
textbox6.place(x=80, y=360)


btnGen = Button(root, command=pick, text="Pressa Push Phanda Play", bg="black", fg="white", width=25)
btnGen.place(x=220, y=430)

btnClear = Button(root, command=clear, text="CLEAR", bg="black", fg="white", width=10)
btnClear.place(x=100, y=480)

btnExit = Button(root, command=exit, bg="black", text="EXIT", fg="white", width=10)
btnExit.place(x=400, y=480)






root.mainloop()


