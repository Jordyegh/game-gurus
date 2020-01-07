from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
teams = [[], [], [], []]
buttons = {}
turn = [0, 0]
curScreen = ''
headerMsg = 'CHOOSE WHO TO FIGHT'
versus = [None, None]
dots = None 
roll = 0
rolls = [[], []]
ended = 0
extraDamage = 0
chosenWeapons = [None, None]
chosenArmor = [0, 0]
weaponSelection = False
weapons = [
           {'src': '9mm.jpeg', 'name': '9mm Pistol', 'damage': 1, 'shots': 1, 'steps': 0},
           {'src': 'dual_9mm.jpeg', 'name': 'Dual 9mm Pistols', 'damage': 1, 'shots': 2, 'steps': 0},
           {'src': 'mp5.jpeg', 'name': 'MP5 SMG', 'damage': 1, 'shots': 3, 'steps': 0},
           {'src': 'p90.jpeg', 'name': 'P90 SMG', 'damage': 1, 'shots': 4, 'steps': -1},
           {'src': 'assault_rifle.jpeg', 'name': 'Assault Rifle', 'damage': 2, 'shots': 1, 'steps': -1},
           {'src': 'ak47.jpeg', 'name': 'AK47 Rifle', 'damage': 3, 'shots': 1, 'steps': -1},
           {'src': 'lmg.jpeg', 'name': 'Light Machine Gun', 'damage': 2, 'shots': 3, 'steps': -2},
           {'src': 'sniper_rifle.jpeg', 'name': 'Sniper Rifle', 'damage': 4, 'shots': 1, 'steps': -3}
]

def initWeaponTiles():
    global buttons
    
    buttons['weapons'] = []
    buttons['smoke'] = {}
    buttons['armor'] = []
    
    for i in range(0, 2):
        buttons['weapons'].append({})
        buttons['armor'].append({})
        
        for y in range(0, 3):
            for x in range(0, 3):
                if y != 2 or x != 2:
                    id = y * 3 + x
                    buttons['weapons'][i][id] = Button('/img/' + weapons[id]['src'], [center[0] - 450 + 150 * x + 575 * i, center[1] - 150 + (y * 150)], [125, 125])
        
            buttons['armor'][i][y] = Button('/img/armor_' + str(y + 1) + '.jpeg', [center[0] - 650 + 1275 * i, center[1] - 150 + (y * 150)], [125, 125])
        
        buttons['smoke'][i] = Button('/img/smoke_grenade.png', [center[0] - 150 + 575 * i, center[1] + 150], [125, 125])
    
def resetScreen():
    global curScreen, headerMsg, weaponSelection, chosenArmor, versus, chosenWeapons, turn, roll
    
    clearScreen()
    chosenWeapons = [None, None]
    chosenArmor = [0, 0]
    versus = [None, None]
    weaponSelection = False
    headerMsg = 'CHOOSE WHO TO FIGHT'
    nextTurn(turn)
    curScreen = 'player_dashboard'
    roll = 0

def setup():
    global buttons, turn, dots
    
    buttons['return'] = Button('Return', [100, 65], [25, 15], '#cccccc')
    buttons['player_buttons'] = {}
    
    x = 0
    for team in teams:
        y = 0
        
        if x != turn[0]:
            for player in team:
                if player.health > 0:
                    buttons['player_buttons'][player.id] = Button(player.name, [center[0] - 400 + x * 200, center[1] - 50 + y * 100], [35, 10])
                    y = y + 1
        
        x = x + 1
        
    dots = functions.getDicePos(100, 100)

