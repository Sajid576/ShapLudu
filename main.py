from init import *
from LuduBoard import *
from User import *


def throwDice(mx,my):
    
    if(mx >= 10 and mx <= 10+30 and my >= 550 and my<= 550+30 ):
        #returns an integer randomly between 1 & 6 including these points
        
        Main.Dice_val= random.randint(1,6)
        print("val is: "+str(Main.Dice_val))
        checkValidity()
        

def ShowDice():
    
    if(Main.Dice_val ==1 ):
        Main.screen.blit(Main.dice_one, (10, 550))

    elif(Main.Dice_val == 2):
        Main.screen.blit(Main.dice_two, (10, 550))   

    elif(Main.Dice_val == 3):
        Main.screen.blit(Main.dice_three, (10, 550))

    elif(Main.Dice_val == 4):
        Main.screen.blit(Main.dice_four, (10, 550))

    elif(Main.Dice_val == 5):
        Main.screen.blit(Main.dice_five, (10, 550))
    
    elif(Main.Dice_val == 6):
        Main.screen.blit(Main.dice_six, (10, 550))
     




class Snakes:
    def __init__(self,mouthIndex,AssIndex):
        self.mouthIndex=mouthIndex
        self.AssIndex=AssIndex
        
    
class Laddder:
    def __init__(self,belowIndex,topIndex):
        self.belowIndex=belowIndex
        self.topIndex=topIndex
        



buildLuduBoard()

#Game loop
running=True
while running:
    Main.screen.fill(Main.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my =pygame.mouse.get_pos()
            print(mx,my)
            throwDice(mx,my)
           
    showBoard()

    ShowDice()
    
    showPlayer1()
    
    #this update() is called at the end of the while loop
    pygame.display.update()