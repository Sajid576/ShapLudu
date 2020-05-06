from init import *

class Laddder:
    def __init__(self,belowIndex,topIndex):
        self.belowIndex=belowIndex
        self.topIndex=topIndex
    def getBelowIndex(self):
        return self.belowIndex
    def getTopIndex(self):
        return self.topIndex






def checkLadder(index):
    for x in Main.ladderList:
        if(x.getBelowIndex()==index):
            print("Ladder paisi mama :p ")
            Main.player1Index=x.getTopIndex()
            coord =Main.indexToCoordinate[Main.player1Index]
            Main.player1_X=coord[0]
            Main.player1_Y=coord[1]
            


def buildLadders():

    for x in Main.ladderIndexPairList:
        LaddderObj=Laddder(x[0],x[1])
        Main.ladderList.append(LaddderObj)

        


def showLadders():
    
    for x in Main.ladderList:
            coord=Main.indexToCoordinate[x.getTopIndex()]
            lat=coord[0]
            lon=coord[1]
            Main.screen.blit(Main.ladder_img, (lat+20 ,lon+50))
