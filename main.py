
#Program to draw board in Python Turtle
import turtle
import sys
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
player1_Y = 0
player1_Xchange = 5
player1_Ychange = 0

#square shaped Box
boxSize=80
list=[]

def throwDice(mx,my):
    
    if(mx >= 10 and mx <= 10+30 and my >= 550 and my<= 550+30 ):
        #returns an integer randomly between 1 & 6 including these points
        global Dice_val 
        Dice_val= random.randint(1,6)
        print("val is: "+str(Dice_val))
        

def ShowDice():
    global Dice_val
    if(Dice_val ==1 ):
        screen.blit(dice_one, (10, 550))

    elif(Dice_val == 2):
        screen.blit(dice_two, (10, 550))   

    elif(Dice_val == 3):
        screen.blit(dice_three, (10, 550))

    elif(Dice_val == 4):
        screen.blit(dice_four, (10, 550))

    elif(Dice_val == 5):
        screen.blit(dice_five, (10, 550))
    
    elif(Dice_val == 6):
        screen.blit(dice_six, (10, 550))
     

def player1():
        screen.blit(player1_Img, (player1_X, player1_Y))

#def moveUser():






class LuduBoard:
    def __init__(self, number, upperLeftX,upperLeftY,upperRightX,upperRightY,lowerLeftX,lowerLeftY,lowerRightX,lowerRightY):
            self.number = number
            self.upperLeftX = upperLeftX
            self.upperLeftY=upperLeftY

            self.upperRightX = upperRightX
            self.upperRightY=upperRightY

            self.lowerLeftX=lowerLeftX
            self.lowerLeftY=lowerLeftY

            self.lowerRightX=lowerRightX
            self.lowerRightY=lowerRightY

    def myfunc(self):
        pygame.draw.polygon(screen, blue, 
                    [(self.upperLeftX, self.upperLeftY), (self.upperRightX, self.upperRightY), 
                    (self.lowerRightX, self.lowerRightY), (self.lowerLeftX, self.lowerLeftY)]) 
        print( self.number)


def buildLuduBoard():

        
        initX=0
        initY=0
        incrX=80
        incrY=60
        cnt=100

        for i in range(1,11,1):
            topLeftX=initX
            topLeftY=initY
            topRightX=initX+incrX
            topRightY=initY

            lowerLeftX=topLeftX
            lowerLeftY=initY+incrY
            lowerRightX=topRightX
            lowerRightY=initY+incrY

            obj=LuduBoard(cnt,topLeftX,topLeftY,topRightX,topRightY,lowerLeftX,lowerLeftY,lowerRightX,lowerRightY)
            cnt-=1      #decreament counter
            list.append(obj)
            
            for j in range(2,11,1):
                
               

                #if row number is ODD ,box will build up from left to right
                if(i%2 !=0):
                        topLeftX += incrX
                        topRightX+=incrX
                        lowerLeftX+=incrX
                        lowerRightX+=incrX

                        obj=LuduBoard(cnt,topLeftX,topLeftY,topRightX,topRightY,lowerLeftX,lowerLeftY,lowerRightX,lowerRightY)
                        cnt-=1      #decreament counter
                        list.append(obj)
                #if row number is EVEN , box will build up from right to left
                else:
                    topLeftX -= incrX
                    topRightX-=incrX
                    lowerLeftX-=incrX
                    lowerRightX-=incrX


                    obj=LuduBoard(cnt,topLeftX,topLeftY,topRightX,topRightY,lowerLeftX,lowerLeftY,lowerRightX,lowerRightY)
                    cnt-=1      #decreament counter
                    list.append(obj)

            initX=topLeftX
            initY=topLeftY+incrY





buildLuduBoard()

def showBoard():
    for x in list:
        x.myfunc()

#Game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my =pygame.mouse.get_pos()
            print(mx,my)
            throwDice(mx,my)
           
    showBoard()

    ShowDice()
    player1()
    
    #this update() is called at the end of the while loop
    pygame.display.update()