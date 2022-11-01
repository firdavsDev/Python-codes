from tkinter import *

root=Tk()
root.title("Aylana")


c=Canvas(root,width=200,height=200,bg="white")
c.pack()

c.create_oval(10,10,190,190,fill='lightgrey',outline='white')
c.create_arc(10,10,190,190,start=0,extent=45,fill='red')
c.create_arc(10,10,190,190,start=180,extent=25,fill='yellow')
c.create_arc(10,10,190,190,start=240,extent=100,style=CHORD,fill='green')
c.create_arc(10,10,190,190,
start=160,extent=-70,style=ARC,outline='darkblue',width=5)

root.mainloop()