#add_library('sound')
from functions import *
from TextBox import *
from Button import *
import elements
import player_selection
import player_dashboard
import random

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
curScreen = ''
rollSpeed = 1
roll = 1
buttons = {}
rollResult = None
turn = []
playSound = False
rollDone = False
dots = None

def setup():
    global buttons, diceSound, dots

    buttons['return'] = Button('Return', [100, 65], [25, 15], '#cccccc')
    buttons['dice'] = Button('', [600, center[1]], [500, 500], '#ffffff', borderRadius = 30)
    dots = functions.getDicePos(200, 200)

def draw():
    global screenSize, center, tick, para, curScreen, rollSpeed, buttons, roll, playSound, diceSound, rollDone, rollResult, turn, dots

    fade = tick * 2.5
    flameSpeed = [tick / 3.5, tick / 5]
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])

    sides = 6

    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])

    tick = tick + 1

    elements.updateElements()

    fill('#000000')

    if buttons['dice'].state == 'clicked' and not rollResult:
        if not playSound:
            playSound = True

        if tick % floor(rollSpeed) == 0:
            oldRoll = roll

            while roll == oldRoll:
                roll = random.randint(0, 5)

            rollSpeed = rollSpeed + 0.5

            if rollSpeed > 10:
                rollSpeed = 1
                print('done')
                playSound = False
                rollDone = True
                buttons['dice'].state = 'ready'
                rollResult = roll + 1

    fill('#ffffff')

    if rollResult:
        addText('You rolled ' + str(rollResult) + '!', [center[0] - 200, 150], '255', 64)

        if 'return' in buttons:
            buttons['return'].destroy()
            del buttons['return']

            buttons['continue'] = Button('Continue', [center[0] - 300, center[1] * 2 - 100], [25, 15], '#ccffcc')
            buttons['attack'] = Button('Attack', [center[0] - 100, center[1] * 2 - 100], [25, 15], '#ffcccc')

    if 'continue' in buttons and buttons['continue'].state == 'clicked':
        clearScreen()
        del buttons['continue']
        del buttons['attack']

        player_dashboard.turn = nextTurn(player_dashboard.turn)
        rollResult = None
        curScreen = 'player_dashboard'
        
    if 'attack' in buttons and buttons['attack'].state == 'clicked':
        clearScreen()
        del buttons['continue']
        del buttons['attack']
        
        curScreen = 'fighting_screen'

    if buttons['dice'].state != 'clicked' and not rollResult:
        addText('Click the dice to roll', [center[0] - 200, center[1] * 2 - 100], str(25 + toPulse(fade, 220)), 35)

    if 'return' in buttons and buttons['return'].state == 'clicked':
        rollSpeed = 1
        curScreen = 'player_dashboard'
        clearScreen()

    for coord in dots[roll % 6]:
        fill('#000000')
        circle(400 + coord[0] * 2, center[1] + coord[1] * 2 - 200, 100)
