from tkinter import *

root=Tk()


# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

root.title("Label options")

l=Label(text='''Hello my name is OM Londhe and I am from Aurangabad .\n
              I am in Government Polytechnic , Aurangabad In the Second Year .''', bg='black' , fg='white' , padx=75, pady=25 , font='monotypecorsiva 21 italic', borderwidth=7, relief=GROOVE)


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

#l.pack(side=BOTTOM, anchor ="sw", fill=X)


l.pack(side=TOP, anchor=NE, fill=X ,padx=51,pady=21)



root.mainloop()