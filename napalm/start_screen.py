from functions import *

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations

def draw():
    global screenSize, center, tick
    
    fade = tick * 20
    flameSpeed = [tick / 1.5, tick / 2.5]
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    addText('Napalm:', [500, 250], '255', 200)
    addText('The Last Survivors', [500, 350], '255', 50)
    addText('Click anywhere', [500, center[1] + 150], str(35 + toPulse(fade, 220)), 35)
    addText('To start the game', [500, center[1] + 200], str(35 + toPulse(fade, 220)), 35)

    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200 + toPulse(flameSpeed[0], 50)])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200 + toPulse(flameSpeed[1], 75)])
    
    tick = tick + 1
