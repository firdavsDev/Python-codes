from time import strftime
from tkinter import *
from tkinter import ttk
from pathlib import Path
from PIL import ImageTk,Image
from playsound import playsound

from db import PostConnect
import psycopg2

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Alarm:
    #YAngi oyna about
    def yangi_oyna(self):
        top = Toplevel()
        top.title('Biz haqimizda')
        top.geometry('700x700')
        img = Image.open("qrcod.png")
        res = img.resize((250,188),Image.ANTIALIAS)
        self.my_img = ImageTk.PhotoImage(res)
        Label(top,image=self.my_img).pack()
        Button(top,text='Yopish',command=top.destroy,bg='red',fg='blue').place(x=320,y=500)




    def __init__(self,root):
        self.root=root
        self.root.title('Budilnik')
        self.root.geometry("1450x900")


        #____________ TITLE ____________

        self.title=Label(self.root,font=('ds-digital',20),background='blue',foreground='red')
        self.title.pack(side=TOP,fill=X)
        self.title.config(padx=65,pady=30)



        #_________________  Parametrlar
        # self.ID=StringVar()
        self.Ism_var=StringVar()
        self.soat_var=StringVar()
        self.min_var=StringVar()

        #------------------Manage ============
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Manage_Frame.place(x=30,y=120,width=450,height=570)

        m_title=Label(Manage_Frame,text='Budilnik qo\'shish',bg='crimson',fg='white',font=('times new roman',30,'bold'))
        m_title.grid(row=0,columnspan=2,pady=10)

        #Name
        lbl_name=Label(Manage_Frame,text='Ism:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_name.grid(row=2,column=0,sticky="w",pady=10,padx=20)

        txt_name=Entry(Manage_Frame,textvariable=self.Ism_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,sticky="w",pady=10,padx=20)


        #Soat
        lbl_kurs=Label(Manage_Frame,text='Soat:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_kurs.grid(row=4,column=0,sticky="w",pady=10,padx=20)

        combo_kurs=ttk.Combobox(Manage_Frame,textvariable=self.soat_var,font=('times new roman',13,'bold'),state='readonly')
        lis = [i for i in range(1,25)]
        combo_kurs['values']=(lis)
        combo_kurs.grid(row=4,column=1,padx=20,pady=10)

        #minute
        lbl_minute=Label(Manage_Frame,text='Minut:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_minute.grid(row=5,column=0,sticky="w",pady=10,padx=20)

        combo_minute=ttk.Combobox(Manage_Frame,textvariable=self.min_var,font=('times new roman',13,'bold'),state='readonly')
        lis = [i for i in range(1,61)]
        combo_minute['values']=(lis)
        combo_minute.grid(row=5,column=1,pady=10,padx=20)



        ################################# Tugma ########################

        BTN_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg='crimson')
        BTN_Frame.place(x=15,y=500,width=420)

        #Tugma qushish un
        addbtn=Button(BTN_Frame,text='Qo\'shish',width=55,command=self.addbtn).grid(row=0,column=0,padx=10,pady=10)



        #======================================================== detail frame ==============================================
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Detail_Frame.place(x=650,y=100,width=770,height=580)


        ruyhat=Label(Detail_Frame,text='Ro\'yxatlar',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        ruyhat.grid(row=0,column=0,sticky="w",pady=10,padx=20)

        searchbtn=Button(Detail_Frame,command=self.yangi_oyna,text='About',width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,command=self.soat,text='Hammasi',width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)


        #################################### TABLE FRAME =================================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='crimson')
        Table_Frame.place(x=10,y=70,width=750,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=('ID',"Ism",'Vaqt'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("ID",text="ID")
        self.Student_table.heading("Ism",text="Ism")
        self.Student_table.heading("Vaqt",text="Vaqt")
        self.Student_table['show']='headings'
        self.Student_table.column("ID",width=100)
        self.Student_table.column("Ism",width=100)
        self.Student_table.column("Vaqt",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.shows()

    ##############Funksiyalar

    #data funksiya
    def sana(self):
        # datem = strftime('%B-%A-%d-%Y')
        datem = strftime('%B-%A-%d-%Y %H:%M:%S %p')
        # datem = strftime('%X')
        self.title.config(text=datem)
        self.title.after(1000,self.sana)
    
    #add button alarmclock
    def addbtn(self):
        name = self.Ism_var.get()
        H = self.soat_var.get()
        M = self.min_var.get()
        #conect basa
        conn = psycopg2.connect(
            database = "alarm",
            user = "postgres",
            password = "2002",
            host = "localhost",
            port = "5432"
        )
        cur = conn.cursor()
        cur.execute(f"INSERT INTO budelnik(ism, vaqt) VALUES ('{name}','{H}:{M}')")
        conn.commit()
        self.shows()
        self.toza()
        cur.close()
        conn.close()

    def shows(self):
        conn = psycopg2.connect(
            database = "alarm",
            user = "postgres",
            password = "2002",
            host = "localhost",
            port = "5432"
        )
        cur = conn.cursor()
        cur.execute("select * from budelnik")
        # cur.execute("delete from budelnik where id>=8 and id<=24")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values = row)
            conn.commit()
        cur.close()
        conn.close()


    def toza(self):
        self.Ism_var.set("")
        self.soat_var.set("")
        self.min_var.set("")

    def soat(self):
        conn = psycopg2.connect(
            database = "alarm",
            user = "postgres",
            password = "2002",
            host = "localhost",
            port = "5432"
        )
        cur = conn.cursor()
        cur.execute("select * from budelnik order by vaqt asc")
        rows = cur.fetchall()
        for row in rows:
            if row[2] == strftime('%X'):
                playsound('')

            print('vaqt buldi')
            break
        cur.close()
        conn.close()



if __name__ == '__main__':
    root=Tk()
    ob=Alarm(root)
    ob.sana()
    root.mainloop()