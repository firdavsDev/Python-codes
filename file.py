import string

# def top(Ism:str)->str:
#     '''BU funksiya'''
#     try:
#         neww=Ism.title()
#         doc = open("text.txt", "a")
#         doc.write('\n'+neww)
#         return 'Yozildi'
#     except Exception:
#         if Ism.isdigit():
#             raise Exception('Xato') 
#         return 'Faqat string bering'
#     finally:
#         doc.close()

# Ism=input('Ism bering ')

# print(top(Ism))
input pathlip

p=Path('.')
p.mkdir('meedi')


def yoz(txt:str):
    try:
        with open('tex.txt','a+') as file:
            file.writelines(txt+'\n')
            tt=file.read()
            print('sizda borlar',tt)
    except Exception as e:
        print('Xato')

t=open('tex.txt','r')
while True:
    # print('Sizda bor uquvchilar ',t.read())
    inn=input('Uquvchi qushishni istaysizmi ? ')
    if inn=='Yuq':
        break
    txt=input('Uquvchi ismi ')
    yoz(txt)
