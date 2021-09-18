import calendar
import random
import re
from time import strftime
from playsound import playsound
from gtts import gTTS
import webbrowser
import os
import wikipedia
import datetime
from pyjokes import pyjokes
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("you say:")
       audio = r.listen(source)

    try:
        speech = r.recognize_google(audio)
        print("you say:" + speech)
        return speech
    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError:
         return 'error'

def say(text):
          voice = gTTS(text, lang="en",slow=False)
          unique_filename = "audio_" + str(random.randint(0,100000)) + ".mp3"
          voice.save(unique_filename)

          playsound.playsound(unique_filename)
          os.remove(unique_filename)
          print("J.A.R.V.I.S: " , text)


def handmassage(message):
          if "what is your name" and "what's your name" in message:
             say("My name is David.I'm Artificial Intelligence ")
          elif "hey David" in message:
             say("Yes sir.")
          elif  "play music whatever you want" in message:
              os.startfile("C:\\Users\\User\\Desktop\\mp3\\Neffex Fight.mp3")
          elif "play concert" in message:
                os.startfile("C:\\Users\\User\\Downloads\\Telegram Desktop\\dizayn2020.mp4")
          elif "movie Avengers" in message :
               os.startfile("C:\\Users\\User\\Downloads\\Telegram Desktop\\Avengers.Age.of.Ultron.mp4")
          elif "thank you" in message:
               say("You are welcome sir")
          elif "play my favorite song" in message:
              os.startfile("C:\\Users\\User\\Desktop\\mp3\\withoutme.mp3")
              say('Eminem, song without me.')
          elif "tell me a joke" in message:
              say(pyjokes.get_joke())
          elif "i'm bad" and "i'm not good" in message:
               say("I'm sorry to hear that")
          elif "what can you" in message:
                  say("I can write txt file , send e-mail massage,play vedio on youtube,open computer programms")
          elif  "open google".lower() in message:
             say("Okay sir")
             url = "https://www.google.com/webhp?authuser=1"
             webbrowser.open(url)
          elif "today's weather".lower() in message:
                webbrowser.open('https://obhavo.uz')
          elif "news" in message:
                say("News of Uzbekistan")
                webbrowser.open('https://kun.uz/uz/news/list')
          elif "location" in message:
               reg_ex = re.search('location (.+)', message)
               if reg_ex:
                   domain = reg_ex.group(1)
                   print(domain)
                   url = 'https://google.nl/maps/place/' + domain + '/&amp;'
                   webbrowser.open(url)
                   say(domain)
          elif "tell me" in message:
               reg_ex = re.search('tell me(.+)', message)
               if reg_ex:
                  domain = reg_ex.group(1)
                  print(domain)
                  url = 'https://www.google.com/search?q=' + domain
                  webbrowser.open(url)
                  say('Search ' + domain)
          elif "who is"  in message:
                   person = get_Person(message)
                   wiki = wikipedia.summary(person, sentences=4)
                   command = ' ' + wiki
                   say(command)
          elif 'current time' in message:
                 now = datetime.datetime.now()
                 say('Current time is %d hours %d minutes' % (now.hour, now.minute))
          elif 'what is' in message:
                 thing = get_Person(message)
                 wiki = wikipedia.summary(thing, sentences=4)
                 command = ' ' + wiki
                 say(command)
          elif "what date" in message:
                now = datetime.datetime.now()
                my_date = datetime.datetime.today()
                weekday = calendar.day_name[my_date.weekday()]  # e.g. Monday
                monthNum = now.month
                dayNum = now.day
                month_names = ['January', 'February', 'March', 'April', 'May',
                       'June', 'July', 'August', 'September', 'October', 'November',
                       'December']
                ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th',
                          '7th', '8th', '9th', '10th', '11th', '12th',
                          '13th', '14th', '15th', '16th', '17th',
                          '18th', '19th', '20th', '21st', '22nd',
                          '23rd', '24th', '25th', '26th', '27th',
                          '28th', '29th', '30th', '31st']

                der ='Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'
                say(der)
          elif "hello"  in message:
              day_time = int(strftime('%H'))
              if day_time < 12:
                     say('Hello Sir. Good morning')
              if 12 <= day_time < 18:
                    say('Hello Sir. Good afternoon')
              else:
                 say('Hello Sir. Good evening')
          elif "no" in message:
                      say("telegram")
          elif "play video" in message:
                reg_ex = re.search('play video (.+)', message)
                if reg_ex:
                        domain = reg_ex.group(1)
                        print(domain)
                        url = 'https://www.youtube.com/results?search_query=' + domain
                        webbrowser.open(url)
                        say('play video' + domain)
          elif "bye" and "bye-bye" and "goodbye" in message:
             finish()

          else:
                   say("What.")



def get_Person(text):
        wordlist = text.split()
        for i in range(0, len(wordlist)):
            if i + 3 <= len(wordlist) - 1 and  wordlist[i].lower() == 'who' and wordlist[i + 1].lower() == 'is':
                return wordlist[i - 2] + ' ' + wordlist[i + 3]
        for i in range(0, len(wordlist)):
            if i + 2 <= len(wordlist) - 1 and  wordlist[i].lower() == 'what' and wordlist[i + 1].lower() == 'is':
                return wordlist[i - 2] + ' ' + wordlist[i + 3]



def finish():
    say("good bye sir")
    exit()




if __name__  ==  '__main__':
        print("J.A.R.V.I.S.")

while True:
      command = listen()
      handmassage(command)
