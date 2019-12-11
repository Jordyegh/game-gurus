from functions import *
from TextBox import *
from Button import *
from Player import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
nameBoxes = []


def setup():
    Button('Use item', [400, 800], [50, 25], '200', 'none', '0')
    Button('Use item', [800 - 200, 800], [50, 25], '200', 'none', '0')
    Button('Use item', [800 + 200, 800], [50, 25], '200', 'none', '0')
    Button('Use item', [1200, 800], [50, 25], '200', 'none', '0')

def draw():
    global screenSize, center, tick, item


    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    addText('Player Inventory', [375, 75], '255', 64, 'scorch')
    
    elements.updateElements()
    

    
