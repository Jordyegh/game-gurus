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

def setup():
    global screenSize, center, tick, buttons
    buttons['return'] = Button('Return', [100, 835], [25, 15], '#cccccc')
    buttons['stimpackDmg'] = Button('/img/stimpackDmg.png', [200, 400], [250, 250])
    buttons['stimpackRange'] = Button('/img/stimpackRange.png', [600, 400], [250, 250])
    buttons['energyDrink'] = Button('/img/energyDrink.png', [1000, 400], [250, 250])
    buttons['bandageAmount2'] = Button('+2 HP', [1400, 350], [25, 10], '235,255,235', 'none', '0', '200,255,200')
    buttons['bandageAmount4'] = Button('+4 HP', [1400, 450], [25, 10], '235,255,235', 'none', '0', '200,255,200')
    buttons['bandage'] = Button('/img/bandage.png', [1400, 400], [250, 250])
    
def draw():
    global screenSize, center, tick, buttons, curScreen
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    addText('2 extra DMG', [205, 580], '0', 40, 'scorch')
    addText('2 extra RANGE', [605, 580], '0', 40, 'scorch')
    addText('Roll the dice twice', [1005, 574], '0', 30, 'scorch')
    addText('Heal yourself', [1405, 580], '0', 40, 'scorch')
    addText('Player Inventory', [375, 75], '255', 64, 'scorch')
    addText('2 extra DMG', [200, 575], '255', 40, 'scorch')
    addText('2 extra RANGE', [600, 575], '255', 40, 'scorch')
    addText('Roll the dice twice', [1000, 569], '255', 30, 'scorch')
    addText('Heal yourself', [1400, 575], '255', 40, 'scorch')
    #print(buttons['stimpackDmg'].state)
    if buttons['stimpackDmg'].state == 'clicked':
        #+2 damage will be added to your weapon for 1 attack.
        curScreen = 'player_dashboard'
        clearScreen()
    if buttons['stimpackRange'].state == 'clicked':
        curScreen = 'player_dashboard'
        clearScreen()
    if buttons['energyDrink'].state == 'clicked':
        curScreen = 'dice_system'
        clearScreen()
    if buttons['bandage'].state == 'clicked':
        buttons['bandage'].willDraw = False
    if buttons['bandageAmount2'].state == 'clicked':
        #Heal 2 and next player.
        currentScreen = 'player_dashboard' #NEXT PLAYER
    if buttons['bandageAmount2'].state == 'clicked':
        #Heal 4 and next player.
        currentScreen = 'player_dashboard' #NEXT PLAYER
    if buttons['return'].state == 'clicked':
        curScreen = 'player_dashboard'
        clearScreen()
        
    
    elements.updateElements()
