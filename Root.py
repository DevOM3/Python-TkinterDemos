from  tkinter import *

root=Tk()

root.title("Root 1st") #This can change the title of the output window
root.geometry("600x400")  # it is used while specifying the dimension of window in widthxheight format

root.minsize(400,200) #specifies minimum dimension in width,height format
root.maxsize(1920,1080) #specifies maximum dimension of window in width,height fromat

l=Label(text="Welcome to my First GUI") #This will make the label which will show up on the top of the GUI window
l.pack() #to print the label text we need to pack it in this function

root.mainloop()