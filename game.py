import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600))

# player
player_img = pygame.image.load("space-invaders.png").convert()
player_x =370
player_y = 480

def player():
    screen.blit(player_img, (player_x, player_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))

    player()

    pygame.display.update()