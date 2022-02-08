
from tkinter import font
import pygame
import socket
import pickle
from tkinter import *

server_ip = []

root = Tk()

def GetEntryText():

    got_text_ip = Enght.get()
    server_ip.append(got_text_ip)
    server_ip.append(int(Port_sd.get()))
    
    root.destroy()

Enght = Entry(root,width=100)
Enght.grid(row=1,column=1)
enght_lab = Label(root,text="Game Code:- ").grid(row=1,column=0)

port_lbal = Label(root,text="Port :-").grid(row=2,column=0)
Port_sd = Entry(root)
Port_sd.grid(row=2,column=1)
Butoo = Button(root,text="Go",command=GetEntryText).grid(row=3,column=1)

root.mainloop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_ip)
s.connect((server_ip[0],server_ip[1]))

s.recv(1024).decode()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (10, 59, 255)
green = (10, 59, 255)
lt_red = (247, 124, 142)
# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Multi Rumble")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
player_1_x = 45
player_1_y = 55
velocity_x = 0
velocity_y = 0

player_1_configures = [45,55,500,100,0,0]

player_2_x = 60
player_2_y = 10

food_x = 100
food_y = 80

score = 0

snake_size = 10
fps = 12
clock = pygame.time.Clock()

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - 10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - 10
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

    player_1_y = player_1_y + velocity_y
    player_1_x = player_1_x + velocity_x

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [player_2_x, player_2_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [player_1_x, player_1_y, snake_size, snake_size])

    pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])
    
  
    player_1_configures[0] = player_1_x
    player_1_configures[1] = player_1_y


    s.send(pickle.dumps(player_1_configures))
    recodede = pickle.loads(s.recv(4024))

    player_2_x = recodede[0]
    player_2_y = recodede[1]
    
    food_x = recodede[2]
    food_y = recodede[3]

    Main_Score = f"You:{recodede[5]}-Enemy:{recodede[4]}"
  
    text_x = screen_width/2

    text_y = 20

    font = pygame.font.Font('freesansbold.ttf', 25)

    
    text = font.render(Main_Score, True, green, lt_red)

    textRect = text.get_rect()

    textRect.center = (text_x,text_y)

    gameWindow.blit(text, textRect)

    pygame.display.update()


    clock.tick(fps)

pygame.quit()
quit()