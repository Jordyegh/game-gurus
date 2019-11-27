from functions import *
from TextBox import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations

def setup():
    TextBox('Player 1', [center[0], center[1]], [250, 50], '225', '0')
    TextBox('Player 2', [center[0], center[1] + 100], [250, 50], '225', '0')
    TextBox('Player 3', [center[0], center[1] + 200], [250, 50], '225', '0')

def draw():
    global screenSize, center, tick
    
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    addText('Player Selection', [center[0], 75], '0', 64)

    tick = tick + 1
    
    elements.updateElements()
