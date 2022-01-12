import pygame
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost",1586))

s.recv(1024).decode()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
player_1_x = 45
player_1_y = 55
velocity_x = 0
velocity_y = 0
player_1_Cords = [45,55]
player_2_x = 60
player_2_y = 10
snake_size = 10
fps = 10
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
    pygame.display.update()
    player_1_Cords[0] = player_1_x
    player_1_Cords[1] = player_1_y

    s.send(pickle.dumps(player_1_Cords))
    recodede = pickle.loads(s.recv(1024))
    player_2_x = recodede[0]
    player_2_y = recodede[1]
    clock.tick(fps)

pygame.quit()
quit()

