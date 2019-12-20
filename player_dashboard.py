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
    buttons['startDice'] = Button('/img/halfCircle1.png',   [center[0] - 660, center[1]], [350, 500])
    buttons['openInventory'] = Button('/img/halfCircle3.png', [center[0] + 700, center[1]], [350, 500])
    buttons['startFight'] = Button('/img/halfCircle2.png', [center[0], center[1] + 330], [500, 350])
    
    #buttons['openInventory'] = Button('/img/backpack.png', [center[0] - 250, center[1]], [250, 250])
    #buttons['startFight'] = Button('/img/vslogo.png', [center[0] + 250, center[1]], [250, 200])

def draw():
    global screenSize, center, tick, curScreen
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    #addImage('/img/Dashboard_backpack.png', [1505, 200], [275, 470])
    #addImage('/img/Dashboard_dice.png', [95, 200], [275, 470])
    #addImage('/img/Dashboard_fight.png', [800, 655], [470, 275])
    
    addText('Player Dashboard', [375, 75], '255', 64, 'scorch')
    
    if 'startDice' in buttons and buttons['startDice'].state == 'clicked':
        clearScreen()
        curScreen = 'dice_system'
        
    if 'openInventory' in buttons and buttons['openInventory'].state == 'clicked':
        clearScreen()
        curScreen = 'player_inventory'
        print('df')
        
    if 'startFight' in buttons and buttons['startFight'].state == 'clicked':
        clearScreen()
    
    elements.updateElements()
    
    addImage('/img/dice.png', [center[0] - 660, center[1] - 125], [250, 250])
    addImage('/img/backpack.png', [center[0] + 660, center[1] - 125], [250, 250])
    