def draw():
    global teams, buttons, curScreen, headerMsg, versus, weaponSelection, dots, roll, rolls, chosenWeapons, chosenArmor, ended, extraDamage
    
    addImage('/img/Dashboard_background.jpg', [center[0], 0], [1600, 900])
    
    addText(headerMsg, [center[0] - 10, 100 + 5], '0', 64, font = 'scorch')
    addText(headerMsg, [center[0], 100], '255', 64, font = 'scorch')
            
    if weaponSelection:
        for i in range(0, 2):
            healthWidth = int(450 * (versus[i].health / 5.0))
            
            if healthWidth <= 0:
                healthWidth = 1
                
            addFigure('rect', [center[0] - 300 + 575 * i, 165], [465, 65], '0')
            addFigure('rect', [center[0] - 300 + 575 * i, 165], [healthWidth, 50], '50,200,50')
            addImage('/img/noise.png', [center[0] - 300 + 575 * i, 140], [healthWidth + 15, 50])
                
        if chosenWeapons[0] == None or chosenWeapons[1] == None:
            addText('Select your weapon', [center[0] - 10, center[1] * 2 - 95], '#000000', 48, 'scorch')
            addText('Select your weapon', [center[0], center[1] * 2 - 100], '#ffffff', 48, 'scorch')
            addFigure('rect', [center[0] - 300, center[1]], [475, 475], '#000000')
            addFigure('rect', [center[0] + 275, center[1]], [475, 475], '#000000')
            
            addFigure('rect', [center[0] - 650, center[1]], [175, (475 if chosenArmor[0] == 0 else 175)], '#000000')
            addFigure('rect', [center[0] + 625, center[1]], [175, (475 if chosenArmor[1] == 0 else 175)], '#000000')
            
            for p in range(0, 2):
                for i in buttons['weapons'][p]:
                    el = buttons['weapons'][p][i]
                    
                    if el.onHover:
                        addFigure('rect', el.pos, [135, 135], '#ff0000')
                        
                    if el.state == 'clicked':
                        for u in range(0, 8):
                            if u in buttons['weapons'][p] and buttons['weapons'][p][u] != buttons['weapons'][p][i]:
                                buttons['weapons'][p][u].destroy()
                                del buttons['weapons'][p][u]
                                
                        buttons['smoke'][p].destroy()
                        del buttons['smoke'][p]
                                
                        chosenWeapons[p] = weapons[i]
                        rolls[p] = []
                        
                        for i in range(0, weapons[i]['shots']):
                            rolls[p].append(0)
                        
                        el.state = 'ready'
                        el.canClick = False
                        
                        break
                    
                for id in buttons['smoke']:
                    if buttons['smoke'][id].onHover:
                        addFigure('rect', buttons['smoke'][id].pos, [135, 135], '#ff9900')
                        
                    if buttons['smoke'][id].state == 'clicked':
                        buttons['smoke'][id].state = 'ready'
                        resetScreen()
                        curScreen = 'player_dashboard_newturn'
                        
                for id in buttons['armor'][p]:
                    button = buttons['armor'][p][id]
                    
                    if button.onHover:
                        addFigure('rect', button.pos, [135, 135], '#00aaff')
                        
                    if button.state == 'clicked':
                        for i in buttons['armor'][p]:
                            if buttons['armor'][p][id] != buttons['armor'][p][i]:
                                buttons['armor'][p][i].destroy()
                                del buttons['armor'][p][i]
                                
                        button.state = 'ready'
                        button.canClick = False
                        button.pos[1] = center[1]
                        chosenArmor[p]= (id + 1)
                        break
                        
        else:
            roll = roll + 0.25
            
            side = 0
            for rem in buttons['weapons']:
                for elId in rem:
                    el = rem[elId]
                    el.pos = [center[0] - 300 + 575 * (side % 2), center[1]]
                    
                side = side + 1
            
            side = 0
            for weapon in chosenWeapons:
                
                for i in buttons['armor'][side]:
                    if (i + 1) != chosenArmor[side]:
                        buttons['armor'][side][i].destroy()
                        del buttons['armor'][side][i]
                        break
                
                for shot in range(0, weapon['shots']):
                    form = -((weapon['shots'] - 1) * 125 / 2) + shot * 125
                    pos = [center[0] - 300 + 575 * (side % 2) + form, center[1] + 150]
                    addFigure('rect', pos, [115, 115], '#ffffff')
                
                    if rolls[side][shot] < 20 + 20 * shot:
                        if versus[0].health > 0 and versus[1].health > 0:
                            rolls[side][shot] = rolls[side][shot] + 0.25
                        
                        if rolls[side][shot] >= 20 + 20 * shot:
                            rolls[side][shot] = rolls[side][shot] + random(0, 5)
                            
                            damage = weapon['damage'] - chosenArmor[1 - side] if (rolls[side][shot] % 6) <= 3 else weapon['damage']
                            
                            if damage <= 0:
                                continue
                            
                            versus[1 - side].health = versus[1 - side].health - damage
                            
                            print(shot, weapon['shots'] - 1)
                            if shot >= (weapon['shots'] - 1):
                                ended = ended + 1
                                print('Out of ammo, ended: ', ended)
                                
                            if versus[1 - side].health <= 0 or floor(ended) >= 2:
                                buttons['continue'] = Button('Continue', center, [25, 15], '#cccccc')
                                ended = 0
                    else:
                        if (rolls[side][shot] % 6) > 3:
                            addText('HIT!', [pos[0], pos[1] + 125], '#ccffcc', 32)
                        else:
                            addText('B. HIT!', [pos[0], pos[1] + 125], '#ffcccc', 32)
                        
                        if shot >= (weapon['shots'] - 1):
                            addText('OUT OF AMMO', [center[0] - 300 + 575 * (side % 2), pos[1] + 225], '#ffffff', 64)
                    
                    for coord in dots[floor(rolls[side][shot]) % 6]:
                        fill('#000000')
                        circle(pos[0] - 50 + coord[0], pos[1] - 50 + coord[1], 15)
                    
                side = side + 1
                
            if 'continue' in buttons and buttons['continue'].state == 'clicked':
                del buttons['continue']
                
                resetScreen()
                curScreen = 'player_dashboard_newturn'
    else:
        for id in buttons['player_buttons']:
            button = buttons['player_buttons'][id]
            
            versus[0] = teams[turn[0]][turn[1]]
            
            if button.state == 'clicked':
                for team in teams:
                    for player in team:
                        if player.id == id:
                            versus[1] = player
                            
                headerMsg = versus[0].name + '      VS      ' + versus[1].name
                button.state = 'ready'
                weaponSelection = True
                clearScreen()
                
                initWeaponTiles()
            
    if 'return' in buttons and buttons['return'].state == 'clicked':
        extraDamage = 0
        curScreen = 'player_dashboard'
        clearScreen()
    
    elements.updateElements()
