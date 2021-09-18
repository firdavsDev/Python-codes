from gtts import gTTS
import os 

fh = open('test.txt', 'r')
Text = fh.read().replace('\n', ' ')

til = 'ko'

output = gTTS(Text, lang = til, slow = False)

output.save('output.mp3')
fh.close()
os.system('start output.mp3')


