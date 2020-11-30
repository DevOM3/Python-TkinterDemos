from tkinter import  *
import tkinter.messagebox as tm #used for message box

def quit():
    q=tm.askquestion("Do you want to Exit ?")

    if q=='yes':
        exit()


def Help():
    tm.showinfo("Help not available")


def cu():
    recur=tm.askretrycancel("Can't connect at the moment")
    if recur:
        cu()


root=Tk()

root.geometry("480x360")

m=Menu(root)

m1=Menu(m,tearoff=0)

m1.add_command(label='New Project')
m1.add_command(label='New')
m1.add_separator()
m1.add_command(label='Open')
m1.add_command(label='close')
m1.add_separator()
m1.add_command(label='Save')
m1.add_command(label='Save as')
m1.add_command(label='Save all')

root.config(menu=m)
m.add_cascade(label='File',menu=m1)


m1=Menu(m,tearoff=0)

m1.add_command(label='Clear all')
m1.add_separator()
m1.add_command(label='Undo')
m1.add_command(label='Redo')
m1.add_separator()
m1.add_command(label='Cut')
m1.add_command(label='Copy')
m1.add_command(label='Paste')
root.config(menu=m)
m.add_cascade(label='Edit',menu=m1)


m1=Menu(m,tearoff=0)
m1.add_command(label='Help',command=Help)
m1.add_command(label='Exit',command=quit)
m1.add_cascade(label='Contact us',command=cu)

root.config(menu=m)
m.add_cascade(label='Help',menu=m1)


root.mainloop()