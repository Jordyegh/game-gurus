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
import Button as btn
# functions.py is where all the useful functions are located (It makes your life easier)
# start_screen.py is for the start screen

currentScreen = 'start'
teams = [[], [], [], []]
test = True
diceSound = None
soundtrack = None
creepySoundtrack = None
gunSound = None
rollOnce = True
playOnce = True #For creepy soundtrack

listButtonsManual = [] # List of buttons
manualPage = 0 # Page counter

def setup():
    global diceSound, soundtrack, creepySoundtrack, gunSound, listButtons
    size(1600, 900)
    functions.setup()
    #diceSound = SoundFile(this, 'diceRoll.mp3')
    #diceSound.amp(1.0)
    #player_selection.setup()
    #soundtrack = SoundFile(this, 'soundtrackTrimmed.mp3')
    #soundtrack.amp(0.25)
    #soundtrack.play()
    #gunSound = SoundFile(this, 'gunshot.mp3')
    #gunSound.amp(1.0)
    #creepySoundtrack = SoundFile(this, 'creepySoundtrackTrimmed.mp3')
    #creepySoundtrack.amp(0.8)
    
    # Create and add buttons to the list
    listButtonsManual.append(btn.ButtonTemplate(width-90, height-35, 150, 40, "NEXT", 14, color(255,255,255), CENTER, CENTER, 1))
    listButtonsManual.append(btn.ButtonTemplate(width-90, height-35, 150, 40, "NEXT", 14, color(255,255,255), CENTER, CENTER, 1))
    listButtonsManual.append(btn.ButtonTemplate(width-90, height-35, 150, 40, "CLOSE", 14, color(255,255,255), CENTER, CENTER, 1))

def draw():
    global currentScreen, test, diceSound, rollOnce, soundtrack, creepySoundtrack, playOnce, gunSound, teams

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
        manual_screen.draw(manualPage)
        
        # Show current button of the current page
        listButtonsManual[manualPage].Show()
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
        player_inventory.teams = teams

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
        player_inventory.turn = player_dashboard.turn
        player_inventory.setup()
    elif player_dashboard.curScreen == 'fighting_screen':
        player_dashboard.curScreen = 'none'
        currentScreen = 'fighting_screen'
        fighting_screen.teams = teams
        fighting_screen.turn = player_dashboard.turn
        fighting_screen.setup()
    elif player_inventory.curScreen == 'dice_system':
        player_inventory.curScreen = 'none'
        currentScreen = 'dice_system'
        dice_system.setup()
        dice_system.doubleThrow = True
        
    
    if dice_system.curScreen == 'player_dashboard':
        dice_system.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()
    elif dice_system.curScreen == 'fighting_screen':
        dice_system.curScreen = 'none'
        currentScreen = 'fighting_screen'
        fighting_screen.teams = teams
        fighting_screen.turn = player_dashboard.turn
        fighting_screen.setup()
    if player_inventory.curScreen == 'player_dashboard':
        player_inventory.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()
    if player_inventory.curScreen == 'fighting_screen':
        player_inventory.curScreen = 'none'
        currentScreen = 'fighting_screen'
        fighting_screen.extraDamage = 2
        fighting_screen.teams = teams
        fighting_screen.turn = player_dashboard.turn
        fighting_screen.setup()
    if fighting_screen.curScreen == 'player_dashboard':
        fighting_screen.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()
        dice_system.rollResult = None
        dice_system.doubleThrow = False
    if fighting_screen.curScreen == 'player_dashboard_newturn':
        fighting_screen.curScreen = 'none'
        currentScreen = 'player_dashboard'
        player_dashboard.setup()
        dice_system.rollResult = None
        dice_system.doubleThrow = False
        
    if player_dashboard.curScreen == 'napalm':
        player_dashboard.curScreen = 'none'
        currentScreen = 'start'
        teams = [[], [], [], []]
        player_dashboard.turn = [0, 0]
        player_selection.teams = teams
        player_selection.buttons.clear()
        player_selection.nameBoxes = []
        player_dashboard.buttons.clear()

    if dice_system.rollDone == True:
        rollOnce = True
    if dice_system.playSound == True and rollOnce:
        #diceSound.stop()
        #rollOnce = False
        #diceSound.play()
        dice_system.playsound = False
    if player_selection.stopSoundtrack == True and playOnce:
        #soundtrack.stop()
        playOnce = False
        #gunSound.play()
        #creepySoundtrack.play()
        #creepySoundtrack.loop()
    


    # Reset properties
    rectMode(CORNER)
    textAlign(LEFT, BASELINE)


def mousePressed():
    global currentScreen, listButtonsManual, manualPage
    
    if currentScreen == 'start':
        player_selection.setup()
        currentScreen = 'player_selecting'
        player_selection.tick = start_screen.tick
    elif currentScreen == 'manual_screen':
        
        # Check click of the current button
        if listButtonsManual[manualPage].CheckClick(mouseX, mouseY):
            
            # Next page
            manualPage+=1
            
            # Over the limit, go to the menu
            if manualPage > 2:
                manualPage=0
                currentScreen = 'player_selecting'
            
        player_selection.curScreen = ''
    else:
        elements.mousePressed()

def keyPressed():
    elements.keyPressed()
