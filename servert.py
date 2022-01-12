import socket
from threading import Thread
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost",1586))

s.listen(10)

Players=[]

first_Join_Massage = "Comfirmed"

while True:
    clies , addr = s.accept()
    Players.append(clies)

    if len(Players) == 2:
        for i in Players:
            i.send(first_Join_Massage.encode())

        break

print("runned")
def BroadCast(sk,msg):
    sk.send(msg)

def Getplayer1():
    while True:
        a = Players[0].recv(4096)
        f = pickle.loads(a)
        BroadCast(Players[1],a)
        print(f)

def Getplayer2():
    while True:
        a = Players[1].recv(4096)
        f = pickle.loads(a)
        BroadCast(Players[0],a)
        print(f)


Thread(target=Getplayer1).start()
Thread(target=Getplayer2).start()
