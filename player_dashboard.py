from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
buttons = {}
curScreen = ''
teams = [[], [], [], []]
turn = [0, 0]

def setup():
    buttons['startDice'] = Button('/img/halfCircle1.png',   [center[0] - 660, center[1]], [350, 500])
    buttons['openInventory'] = Button('/img/halfCircle3.png', [center[0] + 700, center[1]], [350, 500])
    buttons['startFight'] = Button('/img/halfCircle2.png', [center[0], center[1] + 330], [500, 350])
    buttons['restart'] = Button('Restart Game', [center[0] * 2 - 150, 25], [5, 5])

def draw():
    global screenSize, center, tick, curScreen, turn, teams
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    
    addText('Player Dashboard', [center[0] - 10, 80], '0', 64, 'scorch')
    addText('Player Dashboard', [center[0], 75], '255', 64, 'scorch')
    
    addText(teams[turn[0]][turn[1]].name + '\'s Turn', [center[0] - 5, 210], '0', 64, 'scorch')
    addText(teams[turn[0]][turn[1]].name + '\'s Turn', [center[0], 200], '255', 64, 'scorch')
    
    #addText('0  KEYS', [center[0] - 5, center[1] + 10], '0', 64, 'scorch')
    #addText('0  KEYS', [center[0], center[1]], '255', 64, 'scorch')
    
    healthWidth = int(600 * (teams[turn[0]][turn[1]].health / 5.0))
            
    if healthWidth <= 0:
        healthWidth = 1
    
    addFigure('rect', [center[0], 275], [600 + 15, 65], '0')
    addFigure('rect', [center[0], 275], [healthWidth, 50], '50,200,50')
    addImage('/img/noise.png', [center[0], 243], [615, 65])
    
    if 'startDice' in buttons and buttons['startDice'].state == 'clicked':
        clearScreen()
        curScreen = 'dice_system'
        
    if 'openInventory' in buttons and buttons['openInventory'].state == 'clicked':
        clearScreen()
        curScreen = 'player_inventory'
        
    if 'startFight' in buttons and buttons['startFight'].state == 'clicked':
        clearScreen()
        curScreen = 'fighting_screen'
        
    if buttons['restart'].state == 'clicked':
        clearScreen()
        curScreen = 'napalm'
    
    elements.updateElements()
    
    addImage('/img/dice.png', [center[0] - 660, center[1] - 125], [250, 250])
    addImage('/img/backpack.png', [center[0] + 660, center[1] - 125], [250, 250])
    addImage('/img/vslogo.png', [center[0] - 10, center[1] + 250], [250, 175])
    
