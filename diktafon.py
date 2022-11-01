import pyaudio as p
from tkinter import *
import wave
import time

tk = Tk()
tk.title("Mini-Diktafon")

tk.resizable(width=False, height=False)


con = Entry(tk, font='Segoe', width = 20, border=0, bg="#FAFBFD", justify="center")
end = Label(text = "", font='Comic')
start = Button(text='Yozuvni boshlash', font='Comic', width= 25, border=0, bg="#999")
# label.grid(row=0, column=0)
con.grid(row=1, column=0)
end.grid(row=2, column=0, pady=10,)
start.grid(row=3, column=0, sticky=W, padx=20, pady=20)



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100 # Chastota
RECORD_SECONDS = T
WAVE_OUTPUT_FILE_NAME = f"{int(time.time())}.wav"


stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)



stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open(WAVE_OUTPUT_FILE_NAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writefram