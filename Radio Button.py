from tkinter import *
import tkinter.messagebox as m

def done():
    m.showinfo("Grade Submitted                                             ")
root=Tk()

root.geometry("800x400")
root.title("Grade")

Label(root, text="Select and Submit your grades :").pack(anchor='w')

g=StringVar()
g.set(' ')

radio=Radiobutton(root,text='A+',value='A+',variable=g).pack(anchor='w')
radio=Radiobutton(root,text='A',value='A',variable=g).pack(anchor='w')
radio=Radiobutton(root,text='B+',value='B+',variable=g).pack(anchor='w')
radio=Radiobutton(root,text='b',value='B',variable=g).pack(anchor='w')
radio=Radiobutton(root,text='C+',value='C+',variable=g).pack(anchor='w')
radio=Radiobutton(root,text='C',value='C',variable=g).pack(anchor='w')
radio=Radiobutton(root,text='D',value='D',variable=g).pack(anchor='w')

Button(root,text='Submit',command=done).pack(side=LEFT)

root.mainloop()