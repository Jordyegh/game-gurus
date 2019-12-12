from functions import *
from TextBox import *
from Button import *
from Player import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
curScreen = ''
buttons = {}

def setup():
    global screenSize, center, tick, buttons
    buttons['stimpackDmg'] = Button('/img/stimpackDmg.png', [200, 400], [250, 250])
    buttons['stimpackRange'] = Button('/img/stimpackRange.png', [600, 400], [250, 250])
    buttons['energyDrink'] = Button('/img/energyDrink.png', [1000, 400], [250, 250])
    buttons['bandage'] = Button('/img/bandage.png', [1400, 400], [250, 250])
def draw():
    global screenSize, center, tick, buttons
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    addText('Player Inventory', [375, 75], '255', 64, 'scorch')
    
    if buttons['stimpackDmg'].state == 'clicked':
        buttons['stimpackDmg'].willDraw = False
    if buttons['stimpackRange'].state == 'clicked':
        buttons['stimpackRange'].willDraw = False
    if buttons['energyDrink'].state == 'clicked':
        currentScreen = 'dice_system'
    if buttons['stimpackDmg'].state == 'clicked':
        buttons['stimpackDmg'].willDraw = False
    
    elements.updateElements()
