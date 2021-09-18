import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

#kannalni ulaymiz
HOST='127.0.0.1'
PORT=8000

class Client:
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname",'Iltimos niknamizni yozing',parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread=threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="gray")

        self.chat_label=tkinter.Label(self.win,text='Telegram: ', bg='gray')
        self.chat_label.config(font=('Arial',12))
        self.chat_label.pack(padx=20,pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20,pady=5)
        self.text_area.config(state='disable')

        self.msg_label=tkinter.Label(self.win,text='Xabar: ', bg='gray')
        self.msg_label.config(font=('Arial',12))
        self.msg_label.pack(padx=20,pady=5)

        self.inpute_are = tkinter.Text(self.win,height=3)
        self.inpute_are.pack(padx=20,pady=5)

        self.send_button=tkinter.Button(self.win,text="Send",command=self.write)
        self.send_button.config(font=('Arial',12))
        self.send_button.pack(padx=20,pady=5)

        self.gui_done=True

        self.win.protocol('WM_DELETE_WINDOW',self.stop)

        self.win.mainloop()


    def write(self):
        message=f"{self.nickname}: {self.inpute_are.get('1.0','end')}"
        self.sock.send(message.encode('utf-8'))
        self.inpute_are.delete('1.0','end')


    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message= self.sock.recv(1024)
                if message=="SALOM":
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end',message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disable')
                        
            except ConnectionAbortedError:
                break
            except :
                print("Error")
                self.sock.close()
                break
client=Client(HOST,PORT)