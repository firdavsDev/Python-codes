from tkinter import *
from tkinter import messagebox
form = Tk()
i = StringVar()
c = ""

class program:
    class main:
        class events:
            class onclick:
                
                def setnum(n):
                    global i
                    global c
                    c+=str(n)
                    i.set(c)

                def error(self):
                    global i
                    global c
                    messagebox.showerror("Syntax Error", "Invaid Syntax")
                    i.set("")
                    c=""
                    
                def clear(self):
                    global i
                    global c
                    c = ""
                    i.set(c)
                    

                def calculate(edit1):
                    global i
                    global c
                    try:
                        c = str(eval(c)) 
                        i.set(c)  
                    except:
                        program.main.events.onclick.error()

        def widgets(form, i, c):
            i.set("             Welcome - Calculator")
            edit1 = Entry(form, border=0, width=33, textvariable=i, relief="ridge", highlightbackground="black", highlightcolor="black", highlightthickness=2)             
            button1 = Button(form, text='1', fg='black', bg='gray', relief="ridge", highlightbackground="black",
                             highlightcolor="black", highlightthickness=2, command=lambda: program.main.events.onclick.setnum(1), height=0, width=3)            
            button2 = Button(form, text='2', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(2), height=0, width=3)             
            button3 = Button(form, text='3', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(3), height=0, width=3)             
            button4 = Button(form, text='4', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(4), height=0, width=3)             
            button5 = Button(form, text='5', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(5), height=0, width=3)             
            button6 = Button(form, text='6', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(6), height=0, width=3)                         
            button7 = Button(form, text='7', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(7), height=0, width=3)                         
            button8 = Button(form, text='8', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(8), height=0, width=3)                         
            button9 = Button(form, text='9', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                             highlightthickness=2, command=lambda: program.main.events.onclick.setnum(9), height=0, width=3)                         
            button10 = Button(form, text='0', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum(0), height=0, width=3)                         
            button11 = Button(form, text='.', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum("."), height=0, width=3)                         
            button12 = Button(form, text='C', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.clear(), height=0, width=3)            
            button13 = Button(form, text=')', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum(")"), height=0, width=3)         
            button14 = Button(form, text='+', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum("+"), height=0, width=3)           
            button15 = Button(form, text='-', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum("-"), height=0, width=3)             
            button16 = Button(form, text='*', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum("*"), height=0, width=3)          
            button17 = Button(form, text='/', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum("/"), height=0, width=3)          
            button18 = Button(form, text='(', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.setnum("("), height=0, width=3)           
            button19 = Button(form, text='=', fg='black', bg='gray', relief="ridge", highlightbackground="black", highlightcolor="black",
                              highlightthickness=2, command=lambda: program.main.events.onclick.calculate(edit1), height=0, width=28)
            
            edit1.grid(columnspan=100, padx=5, pady=5)
            button1.grid(row=2, column=0, pady=4, padx=6)
            button2.grid(row=2, column=1, pady=4, padx=2)
            button3.grid(row=2, column=2, pady=4, padx=2)
            button4.grid(row=2, column=3, pady=4, padx=2)
            button5.grid(row=2, column=4, pady=4, padx=2)
            button6.grid(row=2, column=5, pady=4, padx=2)
            button7.grid(row=3, column=0, pady=4, padx=6)
            button8.grid(row=3, column=1, pady=4, padx=2)
            button9.grid(row=3, column=2, pady=4, padx=2)
            button10.grid(row=3, column=3, pady=4, padx=2)            
            button11.grid(row=3, column=4, pady=4, padx=2)
            button12.grid(row=3, column=5, pady=4, padx=2) 
            button13.grid(row=4, column=5, pady=4, padx=2) 
            button14.grid(row=4, column=0, pady=4, padx=6) 
            button15.grid(row=4, column=1, pady=4, padx=2)
            button16.grid(row=4, column=2, pady=4, padx=2) 
            button17.grid(row=4, column=3, pady=4, padx=2) 
            button18.grid(row=4, column=4, pady=4, padx=2)
            button19.grid(columnspan=50, row=5, column=0, pady=4, padx=7)
            #program.bind("<1>", program.main.events.onclick.setnum(1))
            
        def run(form, i, c):
            ww = form.winfo_reqwidth()
            wh = form.winfo_reqheight()
            pr = int(form.winfo_screenwidth()/2 - ww/2)
            pd = int(form.winfo_screenheight()/2 - wh/2)
            form.geometry("+{}+{}".format(pr, pd))
            form.configure(background="gray")
            form.title("Calculator")
            form.maxsize(width=234, height=180)
            form.minsize(width=234, height=180)
            program.main.widgets(form, i, c)
            messagebox.showinfo("Calcuator","Program author:Firdavs")
            form.mainloop()
            #program.main.events.onclick.exit(form)

program.main.run(form, i, c)
