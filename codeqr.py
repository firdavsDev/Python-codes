import qrcode

txt=input('matn nomi? ')

qr=qrcode.make(txt)
qr.save('qrcod.png')