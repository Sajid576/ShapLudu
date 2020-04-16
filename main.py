import math
import random

import pygame
from pygame import mixer


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('bg.jpg')

# Sound
mixer.music.load("Astronomia.mp3")
mixer.music.play(-1)


pygame.display.set_caption("Shap Ludu")
icon = pygame.image.load('bg.jpg')
pygame.display.set_icon(icon)

#Game loop
running=True
while running:

     
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False