from tkinter import *

root=Tk()

w=800
h=400

root.geometry(f"{w}x{h}")

#making widget
can_widget=Canvas(root,width=w,height=h)
can_widget.pack()

#create line accepts x1 , y1, x2 , y2 and fill="color"  which is optional co ordinates`

can_widget.create_line(0,0,100,400)
can_widget.create_line(0,0,400,200)
can_widget.create_line(0,0,600,400)
can_widget.create_line(380,500,0,0)
can_widget.create_line(700,167,0,0)
can_widget.create_line(500,376,0,0)
can_widget.create_line(300,0,0,678)
can_widget.create_line(500,0,0,150)
can_widget.create_line(734,0,0,100)

#create rectangle accepts x1 , y1, x2 , y2 and fill="color"  which is optional co ordinates`

can_widget.create_rectangle(0,0,100,400)
can_widget.create_rectangle(0,0,400,200)
can_widget.create_rectangle(0,0,600,400)
can_widget.create_rectangle(380,500,0,0)
can_widget.create_rectangle(700,167,0,0)
can_widget.create_rectangle(500,376,0,0)
can_widget.create_rectangle(300,0,0,678)
can_widget.create_rectangle(500,0,0,150)
can_widget.create_rectangle(734,0,0,100)

#this will create text using x,y ordinates and text=" "

can_widget.create_text(200,100,text="Om Londhe Python")

#this will create the Oval shape by taking two parameters which are like rectangle parameter

can_widget.create_oval(50,200,100,400)
can_widget.create_oval(210,40,400,200)
can_widget.create_oval(430,20,600,400)
can_widget.create_oval(380,500,40,40)
can_widget.create_oval(700,167,40,40)
can_widget.create_oval(500,376,110,40)
can_widget.create_oval(300,40,310,678)
can_widget.create_oval(500,130,320,150)
can_widget.create_rectangle(734,130,65,100)

#self done

can_widget.create_arc(200,300,400,600)

can_widget.create_window(200,100)



root.mainloop()