from tkinter import *
from tkinter import messagebox
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class bank(object):
    def __init__(self, root):

        self.root = root
        self.root.title("Bank")
        self.root.geometry("600x400")
        self.root.config(bg="green")
        # self.resizable(False, False)

        # self.photo = PhotoImage(self.root, file="banks.png")
        # self.pic_label = Label(self.root, image=self.photo)
        # self.pic_label.place(x=20, y=10)

        # headings
        self.heading_info = Label(self.root, text="Enter Your Details and submit for further instructions", bg="black", fg="white")
        self.heading_info.place(x=150, y=70)
        self.heading = Label(self.root, text="Banks of South Africa", bg="black", fg="white")
        self.heading.place(x=250, y=10)

        # Cell number label and entry
        self.acc_holder = Label(self.root, text="Account Holder:", bg="yellow")
        self.acc_holder.place(x=110, y=100)
        self.acc_holder_entry = Entry(self.root)
        self.acc_holder_entry.place(x=320, y=100)
        self.acc_num = Label(self.root, text="Account Number:", bg="yellow")
        self.acc_num.place(x=110, y=145)
        self.acc_num_ent = Entry(self.root)
        self.acc_num_ent.place(x=320, y=145)

        # Type of bank
        self.select_bank_label = Label(self.root, text="Select Your Bank:", bg="yellow")
        self.select_bank_label.place(x=110, y=200)
        self.options = ["First National Bank", "Absa", "Standard Bank", "Capitec", "Nedbank"]
        self.variable = StringVar(self.root)
        self.variable.set("Select Bank")
        self.bank_opt = OptionMenu(root, self.variable, *self.options)
        self.bank_opt.place(x=320, y=200, width=170,)

        self.border1 = Label(self.root, text="xxxxxxx'You'xxxxxxxxxx'Are'xxxxx'A'xxxx'winner'xxxxxxxxxxxxxxxxxxxxxxxxx",
                             bg="blue")
        self.border2 = Label(self.root, text="xxxxxxx'You'xxxxxxxxxx'Are'xxxxx'A'xxxx'winner'xxxxxxxxxxxxxxxxxxxxxxxxx",
                             bg="blue")
        self.border1.place(x=50, y=40)
        self.border2.place(x=50, y=250)

        self.btn = Button(self.root, text="submit", command=self.submit, bg="black", fg="white")
        self.btn.place(x=300, y=300)

        self.btn1 = Button(self.root, text="convert", command=self.convert, bg="black", fg="white")
        self.btn1.place(x=170, y=300)

        self.btn2 = Button(self.root, text="exit", command=self.destroy, bg="black", fg="white")
        self.btn2.place(x=420, y=300)


    def destroy(self):
        msg = messagebox.askquestion("THANK YOU FOR YOU USING OUR APP ? ", "Are You Sure You Would Like To Exit ?")  # MESSAGE DISPLAYED
        # WHEN CLICKING EXIT BUTTON
        if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
            root.destroy()  # CLOSE CURRENT WINDOW


    def convert(self):
        msg = messagebox.askquestion("You are leaving the claim screen", "Do you want to convert" )
        if msg == "yes":
            root.destroy()
            import con

    def submit(self):
        messagebox.showinfo("Thank you for playing", " An email will be sent soon.")
        read_text_file = 'storage.txt'
        read_file = open(read_text_file, "r")
        list_file = read_file.readlines()

        email = str(list_file)
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email)
        email = emails[-1]
        print(email)

        sender_email_id = 'luckylottoyamkela@gmail.com'
        receiver_email_id = email
        password = "mercislife"
        subject = "Lotto"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "HI, Congratulations You've won the LOTTO!!\n"
        body = body + "Congratulations on winning the LOTTO, you will be informed on the next email"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(sender_email_id, password)
        print(receiver_email_id)

        # sending the mail
        s.sendmail(sender_email_id, receiver_email_id, text)
        # terminating the session
        s.quit()

    def acc(self):
        self.acc_num = self.acc_num_ent.get()
        self.acc_holder = self.acc_holder_entry.get()

        if not self.acc_holder.isalpha():
            messagebox.showerror("INVALID", "PLEASE ENTER PROPER NAME")

        elif not self.acc_num.isdigit():
            messagebox.showerror("INVALID", "PLEASE ENTER VALID ACCOUNT NUMBER")

root = Tk()
bank(root)
root.mainloop()
