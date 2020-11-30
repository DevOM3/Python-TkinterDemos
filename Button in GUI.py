from tkinter import  *

root=Tk()


def n():
    print("7")
def n1():
    print("8")
def n2():
    print("9")
def n3():
    print("4")
def n4():
    print("5")
def n5():
    print("6")
def n6():
    print("1")
def n7():
    print("2")
def n8():
    print("3")
def n9():
    print("0")
def p():
    print("+")
def m():
    print("-")
def a():
    print("*")
def d():
    print("/")
def iet():
    print("=")
def point():
    print(".")

root.geometry("480x360")
root.title("Calculator Layout")
f1=Frame(root,borderwidth=10,relief=GROOVE,bg="black")
f1.grid()

b=Button(f1,fg="gray",text="7",padx=9,command=n)
b.grid(row=0,column=0)

b1=Button(f1,fg="gray",text="8",padx=9,command=n1)
b1.grid(row=0,column=1)

b2=Button(f1,fg="gray",text="9",padx=9,command=n2)
b2.grid(row=0,column=2)

b3=Button(f1,fg="gray",text="4",padx=9,command=n3)
b3.grid(row=1,column=0)

b4=Button(f1,fg="gray",text="5",padx=9,command=n4)
b4.grid(row=1,column=1)

b5=Button(f1,fg="gray",text="6",padx=9,command=n5)
b5.grid(row=1,column=2)

b6=Button(f1,fg="gray",text="1",padx=9,command=n6)
b6.grid(row=2,column=0)

b7=Button(f1,fg="gray",text="2",padx=9,command=n7)
b7.grid(row=2,column=1)

b8=Button(f1,fg="gray",text="3",padx=9,command=n8)
b8.grid(row=2,column=2)

b9=Button(f1,fg="gray",text="0",padx=9,command=n9)
b9.grid(row=3,column=1)

bp=Button(f1,fg="gray",text="+",padx=9,command=p)
bp.grid(row=0,column=3)

bm=Button(f1,fg="gray",text="-",padx=9,command=m)
bm.grid(row=1,column=3)

ba=Button(f1,fg="gray",text="*",padx=9,command=a)
ba.grid(row=2,column=3)

bd=Button(f1,fg="gray",text="/",padx=9,command=d)
bd.grid(row=3,column=3)

be=Button(f1,fg="gray",text="=",padx=9,command=iet)
be.grid(row=3,column=0)

bpoint=Button(f1,fg="gray",text=".",padx=9,command=point)
bpoint.grid(row=3,column=2)

root.mainloop()