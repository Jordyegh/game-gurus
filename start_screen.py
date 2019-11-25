from functions import *

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations

def draw():
    global screenSize, center, tick
    
    fade = tick * 3.5
    flameSpeed = [tick / 1.5, tick / 2.5]

    addText('Napalm:', [center[0], center[1]], '0', 200)
    addText('The Last Survivors', [center[0], center[1] + 110], '0', 50)
    addText('Click anywhere', [center[0], center[1] + 250], str(toPulse(fade, 255)), 35)
    addText('To start the game', [center[0], center[1] + 300], str(toPulse(fade, 255)), 35)
    
    addImage('/img/logo.jpeg', [center[0], 0], [200, 300])
    
    addImage('/img/fire.png', [300, screenSize[1] - 200 - toPulse(flameSpeed[0], 50)], [600, 200 + toPulse(flameSpeed[0], 50)])
    addImage('/img/fire_reverse.png', [275, screenSize[1] - 200 - toPulse(flameSpeed[1], 75)], [500, 200 + toPulse(flameSpeed[1], 75)])
    
    addImage('/img/fire.png', [screenSize[0] - 300, screenSize[1] - 200 - toPulse(flameSpeed[0], 50)], [600, 200 + toPulse(flameSpeed[0], 50)])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 200 - toPulse(flameSpeed[1], 75)], [500, 200 + toPulse(flameSpeed[1], 75)])
    
    tick = tick + 1
