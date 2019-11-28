from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations

def draw():
    global screenSize, center, tick
    addImage('/img/Dashboard_background2.jpg', [center[0], 0], [1600, 900])
    addImage('/img/Dashboard_backpack.png', [1505, 200], [275, 470])
    addImage('/img/Dashboard_dice.png', [95, 200], [275, 470])
    addImage('/img/Dashboard_fight.png', [800, 655], [470, 275])
    addText('Player Dashboard', [375, 75], '255', 64, 'scorch')
    
