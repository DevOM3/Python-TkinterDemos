from tkinter import *


def Reg():
    register=open("register.txt",'a')
    register.write("\n\nFirst Name      :")
    register.write(firstname.get())
    register.write("\nLast Name      :")
    register.write(lastname.get())
    register.write("\nPhone Number  :")
    register.write(phone.get())
    register.write("\nEmail Address  :")
    register.write(emailid.get())
    # register.close()

root=Tk()


root.title("Registration Form")

l=Label(text="Om Londhe Corporation",font='monotypecorsiva 24 bold',pady=21)


last=Label(root,text="Last Name",pady=5)
first=Label(root,text="First Name",pady=5)
phno=Label(root,text="Phone Number",pady=5)
email=Label(root,text="Email Address",pady=5)

l.grid()
last.grid(row=2,pady=5)
first.grid(row=2,column=1,pady=5)
phno.grid(row=5,pady=5)
email.grid(row=10,pady=5)




lastname = StringVar()
firstname = StringVar()
phone = StringVar()
emailid= StringVar()
robot = IntVar()



la=Entry(root,textvariable = lastname)
f = Entry(root, textvariable = firstname)
p= Entry(root,textvariable=phone)
e = Entry(root,textvariable=emailid)


#checkbox

r = Checkbutton(text="I'm not a Robot",variable=robot)
r.grid()


la.grid(row=1)
f.grid(row=1,column=1)
p.grid(row=5,column=1)
e.grid(row=10,column=1)



Button(root,text="Register",command=Reg,pady=5).grid()


root.mainloop()