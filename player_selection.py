from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
buttons = {}
curScreen = ''

def setup():
    buttons['addPlayer'] = Button('+', [100, 100], [150, 5], '200,255,200', 'none', '0', '150,255,150')
    buttons['startGame'] = Button('START GAME', [screenSize[0] - 350, 200], [50, 25], '200', 'none', '0')
    
    TextBox('Player 1', [150, center[1]], [150, 50], '225', '0', 10)
    TextBox('Player 2', [250, center[1]], [150, 50], '225', '0')

def draw():
    global screenSize, center, tick, curScreen

    flameSpeed = [tick / 3.5, tick / 5]

    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    addText('Player Selection', [375, 75], '255', 64, 'scorch')

    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])

    if buttons['startGame'].state == 'clicked':
        curScreen = 'player_dashboard'

    tick = tick + 1

    elements.updateElements()
