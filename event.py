from tkinter import *

def click(event):
    print("You clicked\n")

root=Tk()


#this is the button created
b=Button(root,text="Click")
b.pack()

b.bind('<Button-1>',click)  #this is the event button it passes an default argument so to accept it we need to give a parameter
                            # to the funcion defined that parameter is always named as event



root.mainloop()