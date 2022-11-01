import qrcode

txt=input('Matn nomi? ')

qr=qrcode.make(txt)
qr.save('qrcod.png')
