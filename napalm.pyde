#add_library('sound')
import functions
import TextBox
import elements
import start_screen
import player_selection
import manual_screen
import player_dashboard
import player_inventory
import fighting_screen
import dice_system
# functions.py is where all the useful functions are located (It makes your life easier)
# start_screen.py is for the start screen

currentScreen = 'start'

def setup():
    size(1600, 900)
    functions.setup()
    #player_selection.setup()
    #s = SoundFile(this, 'soundtrack.mp3')
    #s.amp(0.50)
    #s.play()
    #s.loop()

def draw():
    global currentScreen

    fill(255)
    noStroke()
    rect(0, 0, 1600, 900)

    if currentScreen == 'start':
        start_screen.draw()
    elif currentScreen == 'player_selecting':
        player_selection.draw()
    elif currentScreen == 'player_dashboard':
        player_dashboard.draw()
    elif currentScreen == 'manual_screen':
        manual_screen.draw()
    elif currentScreen == 'fighting_screen':
        fighting_screen.draw()
    elif currentScreen == 'dice_system':
        dice_system.draw()

    if player_selection.curScreen == 'player_dashboard':
        currentScreen = 'player_dashboard'
        player_selection.curScreen = 'none'
        
        for i in range(0, len(elements.elements)):
            elements.elements[0].destroy()
        
        player_dashboard.setup()
    elif player_selection.curScreen == 'manual_screen':
        currentScreen = 'manual_screen'
    elif player_dashboard.curScreen == 'dice_system':
        player_dashboard.curScreen = 'none'
        currentScreen = 'dice_system'
        dice_system.setup()
    elif dice_system.curScreen == 'player_dashboard':
        dice_system.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()

def mousePressed():
    global currentScreen

    if currentScreen == 'start':
        player_selection.setup()
        currentScreen = 'player_selecting'
        player_selection.tick = start_screen.tick
    elif currentScreen == 'manual_screen':
        currentScreen = 'player_selecting'
        player_selection.curScreen = ''
    else:
        elements.mousePressed()

def keyPressed():
    elements.keyPressed()
