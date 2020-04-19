from init import *

class LuduBoard:
    def __init__(self, number, upperLeftX,upperLeftY,rowNumber):
            
            Main.indexToRowDict[number]=rowNumber
            Main.indexToCoordinate[number]= (upperLeftX,upperLeftY)

            self.number = number
            self.upperLeftX = upperLeftX
            self.upperLeftY=upperLeftY

           
    def drawRectangle(self):
       # draw a rectangle
        pygame.draw.rect(Main.screen, Main.blue, pygame.Rect(self.upperLeftX, self.upperLeftY, 80, 60), 5)
        #print( self.number)

    def drawNumber(self):
        textNumber = Main.myfont.render(str(self.number), False,Main.white)
        Main.screen.blit(textNumber, ( (self.upperLeftX+80/2) ,self.upperLeftY+ 10))

    
    def getNumber(self):
        return self.number

    def getSquareBoxCenterPosition(self):
        return self.upperLeftX+(80/2),self.upperLeftY+(60/2)   


#this method is used for showing Ludu board on screen
def showBoard():
    for x in Main.list:
        x.drawRectangle()
        x.drawNumber()

#this method is used for building the logic of Ludu Board only once
def buildLuduBoard():   
        initX=0
        initY=0
        incrX=80
        incrY=60
        cnt=100

        for i in range(1,11,1):
            topLeftX=initX
            topLeftY=initY
            

            obj=LuduBoard(cnt,topLeftX,topLeftY,i)
            cnt-=1      #decreament counter
            Main.list.append(obj)
            
            for j in range(2,11,1):
                #if row number is ODD ,box will build up from left to right
                if(i%2 !=0):
                        topLeftX += incrX
                        
                        obj=LuduBoard(cnt,topLeftX,topLeftY,i)
                        cnt-=1      #decreament counter
                        Main.list.append(obj)
                #if row number is EVEN , box will build up from right to left
                else:
                    topLeftX -= incrX
                    
                    obj=LuduBoard(cnt,topLeftX,topLeftY,i)
                    cnt-=1      #decreament counter
                    Main.list.append(obj)

            initX=topLeftX
            initY=topLeftY+incrY
