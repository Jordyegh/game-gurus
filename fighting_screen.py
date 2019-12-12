from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
teams = [[], [], [], []]
buttons = {}

def draw():
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    
    addText('CHOOSE WHO TO FIGHT', [center[0] - 10, 100 + 5], '0', 64, font = 'scorch')
    addText('CHOOSE WHO TO FIGHT', [center[0], 100], '255', 64, font = 'scorch')
    
    elements.updateElements()
