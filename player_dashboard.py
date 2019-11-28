from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
buttons = {}
curScreen = ''


def draw():
    global screenSize, center, tick
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    addImage('/img/halfcircle3.png', [1505, 200], [275, 470])
    addImage('/img/halfcircle1.png', [95, 200], [275, 470])
    addImage('/img/halfcircle2.png', [800, 655], [470, 275])
    addImage('/img/backpack.png', [1505, 310], [220, 220])
    addImage('/img/dice.png', [85, 310], [220, 220])
    addImage('/img/versus.png', [800, 720], [250, 190])
    addText('Use item', [1505, 200], '255', 40) #concept description and font
    addText('Roll dice', [95, 200], '255', 40) #concept description and font
    addText('Fight enemy', [800, 655], '255', 40) #concept description and font

    addText('Player Dashboard', [375, 75], '255', 64, 'scorch')
    addText('\'s turn', [850, 200], '255', 64, 'scorch') #Need to add Currentplayer(?) + variable to this string. or sumtin'
    addText('Keys', [850, 200 + 50], '255', 40, 'scorch') #Need to add a + Currentkeys(?) variable to this string. or sumtin'
