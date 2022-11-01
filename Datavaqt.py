from datetime import datetime

from tkinter import *

oyna=Tk()

oyna.title('Firdavs_Dev')

oyna.geometry('300x300')

natija=Label(text='Natija',bg='red')
natija.place(x=90,y=135,width=120,height=40)

xotalik=Label(text='Natija',bg='white',fg='white')

yil=Entry()
yil.place(x=75,y=50,width=150,height=30)

def farq():
    bugun=datetime.today()
    try:
        natija.config(text=bugun.year-int(yil.get()))
    except:
        xotalik.place(x=90,y=185,width=120,height=40)
        xotalik.config(text='Iltimos faqat \ntug\'ilgan yilizi kriting',fg='red')

tugma=Button(text="Hisoblash",command=farq,)
tugma.place(x=90,y=90,width=120,height=40)

#Firdavs_Dev

oyna.mainloop()