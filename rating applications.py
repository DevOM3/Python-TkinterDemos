from tkinter import *
import tkinter.messagebox as tm

def submit():
    t=tm.askquestion("Are you sure to give this rating ?")
    if t=='yes':
        tm.showinfo("Thank you , for Rating us ")


root=Tk()

root.geometry("700x500")
root.title("Rating")

Label(text='Rate our App from 1 to 5',font='monotypecorsiva 21 bold').pack()


slider = Scale(root, from_=1 , to = 5 ,orient=HORIZONTAL,bg='white',fg='red')
slider.pack(padx=71,pady=51)

Button(text='Submit',command=submit).pack()


root.mainloop()
