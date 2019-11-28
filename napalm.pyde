import functions
import TextBox
import elements
import start_screen
import player_selection
import player_dashboard

# functions.py is where all the useful functions are located (It makes your life easier)
# start_screen.py is for the start screen!

currentScreen = 'start'

def setup():
    size(1600, 900)
    functions.setup()
    player_selection.setup()

def draw():
    fill(255)
    noStroke()
    rect(0, 0, 1600, 900)
    
    if currentScreen == 'start':
        start_screen.draw()
    
    elif currentScreen == 'player_selecting':
        player_selection.draw()
        
def mousePressed():
    global currentScreen
    
    if currentScreen == 'start':
        currentScreen = 'player_selecting'
        player_selection.tick = start_screen.tick
    else:
        elements.mousePressed()
        
def keyPressed():
    elements.keyPressed()
