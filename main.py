import math
import random
import time
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
#scaling the background image size into screen size
background = pygame.transform.scale(background, (screenWidth,screenHeight))

# Sound
mixer.music.load("Astronomia.mp3")
mixer.music.play(-1)


pygame.display.set_caption("Shap Ludu")
icon = pygame.image.load('bg.jpg')
pygame.display.set_icon(icon)

# Player1
player1_Img = pygame.image.load('player.jpg')
player1_Img = pygame.transform.scale(player1_Img, (50,50))
player1_X = 0
player1_Y = 0
player1_Xchange = 5
player1_Ychange = 0


def player1():
        screen.blit(player1_Img, (player1_X, player1_Y))

def moveForward():
      global player1_X,player1_Xchange
      
      player1_X=player1_X+player1_Xchange  


#Game loop
running=True
while running:

     # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                     moveForward()
 

    player1()
    #this update() is called at the end of the while loop
    pygame.display.update()