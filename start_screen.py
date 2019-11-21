import functions

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations

def setup():
    pass

def draw():
    global screenSize, center, tick
    
    fade = tick * 2.5

    functions.placeText('Napalm:', [center[0], center[1]], '0', 200)
    functions.placeText('The Last Survivors', [center[0], center[1] + 110], '0', 50)
    functions.placeText('Click anywhere', [center[0], center[1] + 250], str(functions.toAlpha(fade)), 35)
    functions.placeText('To start the game', [center[0], center[1] + 300], str(functions.toAlpha(fade)), 35)
    
    functions.placeImage('/img/logo.jpeg', [center[0], 0], [200, 300])
    
    tick = tick + 1
