from tkinter import *
from tkinter import messagebox
from tkcalendar import *

r = Tk()
r.title("my calendar")

cal = Calendar(r, selectmode="day", year=2020, moth=6, day=8)
cal.grid(row=0, column=0)

c = Entry()
c.grid(row=5, column=0)


def abcc():
    messagebox.showinfo(
        "info", "bu dasturdan kalendar sifatida foydalanishingz mumkn \nva kunni belgilab usha kunga eslatmalaringizni saqlab qoyishingz mumkn")


d = Button(text="qo'llanma", command=abcc)
d.grid(row=5, column=4)

my = Listbox(r)

my.grid(row=0, column=4)


def aka():
    myy = []
    myy.append((str(c.get())+" "+str(cal.get_date())))

    for i in myy:
        my.insert(0, i)


def cl():
    my.delete(ANCHOR)


lll = Label(text="eslatmangizni yozing ")
lll.grid(row=3, column=0)
t = Button(r, text="eslatma saqlash",bg='green',command=aka)
t.grid(row=6, column=0)

k = Button(text="clear", command=cl)
k.grid(row=1, column=4)


r.mainloop()

