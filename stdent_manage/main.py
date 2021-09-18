from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title('Malika education')
        self.root.geometry("1350x700+0+0")

        #_____________TITLE____________
        title=Label(self.root, text="Malika education", relief=GROOVE ,font=('times new roman',40,'bold'),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #=================== Parametrlar =================
        self.Yosh_var=StringVar()
        self.Ism_var=StringVar()
        self.Familya_var=StringVar()
        self.Kurs_var=StringVar()
        self.Number_var=StringVar()
        self.Vaqti_var=StringVar()
        

        #------------------Manage ============
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Manage_Frame.place(x=20,y=100,width=450,height=570)

        m_title=Label(Manage_Frame,text='Talabalar ro\'yhati',bg='crimson',fg='white',font=('times new roman',30,'bold'))
        m_title.grid(row=0,columnspan=2,pady=10)

        #ROLL
        lbl_roll=Label(Manage_Frame,text='Yosh:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_roll.grid(row=1,column=0,sticky="w",pady=10,padx=20)

        txt_roll=Entry(Manage_Frame,textvariabl=self.Yosh_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,sticky="w",pady=10,padx=20)

        #Name
        lbl_name=Label(Manage_Frame,text='Ism:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_name.grid(row=2,column=0,sticky="w",pady=10,padx=20)

        txt_name=Entry(Manage_Frame,textvariable=self.Ism_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,sticky="w",pady=10,padx=20)

        #Email
        lbl_email=Label(Manage_Frame,text='Familya:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_email.grid(row=3,column=0,sticky="w",pady=10,padx=20)

        txt_email=Entry(Manage_Frame,textvariable=self.Familya_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,sticky="w",pady=10,padx=20)

        #kurs
        lbl_kurs=Label(Manage_Frame,text='Kurs:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_kurs.grid(row=4,column=0,sticky="w",pady=10,padx=20)

        combo_kurs=ttk.Combobox(Manage_Frame,textvariable=self.Kurs_var,font=('times new roman',13,'bold'),state='readonly')
        combo_kurs['values']=('Ona tili',"Matimatika","Ingliz tili")
        combo_kurs.grid(row=4,column=1,padx=20,pady=10)

        # txt_kurs=Entry(Manage_Frame,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        # txt_kurs.grid(row=3,column=1,sticky="w",pady=10,padx=20)


        #contact
        lbl_contact=Label(Manage_Frame,text='Number:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_contact.grid(row=5,column=0,sticky="w",pady=10,padx=20)

        txt_contact=Entry(Manage_Frame,textvariable=self.Number_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,sticky="w",pady=10,padx=20)

        # Dod
        lbl_Dod=Label(Manage_Frame,text='Vaqti :',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_Dod.grid(row=6,column=0,sticky="w",pady=10,padx=20)

        txt_Dod=Entry(Manage_Frame,textvariable=self.Vaqti_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_Dod.grid(row=6,column=1,sticky="w",pady=10,padx=20)

        # MAnzil
        lbl_Adres=Label(Manage_Frame,text='Manzil:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_Adres.grid(row=7,column=0,sticky="w",pady=10,padx=20)

        self.txt_Adres=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Adres.grid(row=7,column=1,sticky="w",pady=10,padx=20)

        ################################# BUTTON ########################

        BTN_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg='crimson')
        BTN_Frame.place(x=15,y=500,width=420)

        addbtn=Button(BTN_Frame,text='Qushish',width=10).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(BTN_Frame,text='Yangilash',width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(BTN_Frame,text='O\'chirish',width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(BTN_Frame,text='Tozalash',width=10).grid(row=0,column=3,padx=10,pady=10)


        #==================================================================== detail frame ==============================================
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Detail_Frame.place(x=500,y=100,width=765,height=580)


        lbl_Search=Label(Detail_Frame,text='Qidirish:',bg='crimson',fg='white',font=('times new roman',20,'bold'))
        lbl_Search.grid(row=0,column=0,sticky="w",pady=10,padx=20)

        
        combo_search=ttk.Combobox(Detail_Frame,width=10,font=('times new roman',13,'bold'),state='readonly')
        combo_search['values']=('Yosh',"Ism","Number")
        combo_search.grid(row=0,column=1,padx=20,pady=10)


        txt_search=Entry(Detail_Frame,width=20,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,sticky="w",pady=10,padx=20)

        searchbtn=Button(Detail_Frame,text='Qidirish',width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        


        #################################### TABLE FRAME =================================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='crimson')
        Table_Frame.place(x=10,y=70,width=745,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_Frame,columns=('Yosh',"Ism",'Familya','Kurs','Number','dob','Manzil'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Yosh",text="Yoshi")
        Student_table.heading("Ism",text="Ism")
        Student_table.heading("Familya",text="Familya")
        Student_table.heading("Kurs",text="Kurs")
        Student_table.heading("Number",text="Number")
        Student_table.heading("dob",text="Vaqt")
        Student_table.heading("Manzil",text="Manzil")
        Student_table['show']='headings'
        Student_table.column("Yosh",width=100)
        Student_table.column("Ism",width=100)
        Student_table.column("Familya",width=100)
        Student_table.column("Kurs",width=100)
        Student_table.column("Number",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("Manzil",width=150)
        Student_table.pack(fill=BOTH,expand=1)

    # def add_students(self):
    #     con=pymysql.connect(host='localhost',user='root',password='',database='stm')

    # def add_student(self):
    #     con=pymysql.connect()

root=Tk()
ob=Student(root)
root.mainloop()