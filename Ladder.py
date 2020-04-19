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

        LaddderObj=Laddder(2,14)
        LaddderObj1=Laddder(3,50)
        LaddderObj2=Laddder(24,60)

        Main.ladderList.append(LaddderObj)
        Main.ladderList.append(LaddderObj1)
        Main.ladderList.append(LaddderObj2)
