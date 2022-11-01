import os
from win10toast import ToastNotifier

def bildir():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    app=ToastNotifier()
    
    tit='Bildirishnoma'
    xx='Assalom alaykum'
    len=30
    app.show_toast(tit,xx,duration=len)

bildir()
