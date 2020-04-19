#Program to draw board in Python Turtle
import turtle
import sys
import math
import random
import time

import pygame
from pygame import mixer

class Main:
        # Intialize the pygame
        pygame.init()


        # create the screen
        screenWidth=800
        screenHeight=600

        screen = pygame.display.set_mode((screenWidth, screenHeight))

        # define the RGB value 
        # for white, green, 
        # blue, black, red 
        # colour respectively. 
        white = (255, 255, 255) 
        green = (0, 255, 0) 
        blue = (0, 0, 128) 
        black = (0, 0, 0) 
        red = (255, 0, 0) 


        # Sound
        mixer.music.load("Astronomia.mp3")
        mixer.music.play(-1)


        pygame.display.set_caption("Shap Ludu")
        icon = pygame.image.load('images/bg.jpg')
        pygame.display.set_icon(icon)

        #Dice
            
        Dice_val=2
        dice_one = pygame.image.load('images/dice_One.jpg')
        dice_one=pygame.transform.scale(dice_one, (30,30))

        dice_two = pygame.image.load('images/dice_two.jpg')
        dice_two=pygame.transform.scale(dice_two, (30,30))

        dice_three = pygame.image.load('images/dice_three.jpg')
        dice_three=pygame.transform.scale(dice_three, (30,30))

        dice_four = pygame.image.load('images/dice_four.jpg')
        dice_four=pygame.transform.scale(dice_four, (30,30))

        dice_five = pygame.image.load('images/dice_five.jpg')
        dice_five=pygame.transform.scale(dice_five, (30,30))

        dice_six = pygame.image.load('images/dice_six.jpg')
        dice_six=pygame.transform.scale(dice_six, (30,30))


        # Player1
        player1_Img = pygame.image.load('images/player.jpg')
        player1_Img = pygame.transform.scale(player1_Img, (40,40))
        player1_X = 0
        player1_Y = screenHeight-40
        player1Index=0
        Player1_validity=0
       
       

        #square shaped Box
        myfont = pygame.font.SysFont('Comic Sans MS', 15)
        list=[]
        indexToRowDict={}
        indexToCoordinate={}

        #snakes
        snakesList=[]

        #Ladder
        ladderList=[]