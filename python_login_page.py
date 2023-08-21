from distutils.cmd import Command
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        ## Background Images
        #self.bg = ImageTk.PhotoImage(file="python/image/bg.jpeg")
        #self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # Login Frame py
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y = 150, width=500, height=400)

        # Title and subtitle
        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y= 30)
        subtitle = Label(Frame_login, text="Member Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y= 100)

        # Username
        lbl_user = Label(Frame_login, text="Username", font=("normal", 15,), fg="grey", bg="white").place(x=90, y= 140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15,), bg="#E7E6E6")
        self.username.place(x=90, y= 170, width=320, height=35)

        # Password
        lbl_password = Label(Frame_login, text="Password", font=("normal", 15,), fg="grey", bg="white").place(x=90, y= 210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15,), bg="#E7E6E6")
        self.password.place(x=90, y= 240, width=320, height=35)

        # Button
        forgot = Button(Frame_login, text="forgot password", bd=0, font=("Goudy old style", 10,), fg="#6162FF", bg="white").place(x=90, y= 280)
        submit = Button(Frame_login,command=self.check_function, text="Login", font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y= 320, width=180, height=40)
    
    # function
    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are requred", parent = self.root)
        elif self.username.get()!="asad" or self.password.get()!="123456":
            messagebox.showerror("Error", "invalid username or passwoed", parent = self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root = Tk()
obj = Login(root)
root.mainloop()
