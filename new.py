import pygame
from pygame.locals import *
import sys
import random

pygame.init()

DISPLY_SURFACE = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)

BACKGROUND_IMG = pygame.image.load('stars.jpg').convert()
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (800,600))
BACKGROUND_X=0
BACKGROUND_Y=0
PLAYER_IMG = pygame.image.load('space-invaders.png')

PLAYER_X = 370
PLAYER_Y = 480
PLAYER_X_CHANGE = 0

def background():
    DISPLY_SURFACE.blit(BACKGROUND_IMG, (BACKGROUND_X, BACKGROUND_Y))
    DISPLY_SURFACE.blit(BACKGROUND_IMG, (BACKGROUND_X, BACKGROUND_Y -600))

while True:
    DISPLY_SURFACE.fill(WHITE)

    BACKGROUND_Y += 2

    background()

    if BACKGROUND_Y >= 600:
        BACKGROUND_Y = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()        
