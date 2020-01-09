from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1400, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
para = [
        {'title': 'Weapon tile', 
         'desc': '3x1 is the damage of the weapon\nfor this example, the weapon will do 1 damage for\n3 times.The ruler stands for the range of the weapon.\nThe steps shows how many steps you have\nto step back after using your the weapon.',
         'img': '/img/guntegel.png'},
        {'title': 'Landmine', 
         'desc': 'The player must try to avoid the landmine.\nLanding on a landmine and also turning it around,\ncauses damage to the player.\nThe player does not know the locations\nof the landmines beforehand. If the player chooses not \nto turn it over,he remains unharmed.\n',
         'img': '/img/landmijn.png'},
        {'title': 'Smoke Grenade', 
         'desc': 'A Smoke Grenade helps the player escape a fight.',
         'img': '/img/rookbom.png'},
        {'title': 'Stim Pack', 
         'desc': 'With a stim pack you can get extra range or damage\nThis effect lasts for 1 turn.\nYou must use the stim pack before the start of your turn.',
         'img': '/img/stimpack.png'},
        {'title': 'Bandage', 
         'desc': 'This item heals the player\n(not more than the maximum health)\nthere are different levels of healing,\n for example +2 or +4. If you use a bandage,\nyour turn will be over.',
         'img': '/img/pleistertegel.png'},
        {'title': 'Armor', 
        'desc': 'This item gives you extra health,more than\nthe maximum of 5 health you are allowed to\nhave.The tile itself will show how much protection you\nwill get.The player must dice in order to have the armour\nworking,If you get a number between 1-3, the armour will\nNOT work.It will only work if you get a number between\n4-6.',
        'img': '/img/armor.png'}
        ]

def addDescription(title = 'Title', desc = 'Description', pos = [100, 100], img = '/img/guntegel.png'):
    addText(title, pos, '255', 24)
    addText(desc, [pos[0], pos[1] + 20], '255', 18)
    addImage(img, [pos[0] + 300, pos[1]], [150,150])

def draw(manualPage):
    global screenSize, center, tick, para

    fade = tick * 2.5
    addImage('/img/backgroundWoods.png', [center[0], 0], [1900, 900])
    
    # Use 'manualPage' with an 'if' condition to show the correctly page
    
    if manualPage==0:
        for y in range(0, 3):
            for x in range(0, 2):
                id = x + y * 2
                
                if id < len(para):
                    addDescription(para[id]['title'], para[id]['desc'], [250 + x * 700, 200 + y * 200], para[id]['img'])
        
        addText('Manual screen', [375, 75], '255', 64, 'scorch')
        addText('', [130, 175], '255', 34)
    
    if manualPage==1:
        img = loadImage("/img/Board.png")
        img.resize(width/2,0)
        image(img,width/4,20)
        
        fill(255)
        textAlign(CENTER,TOP)
        textSize(22)
        text("The board game is split into 6x6 square tiles. In the 4 corners of the board are the places where the keys are located and in the center of the board is where you will find the bunker (The finish). There are gates around the bunkers that the player must open with a key. The quantity of the keys that are required to open the gates varies per game. For every player playing there is 1 key on the board (max 4). You always need at least 1 key to open the bunker. If you play with 4 teams, there will be 4 keys in the game and you will have to get 2 to open the gate. The players are free to choose which keys they want to get in the game (see image below).",
             width/10-80, height/2, width/2-20,height)
        
    if manualPage==2:
        img = loadImage("/img/Dashboard.png")
        img.resize(width/2,0)
        imageMode(CENTER)
        image(img,width/2,height/2)
        
    textAlign(LEFT, BASELINE)
    imageMode(CORNER)
    addText('Click to go next', [660, center[1] + 390], str(25 + toPulse(fade, 220)), 35)
    
    tick = tick + 1
    
    
                       # Size of our screen, [0] is Width and [1] is Height
                       
