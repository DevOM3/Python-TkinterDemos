
from tkinter import *
from PIL import Image, ImageTk


root=Tk()

root.geometry("1255x944")
root.title("Adding image using label in GUI")# change the name of output window
#photo=PhotoImage(file="python-logo-png--728.png") # it accepts image in .png format

#for jpg image
image = Image.open("C:\\Desktop\\google-wallpaper-1.jpg", "r")
photo = ImageTk.PhotoImage(image)

l=Label(image=photo) #this gives photo to tyhe label
l.pack()



root.mainloop()
