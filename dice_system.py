add_library('sound')
from functions import *
from TextBox import *
from Button import *
import elements
import random

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
curScreen = ''
rollSpeed = 1
roll = 1
buttons = {}
playSound = False
rollDone = False

def setup():
    global buttons, diceSound
    
    buttons['return'] = Button('Return', [100, 835], [25, 15], '#cccccc')
    buttons['dice'] = Button('', [650, center[1] - 50], [300, 300], '#ffffff')
    

def draw():
    global screenSize, center, tick, para, curScreen, rollSpeed, buttons, roll, playSound, diceSound, rollDone
    
    fade = tick * 2.5
    flameSpeed = [tick / 3.5, tick / 5]
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    x = 100
    y = 100
    
    sides = 6
    
    dots = [[0, 0] for i in range(6)]

    dots[0] = [
        [x / 2, y / 2]
    ]
    dots[1] = [
        [x / 10, y / 10],
        [x - x / 10, y - y / 10]
    ]
    dots[2] = [
        dots[1][0],
        dots[0][0],
        dots[1][1]
    ]
    dots[3] = [
        dots[1][0],
        dots[1][1],
        [dots[1][0][0], dots[1][1][1]],
        [dots[1][1][0], dots[1][0][1]]
    ]
    dots[4] = [
        dots[1][0],
        dots[1][1],
        dots[0][0],
        [dots[1][0][0], dots[1][1][1]],
        [dots[1][1][0], dots[1][0][1]]
    ]
    dots[5] = [
        dots[1][0],
        dots[1][1],
        [dots[1][0][0], dots[0][0][1]],
        [dots[1][1][0], dots[0][0][1]],
        [dots[1][0][0], dots[1][1][1]],
        [dots[1][1][0], dots[1][0][1]]
    ]
    
    addText('Click the dice to roll', [650, center[1] + 200], str(25 + toPulse(fade, 220)), 35)
    
    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])
    
    tick = tick + 1
    
    elements.updateElements()
        
    fill('#000000')
    
    if buttons['dice'].state == 'clicked':
        if not playSound:
            playSound = True
            
        if tick % floor(rollSpeed) == 0:
            oldRoll = roll
            
            while roll == oldRoll:
                roll = random.randint(0, 5)
                
            rollSpeed = rollSpeed + 0.5
            
            if rollSpeed > 10:
                rollSpeed = 1
                print('done')
                playSound = False
                rollDone = True
                buttons['dice'].state = 'ready'
                
    if buttons['return'].state == 'clicked':
        curScreen = 'player_dashboard'
        clearScreen()
                
    for coord in dots[roll % 6]:
        circle(550 + coord[0] * 2, center[1] + coord[1] * 2 - 150, 50)
