import random
import socket
from threading import Thread
import pickle
from tkinter import *


Code_M_Ls = []

root = Tk()

def Exit_app_Comm():
    root.destroy()

def Create_Game_Room():
    Code_M_Ls.append(Port_Select.get())
    Ip_Enco_Shower.config(text=Join_Code)


Join_Code = socket.gethostbyname(socket.gethostname())
print(Join_Code)

Ip_Enco_Shower = Label(root,text="Game Code Will Apear Here")
Ip_Enco_Shower.grid(row=1,column=1)

port_Lab = Label(root,text="Port :-").grid(row=2,column=0)
Port_Select = Entry(root)
Port_Select.grid(row=2,column=1)

Creat_But = Button(root,text="Creat",bg="#03a2ff",command=Create_Game_Room).grid(row=2,column=2)

Button_Copy = Button(root,text="Copy Game Code").grid(row=3,column=0)
Exit_but = Button(root,text="Start Game",command=Exit_app_Comm).grid(row=3,column=1)
root.mainloop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((Join_Code,int(Code_M_Ls[0])))

s.listen(3)

Players=[]

first_Join_Massage = "Comfirmed"

food_x = 100
food_y = 10
player_1_score = 0
player_2_score = 0

Can_Deploy = True

while True:
    clies , addr = s.accept()
    Players.append(clies)

    if len(Players) == 2:
        for i in Players:
            i.send(first_Join_Massage.encode())

        break



def BroadCast(sk,msg):
    sk.send(msg)


def Getplayer1():
    while True:
        a = Players[0].recv(4096)
        f = pickle.loads(a)
        f[2] = food_x
        f[3] = food_y

        if abs(f[0] - food_x)<6 and abs(f[1] - food_y)<6:
            global player_1_score,Can_Deploy
            player_1_score +=1
            print(player_1_score)
            Can_Deploy = True

        f[4] = player_1_score
        f[5] = player_2_score
        BroadCast(Players[1],pickle.dumps(f))

def Getplayer2():
    while True:
        a = Players[1].recv(4096)
        f = pickle.loads(a)
        f[2] = food_x
        f[3] = food_y

        if abs(f[0] - food_x)<6 and abs(f[1] - food_y)<6:
            global player_2_score,Can_Deploy
            player_2_score +=1
            Can_Deploy = True
        f[4] = player_2_score
        f[5] = player_1_score
        BroadCast(Players[0],pickle.dumps(f))

def deplyIt():
    while True:
        global food_x,food_y,Can_Deploy
        if Can_Deploy == True:
            food_x = random.randint(0,900)
            food_y = random.randint(0,600)
            Can_Deploy = False

Thread(target=deplyIt).start()
Thread(target=Getplayer1).start()
Thread(target=Getplayer2).start()