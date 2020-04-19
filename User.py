from init import *
from Snake import *
from Ladder import *


def checkValidity():
       
        if (Main.Player1_validity==1):
            movePlayer1()
        else:
            if(Main.Dice_val==1):
                Main.player1Index=1
                Main.Player1_validity=1
                
            else:
                Main.Player1_validity=0



def movePlayer1():
   
    userDestinationIndex=Main.player1Index
    userDestinationIndex += Main.Dice_val
    
    for x in Main.list:
       if( x.getNumber()== userDestinationIndex):
            userDestinationX,userDestinationY =x.getSquareBoxCenterPosition()
            
           
            print("source: "+str(Main.player1Index) + " dest: "+str(userDestinationIndex))
            for i in range(Main.player1Index,userDestinationIndex+1,1):
                    
                    coord= Main.indexToCoordinate[i]
                    Main.player1_X=coord[0]
                    Main.player1_Y=coord[1] 

                    Main.player1Index=i 


            checkSnake(Main.player1Index)
            checkLadder(Main.player1Index)


def showPlayer1():
   
    #print("validity: "+str(Main.Player1_validity))
    if(Main.Player1_validity==1):
        Main.screen.blit(Main.player1_Img, (Main.player1_X, Main.player1_Y))