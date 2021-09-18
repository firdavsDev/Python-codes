# from googletrans import Translator

# tr=Translator()

# #src buqaysi tildan avtomatik olingani
# #dest bu aftomatik englizchaga ugiradi
# #text tarjima qilingan matn

# suz=input("suz kiriting ")
# des=input("Qaysi tilga ? ")
# resul=tr.translate(suz, dest=des)

# print(resul.text)
from googletrans import Translator
translator = Translator()
s = input("Satrni kiriting: ")
des = input("Qaysi tilga tarjima qilsin: ")
src=input('qaysidan ')
res = translator.translate(s, dest=des,src=src)
print(res.text)