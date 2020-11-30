from tkinter import *

root=Tk()

root.geometry("600x400")

slider = Scale(root, from_= 0, to=100)      #orient=HORIZONTAL can be used to make the sllider horizontal
                                            #tkinterval is used to show values between
slider.pack(side='right')


root.mainloop()