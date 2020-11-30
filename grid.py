from tkinter import *
def next():
    print("Your entries are :\n\n")
    print("Username :\t",username.get())
    print("Password :\t",password.get())
root=Tk()

root.geometry("480x360")

l=Label(root,text="Username")
l1=Label(root,text="Password")

l.grid()
l1.grid(row = 1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

username = StringVar()
password = StringVar()

userentry = Entry(root,textvariable = username)
passentry =  Entry(root , textvariable = password)

userentry.grid(row = 0 , column = 1)
passentry.grid(row = 1 , column = 1)

Button(text="Next",padx=11, command=next).grid()



root.mainloop()