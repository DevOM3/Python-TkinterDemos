from tkinter import  *

def file():
    print("You clicked on File")

root=Tk()

root.geometry("480x360")


#this is used when it dont have drop down menu

m=Menu(root) #specifies the Menu
m.add_command(label="File",command=file) #add command function taking arguments
m.add_command(label="Exit",command=exit)

root.config(menu=m) #config command is used with root variable at the task bar position

root.mainloop()