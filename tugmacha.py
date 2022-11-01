from tkinter import *

#oyna yasaymiz
root=Tk()



#oyna mavzusi
root.title("Bu tugmacha")

#ekran icon uzgartirish
#root.iconbitmap('icon.ico')
#rasm quyish
#filename=Image.open('img.png')
#Photo=ImageTk.PhotoImage(filename)
#Label(root,image=Photo).grid(column=0,row=0)

#oyna ulchami
#root.geometry('200*300')

#tugma ucun funksiya
def Bosilganda():
    yozuv=Label(root,text='bosildi', bg='red',fg='green')
    yozuv.pack()

def hisobla(text,l):
    #xatoni oldini oolish
    try:
        l.configure(text=eval(text.get()))
    except :
        pass

#kiritish uchun input
txt=Entry(root)
txt.place(x=10, y=10)

#chiqazish uchun 
lab=Label(root,text='javob')
lab.place(x=100,y=30)

#tugma yasaymiz
tugmam=Button(root,text='bos meni', command=Bosilganda, fg='blue', bg='red')

btn=Button(root,text='OK',command=lambda:hisobla(txt,lab))
btn.place(x=100,y=100)

#tugmani joylaymiz
tugmam.pack()
#tugmam.grid(row=0,column=0)

#oynani yopamiz
root.mainloop()