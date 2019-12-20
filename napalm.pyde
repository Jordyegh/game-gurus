add_library('sound')
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
test = True
diceSound = None
soundtrack = None
creepySoundtrack = None
gunSound = None
rollOnce = True
playOnce = True #For creepy soundtrack
teams = [[], [], [], []]

def setup():
    global diceSound, soundtrack, creepySoundtrack, gunSound
    size(1600, 900)
    functions.setup()
    diceSound = SoundFile(this, 'diceRoll.mp3')
    diceSound.amp(1.0)
    #player_selection.setup()
    soundtrack = SoundFile(this, 'soundtrackTrimmed.mp3')
    soundtrack.amp(0.25)
    soundtrack.play()
    gunSound = SoundFile(this, 'gunshot.mp3')
    gunSound.amp(1.0)
    creepySoundtrack = SoundFile(this, 'creepySoundtrackTrimmed.mp3')
    creepySoundtrack.amp(0.8)


def draw():
    global currentScreen, test, diceSound, rollOnce, soundtrack, creepySoundtrack, playOnce, gunSound

    fill(255)
    noStroke()
    rect(0, 0, 1600, 900)

    if currentScreen == 'start':
        start_screen.draw()
    elif currentScreen == 'player_selecting':
        player_selection.draw()
    elif currentScreen == 'player_dashboard':
        player_dashboard.draw()
    elif currentScreen == 'player_inventory':
        player_inventory.draw()
    elif currentScreen == 'manual_screen':
        manual_screen.draw()
    elif currentScreen == 'fighting_screen':
        fighting_screen.draw()
    elif currentScreen == 'dice_system':
        dice_system.draw()

    if player_selection.curScreen == 'player_dashboard':
        currentScreen = 'player_dashboard'
        player_selection.curScreen = 'none'
        teams = player_selection.teams
        player_dashboard.teams = teams
        functions.teams = teams

        print(teams)

        for i in range(0, len(elements.elements)):
            elements.elements[0].destroy()

        player_dashboard.setup()
    elif player_selection.curScreen == 'manual_screen':
        currentScreen = 'manual_screen'
    elif player_dashboard.curScreen == 'dice_system':
        player_dashboard.curScreen = 'none'
        currentScreen = 'dice_system'
        dice_system.setup()
    elif player_dashboard.curScreen == 'player_inventory':
        player_dashboard.curScreen = 'none'
        currentScreen = 'player_inventory'
        player_inventory.setup()
    elif dice_system.curScreen == 'player_dashboard':
        dice_system.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()
    elif player_inventory.curScreen == 'dice_system':
        player_inventory.curScreen = 'none'
        currentScreen = 'dice_system'
        dice_system.setup()
    elif player_inventory.curScreen == 'player_dashboard':
        player_inventory.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()

    if dice_system.rollDone == True:
        rollOnce = True
    if dice_system.playSound == True and rollOnce:
        diceSound.stop()
        rollOnce = False
        diceSound.play()
        dice_system.playsound = False
    if player_selection.stopSoundtrack == True and playOnce:
        print('test')
        soundtrack.stop()
        playOnce = False
        gunSound.play()
        creepySoundtrack.play()
        creepySoundtrack.loop()





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
