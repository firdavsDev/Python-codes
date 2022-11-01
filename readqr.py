import cv2
import pyzbar

img=cv2.imread('qrcod.png')

cod=pyzbar.decode(img)

for code in cod:
    resul=code.data.decode('utf-8')
print(resul)