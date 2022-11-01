import socket
import threading

#kannalni ulaymiz
HOST='127.0.0.1'
PORT=8000

#ulaymiz
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

#boglaymiz
server.listen()


clints = []
nicknames= []

def broadcast(message):
    for clint in clints:
        clint.send(message)

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nickname[clints.index(client)]}")
            broadcast(message)
        except Exception:
            index=clints.index(client)
            clints.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:
        clint, address = server.accept()
        print(f"Bog'landi bilan {str(address)}!")

        clint.send('SALOM'.encode('utf-8'))
        nickname=clint.recv(1024)

        nicknames.append(nickname)
        clints.append(clint)
        print(f"Nickname of the clint is{nickname}")
        broadcast(f"{nickname} connected to server! \n ".encode('utf-8'))
        clint.send('Connected server'.encode('utf-8'))

        thread= threading.Thread(target=handle, args=(clint))
        thread.start()
print('server running...')
receive()