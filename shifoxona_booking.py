from tkinter import *

count_c=0
count_j=0
count_p=0

def next():
   global  count_c,count_j,count_p
   s=en_fam.get()
   si=en_im.get()
   sgr=en_group.get()
   if rad.get()==1:
      count_c=count_c+1
      s1=str(count_c)+"."+s+" "+si+". "+ " - "+sgr+"\n"
      v=str(count_c)+".0"
      tx_c.insert(v,s1)
   elif rad.get()==2:
      count_j=count_j+1
      s1=str(count_j)+"."+s+" "+si+". "+"- "+sgr+"\n"
      v = str(count_j) + ".0"
      tx_j.insert(v, s1)
   elif rad.get()==3:
      count_p=count_p+1
      s1=str(count_p)+"."+s+" "+si+". "+"- "+sgr+"\n"
      v = str(count_p) + ".0"
      tx_p.insert(v, s1)
   else:
      print("Javob yo\'q")
   en_fam.delete(0,END)
   en_im.delete(0, END)
   en_group.delete(0, END)
   en_fam.focus_set()
   
root=Tk()

root.title("Shifoxona")
root.geometry("1100x200+300+300")
fr1=LabelFrame(root,text="Shifokor: ",relief=RAISED,borderwidth=1)
fr1.pack(fill=BOTH,expand=0,side=LEFT,anchor="nw")
fr2=LabelFrame(root,text="Oğir darajadagi bemor",relief=RAISED,borderwidth=1)
fr2.pack(fill=X,expand=0,side=LEFT,anchor="nw")
fr3=LabelFrame(root,text="O\'rta darajadagi bemor",relief=RAISED,borderwidth=1)
fr3.pack(fill=X,expand=0,side=LEFT,anchor="nw")
fr4=LabelFrame(root,text="Yengil darajadagi bemor",relief=RAISED,borderwidth=1)
fr4.pack(fill=X,expand=1,side=LEFT,anchor="nw")
l_fam=Label(fr1,text="Familiya",width=7,font=("Arial",12))
l_fam.grid(row=0,columnspan=2)
fam=StringVar
en_fam=Entry(fr1,textvariable=fam)
en_fam.grid(row=0,column=2,columnspan=3,padx=15)
l_im=Label(fr1,text="Ismi",width=7,font=("Arial",12))
l_im.grid(row=1,columnspan=2)
im=StringVar
en_im=Entry(fr1,textvariable=im)
en_im.grid(row=1,column=2,columnspan=3,padx=15)
l_group=Label(fr1,text="Gruhi",width=7,font=("Arial",12))
l_group.grid(row=2,columnspan=2)
group=StringVar
en_group=Entry(fr1,textvariable=group)
en_group.grid(row=2,column=2,columnspan=3,padx=15)
rad=IntVar()
rad.set(0)
r=Radiobutton(fr1,text="Og\'ir",variable=rad,value=1)
r.grid(row=3,column=2)
r1=Radiobutton(fr1,text="O\'rta",variable=rad,value=2)
r1.grid(row=3,column=3)
r2=Radiobutton(fr1,text="Yengil",variable=rad,value=3)
r2.grid(row=3,column=4)
tx_c=Text(fr2,width=30,height=10,fg="red",wrap=WORD)
tx_c.pack(side=TOP)
tx_j=Text(fr3,width=30,height=10,fg="blue",wrap=WORD)
tx_j.pack(side=TOP)
tx_p=Text(fr4,width=30,height=10,fg="green",wrap=WORD)
tx_p.pack(side=TOP)
b_ex=Button(fr1,text="Chiqish",command=quit)
b_ex.grid(row=4,column=4,pady=10)
b_nex=Button(fr1,text="Qushish",command=next)
b_nex.grid(row=4,column=3,pady=10)

root.mainloop()

