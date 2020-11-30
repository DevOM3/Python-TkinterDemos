from tkinter import *
from PIL import Image, ImageTk

root=Tk()

root.geometry("480x200")

# frame is capital word which returns frae GUI and accepts bg , borderwidth and relief attributes

f=Frame(root,bg="white",borderwidth=2)
f.pack()

f1 = Frame(root,bg="gray" , borderwidth=7 , relief=GROOVE)
f1.pack(side=LEFT,fill=Y)

f2=Frame(root,borderwidth=3,relief=RAISED)
f2.pack()

l=Label(f,padx=1920,pady=7)
l.pack(fill=X)

l=Label(f1,text="Tools here",bg="gray",fg="black",font="black 7 bold",padx=21)
l.pack()

photo=ImageTk.PhotoImage(Image.open("C:\\Desktop\\google-wallpaper-1.jpg"))
l=Label(f2,image=photo)
l.pack()


root.mainloop()