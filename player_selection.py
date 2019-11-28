from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations

def setup():
    TextBox('Player 1', [center[0], center[1]], [250, 50], '225', '0')
    TextBox('Player 2', [center[0], center[1] + 100], [250, 50], '225', '0')
    TextBox('Player 3', [center[0], center[1] + 200], [250, 50], '225', '0')
    
    Button('START GAME', [screenSize[0] - 350, 250], [0, 0], '200', '200', '0')

def draw():
    global screenSize, center, tick
    
    flameSpeed = [tick / 3.5, tick / 5]
    
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    addText('Player Selection', [375, 75], '255', 64, 'scorch')
    
    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])

    tick = tick + 1
    
    elements.updateElements()
