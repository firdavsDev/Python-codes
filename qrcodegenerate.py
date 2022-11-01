from tkinter import *
import qrcode 
from PIL import Image,ImageTk
from resizeimage import resizeimage

#kalss ochamiz
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title('Qr Generator by Davron')
        self.root.resizable(False,False)

        title=Label(self.root,text="Qr kod Generatori", font=('times new roman',40),bg="#053246",fg='white',anchor='w').place(x=0,y=0, relwidth=1)

        
        #variable
        self.var_emp_code=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_deparment=StringVar()
        self.var_destinition=StringVar()

        #Employee detailas
        emp_Frame=Frame(self.root, bd=2,relief=RIDGE, bg='white')
        emp_Frame.place(x=50,y=100, width=500, height=380)

        
        emp_title=Label(emp_Frame,text="Ishsizlar haqida", font=('goudy old style',20),bg="#043256",fg='white').place(x=0,y=0, relwidth=1)
        
        lbl_emp_code=Label(emp_Frame,text="Ishsizlar ID", font=('times new roman',15,'bold'),fg='black').place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Ism", font=('times new roman',15,'bold'),fg='black').place(x=20,y=100)
        lbl_deparment=Label(emp_Frame,text="Hukumat", font=('times new roman',15,'bold'),fg='black').place(x=20,y=140)
        lbl_desinition=Label(emp_Frame,text="Manzili", font=('times new roman',15,'bold'),fg='black').place(x=20,y=180)

        txt_emp_code=Entry(emp_Frame, font=('times new roman',15), textvariable=self.var_emp_code ,bg='lightyellow').place(x=200,y=60)
        txt_name=Entry(emp_Frame, font=('times new roman',15),textvariable=self.var_emp_name,bg='lightyellow').place(x=200,y=100)
        txt_deparment=Entry(emp_Frame,font=('times new roman',15),textvariable=self.var_emp_deparment,bg='lightyellow').place(x=200,y=140)
        txt_desinition=Entry(emp_Frame, font=('times new roman',15),textvariable=self.var_destinition, bg='lightyellow').place(x=200,y=180)
        
        #Tugmalar
        btn_generate=Button(emp_Frame,text='Qr Generator', command=self.generate, font=('times new roman',18,'bold'),bg='#2196f3',fg='white',).place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text='Tozalash', command=self.clear, font=('times new roman',18,'bold'),bg='#607d8b',fg='white',).place(x=290,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg, font=('times new roman',20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #Generate maydoni
        qr_Frame=Frame(self.root, bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100, width=250, height=380)

        
        qr_title=Label(qr_Frame,text="Ishsizlar QR kodi", font=('goudy old style',20),bg="#043256",fg='white').place(x=0,y=0, relwidth=1)

        self.qr_code=Label(qr_Frame,text='QR kod\n Mavjud emas',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_deparment.set('')
        self.var_destinition.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_destinition.get()=='' or self.var_emp_code.get()=='' or self.var_emp_deparment.get()=='' or self.var_emp_name.get()=='':
            self.msg="Hammasi tuldirilishi shart!!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Ishsizning ID: {self.var_emp_code.get()}\nIshsizning ismi: {self.var_emp_name.get()}\nHukumat: {self.var_emp_deparment.get()}\nIshsizning manzili: {self.var_destinition.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save('Ishsiz'+str(self.var_emp_code.get())+'.png')
            #qr codni yangilovchisi
            self.im=ImageTk.PhotoImage(file='Ishsiz'+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #bildirishnoma
            self.msg="QR kod bajarildi!!!"
            self.lbl_msg.config(text=self.msg,fg='green')


root=Tk()
obj=Qr_Generator(root)


root.mainloop()