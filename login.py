import sqlite3 as db
from tkinter import *

#malumot bazasini yasaymiz
conn=db.connect('sampler.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS DATA
(
    Fname TEXT,
    Lname TEXT,
    Gname TEXT
)''')
cur.close()
conn.commit()
conn.close()

#ulaymiz dataga 
def put():
    conn=db.connect('sampler.db')
    cur=conn.cursor()
    cur.execute("insert into DATA values('%s','%s','%s')"%(fname.get(),lname.get(),gname.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Bazaga qushildi')


#GUI yasaymiz
master = Tk()

#variableni yasaymiz
fname=StringVar()
lname=StringVar()
gname=StringVar()
status=StringVar()

Label(master,text='Jinsi: ').grid(row=2,column=0)
Label(master,text='ISMIZ: ').grid(row=0,column=0)
Label(master,text='Familyayiz: ').grid(row=1,column=0)
Label(master,text='',textvariable=status).grid(row=4,columnspan=2)

#enetry yasaymiz inpute olish uchun
Entry(master,textvariable=fname).grid(row=0,column=1)
Entry(master,textvariable=lname).grid(row=1,column=1)
Entry(master,textvariable=gname).grid(row=2,column=1)


#tugma yasaymiz
Button(master,text='Yuborish',command=put).grid(row=3,columnspan=2)

mainloop()