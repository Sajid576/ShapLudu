from init import *

class Snakes:
    
    def __init__(self,mouthIndex,AssIndex):
        self.mouthIndex=mouthIndex
        self.AssIndex=AssIndex

    def getMouthIndex(self):
        return self.mouthIndex
        
    def getAssIndex(self):
        return self.AssIndex
    


def checkSnake(index):
    for x in Main.snakesList:
        if(x.getMouthIndex()==index):
            print("Snake khaise mama")
            Main.player1Index=x.getAssIndex()
            coord =Main.indexToCoordinate[Main.player1Index]
            Main.player1_X=coord[0]
            Main.player1_Y=coord[1]
            


def buildSnakes():

        snakeObj=Snakes(40,2)
        snakeObj1=Snakes(80,4)
        snakeObj2=Snakes(30,4)

        Main.snakesList.append(snakeObj)
        Main.snakesList.append(snakeObj1)
        Main.snakesList.append(snakeObj2)