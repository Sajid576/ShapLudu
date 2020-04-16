import math
import random

import pygame
from pygame import mixer


# Intialize the pygame
pygame.init()


# create the screen
screenWidth=800
screenHeight=600

screen = pygame.display.set_mode((screenWidth, screenHeight))

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

      # RGB = Red, Green, Blue
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()