from PIL import Image,ImageDraw,ImageFont
from random import randint

def new_func():
    img=Image.open('sample.png')
    draw=ImageDraw.Draw(img)
    name=ImageFont.truetype(size=55)
    text=input('ismingiz? ')
    draw.text((((600-len(text)*20)/2),280),text,font=name)
    img.save('uzgardi.png')
    img.show()

new_func()