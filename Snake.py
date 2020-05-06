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

    for x in Main.snakesIndexPairList:
        snakeObj=Snakes(x[0],x[1])
       
        Main.snakesList.append(snakeObj)
        

def showSnakes():

     for x in Main.snakesList:
            coord=Main.indexToCoordinate[x.getMouthIndex()]
            lat=coord[0]
            lon=coord[1]
            Main.screen.blit(Main.snake_img, (lat+(80/2) ,lon+(60/2)))

       