from functions import *
from TextBox import *
from Button import *
import elements
import random

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations


def addDescription(title = 'Title', desc = 'Description', pos = [100, 100], img = '/img/guntegel.png'):
    addText(title, pos, '255', 24)
    addText(desc, [pos[0], pos[1] + 20], '255', 18)
    addImage(img, [pos[0] + 300, pos[1]], [150,150])
    print('Teest')

def draw():
    global screenSize, center, tick, para
    
    fade = tick * 2.5
    flameSpeed = [tick / 3.5, tick / 5]
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    
    for y in range(0, 3):
        for x in range(0, 2):
            id = x + y * 2
            
           
    
    addText('Dobbelsysteem', [375, 75], '255', 64, 'scorch')
    
    
def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled

def main():
    sides = 6
    
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? ENTER = roll. Q=Quit. ")
        if roll_again.lower() !="q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling = False
    print("Thanks for playing")
    

    
    
    
    
    
    
    
    
    
    addText('Click to go next', [650, center[1] + 350], str(25 + toPulse(fade, 220)), 35)
    

    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])
    
    tick = tick + 1
