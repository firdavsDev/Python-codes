import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

window = tk.Tk()
window.title("Smart Translator - EN")
ww = window.winfo_reqwidth()
wh = window.winfo_reqheight()
pr = int(window.winfo_screenwidth()/2 - ww/2)
pd = int(window.winfo_screenheight()/2 - wh/2)
window.geometry("+{}+{}".format(pr, pd))
window.maxsize(width=340, height=300)
window.minsize(width=340, height=300)
text = tk.StringVar()
result_lan = 'en'
def select():
    global result_lan
    if(var.get()==1):
        lbl.config(text = 'Textni kiriting:')
        result_lan = 'uz'
        btn2['text']='TOZALASH'
        lan_select['text']='Tilni tanlang'
        window.title("Aqlli Tarjimon - UZ")
 
    elif(var.get()==2):
        lbl.config(text = 'Введите текст:')
        result_lan = 'ru'
        btn2['text']='ОЧИСТКА'
        lan_select['text']='Язык'
        window.title("Умный переводчик - RU")
        
    elif(var.get()==3):
        lbl.config(text = 'Enter the text:')
        result_lan = 'en'
        btn2['text']='CLEAR'
        lan_select['text']='Language'
        window.title("Smart Translator - EN")
        
def function(obj1,obj2,button=str()):
    from PyDictionary import PyDictionary
    from googletrans import Translator
    dictionary = PyDictionary()
    translator = Translator()
    global text,result_lan
    if(button=='ok'):
        txt = obj1.get()
        if(result_lan=='en'):
            result = 'Translate result:\n --------------------------- \n'
            result += 'Text: '+txt+'\n\n'+'Mean: '+str(dictionary.meaning(txt)['Noun'])+'\n\n'+'Antonym: '+str(dictionary.antonym(txt))+'\n\n'+'Synonym: '
            result += str(dictionary.synonym(txt))+'\n\n'+'Translate UZ: '+str(translator.translate(txt, src='en', dest='uz').text)+'\n\n'+'Translate RU: '+str(translator.translate(txt, src='en', dest='ru').text)

        elif(result_lan=='uz'):
            try:
                mean1 = str(translator.translate(txt, src='uz', dest='en').text)
                mean1 = str(dictionary.meaning(mean1)['Noun'])
                mean1 = str(translator.translate(mean1, src='en', dest='uz').text)
            except:
                pass

            try:
                antonim1 = str(translator.translate(txt, src='uz', dest='en').text)
                antonim1 = str(dictionary.antonym(antonim1))
                antonim1 = str(translator.translate(antonim1, src='en', dest='uz').text)
            except:
                pass

            try:
                sinonim1 = str(translator.translate(txt, src='uz', dest='en').text)
                sinonim1 = str(dictionary.synonym(sinonim1))
                sinonim1 = str(translator.translate(sinonim1, src='en', dest='uz').text)
            except:
                pass

            try:
                tarjima_en1 = str(translator.translate(txt, src='uz', dest='en').text)
            except:
                pass

            try:
                tarjima_ru1 = str(translator.translate(txt, src='uz', dest='ru').text)
            except:
                pass

            result = 'Tarjima natijasi:\n --------------------------- \n'
            result += 'Text: '+txt+'\n\n'+'Anglatadi: '+mean1+'\n\n'+'Antonim: '+antonim1+'\n\n'+'Sinonim: '
            result += sinonim1+'\n\n'+'Tarjima EN: '+tarjima_en1+'\n\n'+'Tarjima RU'+': '+tarjima_ru1
            
        elif(result_lan=='ru'):
            t = 'UZ'
            try:
                mean1 = str(translator.translate(txt, src='ru', dest='en').text)
                mean1 = str(dictionary.meaning(mean1)['Noun'])
                mean1 = str(translator.translate(mean1, src='en', dest='ru').text)
            except:
                pass

            try:
                antonim1 = str(translator.translate(txt, src='ru', dest='en').text)
                antonim1 = str(dictionary.antonym(antonim1))
                antonim1 = str(translator.translate(antonim1, src='en', dest='ru').text)
            except:
                pass

            try:
                sinonim1 = str(translator.translate(txt, src='ru', dest='en').text)
                sinonim1 = str(dictionary.synonym(sinonim1))
                sinonim1 = str(translator.translate(sinonim1, src='en', dest='ru').text)
            except:
                pass

            try:
                tarjima_en1 = str(translator.translate(txt, src='ru', dest='en').text)
            except:
                pass

            try:
                tarjima_uz1 = str(translator.translate(txt, src='ru', dest='uz').text)
            except:
                pass
   
            result = 'Результат перевода:\n --------------------------- \n'
            result += 'Текст: '+txt+'\n\n'+'Объясняет: '+mean1+'\n\n'+'Антоним: '+antonim1+'\n\n'+'Синоним: '
            result += sinonim1+'\n\n'+'Перевод EN: '+tarjima_en1+'\n\n'+'Перевод UZ: '+': '+tarjima_uz1



        try:
            obj2.delete('1.0', tk.END)
        except:
            pass
        obj2.insert(tk.INSERT, result)

    elif(button=='cl'):
        obj2.delete('1.0', tk.END)
        text.set('')

frame = ttk.Frame(window)
frame.grid(column=1, row=0, pady=10, sticky='W')
lbl = ttk.Label(frame, text="Enter the text:")
lbl.grid(column=0, row=0)
Edit = ttk.Entry(frame, textvariable=text)
Edit.grid(column=1, row=0, columnspan=1)
ttk.Label(frame, text="\n").grid(column=2, row=0, sticky='W')

scrol = scrolledtext.ScrolledText(window, width=37, height=11, wrap=tk.WORD, relief="solid",highlightbackground="black", highlightcolor="black", highlightthickness=0)
scrol.grid(column=0, row=1, rowspan=100, pady=10, padx=15, columnspan=100)
scrol.insert(tk.INSERT, "App Author: Matyoqubov Firdavs\nCreated: 27.09.2020")

btn1 = ttk.Button(frame, text='OK', command=lambda: function(Edit,scrol,button='ok'))
btn1.grid(column=0, row=1, sticky='W')
btn2 = ttk.Button(frame, text='CLEAR', command=lambda: function(Edit,scrol,button='cl'))
btn2.grid(column=1, row=1, sticky='W', padx=5)
ttk.Label(frame, text="  \n").grid(column=2, row=1, sticky='W')

lan_select = ttk.LabelFrame(window, text='Language')
lan_select.grid(column=0, row=0, padx=10, pady=5, sticky='W', rowspan=4)

var = tk.IntVar()
R1 = ttk.Radiobutton(lan_select, text="Uzbek", variable=var, value=1,
              command=select)
R1.pack(anchor = 'w')

R2 = ttk.Radiobutton(lan_select, text="Русский", variable=var, value=2,
              command=select)
R2.pack(anchor = 'w')

R3 = ttk.Radiobutton(lan_select, text="English", variable=var, value=3,
              command=select)
R3.pack(anchor = 'w')
window.mainloop()
#messagebox.showinfo('App','Author: Matyoqubov Firdavs\nCreated: 27.09.2020')
