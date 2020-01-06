from functions import *
from TextBox import *
from Button import *
from Player import *
import elements
import manual_screen

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
curScreen = ''
buttons = {}
turn = [0, 0]
teams = [[], [], [], []]

def setup():
    global screenSize, center, tick, buttons
    buttons['return'] = Button('Return', [100, 50], [25, 15], '#cccccc')
    buttons['stimpackDmg'] = Button('/img/stimpackDmg.png', [center[0] - 400, 400], [250, 250])
    buttons['energyDrink'] = Button('/img/energyDrink.png', [center[0], 400], [250, 250])
    buttons['bandage'] = Button('/img/bandage.png', [center[0] + 400, 400], [250, 250])
    
def draw():
    global screenSize, center, tick, buttons, curScreen, turn
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    addText('+2 Damage', [center[0] - 405, 580], '0', 40, 'scorch')
    addText('Roll Twice', [center[0] + 5, 574], '0', 30, 'scorch')
    addText('Heal Yourself', [center[0] + 405, 580], '0', 40, 'scorch')
    
    addText('Player Inventory', [center[0], 85], '0', 64, 'scorch')
    addText('Player Inventory', [center[0] - 10, 75], '255', 64, 'scorch')
    
    addText('2 extra DMG', [center[0] - 400, 575], '255', 40, 'scorch')
    addText('Roll the dice twice', [center[0], 569], '255', 30, 'scorch')
    addText('Heal yourself', [center[0] + 400, 575], '255', 40, 'scorch')
    #print(buttons['stimpackDmg'].state)
    if buttons['stimpackDmg'].state == 'clicked':
        #+2 damage will be added to your weapon for 1 attack.
        curScreen = 'player_dashboard'
        clearScreen()
    if buttons['energyDrink'].state == 'clicked':
        curScreen = 'dice_system'
        clearScreen()
    if buttons['bandage'].state == 'clicked':
        buttons['bandage'].willDraw = False
        buttons['bandage'].state = 'ready'
        buttons['bandage'].canClick = False
        buttons['bandageAmount2'] = Button('+2 HP', [center[0] + 400, 350], [25, 10], '235,255,235', 'none', '0', '200,255,200')
        buttons['bandageAmount4'] = Button('+4 HP', [center[0] + 400, 450], [25, 10], '235,255,235', 'none', '0', '200,255,200')
    if 'bandageAmount2' in buttons and buttons['bandageAmount2'].state == 'clicked':
        #Heal 2 and next player.
        teams[turn[0]][turn[1]].health = teams[turn[0]][turn[1]].health + 2 if (teams[turn[0]][turn[1]].health + 2) <= 5 else 5
        nextTurn(turn)
        curScreen = 'player_dashboard' #NEXT PLAYER
        buttons['bandageAmount2'].state = 'ready'
        clearScreen()
    if 'bandageAmount4' in buttons and buttons['bandageAmount4'].state == 'clicked':
        #Heal 4 and next player.
        teams[turn[0]][turn[1]].health = teams[turn[0]][turn[1]].health + 4 if (teams[turn[0]][turn[1]].health + 4) <= 5 else 5
        nextTurn(turn)
        curScreen = 'player_dashboard' #NEXT PLAYER
        buttons['bandageAmount4'].state = 'ready'
        clearScreen()
    if buttons['return'].state == 'clicked':
        curScreen = 'player_dashboard'
        clearScreen()
        
    
    elements.updateElements()
