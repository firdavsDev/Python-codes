import pyttsx3
engine = pyttsx3.init()
b=True
i=0
while True:
    i=i+1
    if i==5:
        print('good bye')
        break
    inpu=input('WRITE ')
    engine.say(inpu)
    engine.runAndWait()
