from captcha.image import ImageCaptcha

image = ImageCaptcha(width=240,height=90)
captcha_text = 'asadsad0'

data = image.generate(captcha_text)
image.write(captcha_text,'rasmda.png')