import pywhatkit as kit

import re

pat=r"gusht"
match=re.search(pat,"sasiskagushtlijuda")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

str="salom Menin ismim Davron. Salom Davron"

patt = r"Davron"
newstr= re.sub(patt,"Firdavs",str)
print(newstr) #salom Menin ismim Firdavs. Salom Firdavs




#Juda ham foydali ekan!!!

#kit.image_to_ascii_art('sample.png','samplee.text')