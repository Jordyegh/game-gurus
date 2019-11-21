import functions
import start_screen

# functions.py is where all the useful functions are located (It makes your life easier)
# start_screen.py is for the start screen

currentScreen = 'start'

def setup():
    size(1600, 900)

def draw():
    fill(255)
    noStroke()
    rect(0, 0, 1600, 900)
    
    if currentScreen == 'start':
        start_screen.draw()
