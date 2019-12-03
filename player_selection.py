from functions import *
from TextBox import *
from Button import *
from Player import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
playerBox = []
buttons = {}
teams = [[], [], [], []]
curScreen = ''

def addPlayerButton(team):
    yOffset = 100 * len(teams[team]) * (1 - 2 * (team // 2))
    textBoxPos = [300 + (300 * (team % 2)), center[1] - 150 + (400 * (team // 2) + yOffset)]
    buttons['addPlayer' + str(team)] = Button('Add Player', [textBoxPos[0], center[1] - 50 + (200 * (team // 2))], [25, 10], '235,255,235', 'none', '0', '200,255,200')

def addPlayerField(team):
    yOffset = 100 * len(teams[team]) * (1 - 2 * (team // 2))
    textBoxPos = [300 + (300 * (team % 2)), center[1] - 150 + (400 * (team // 2) + yOffset)]
    takenIds = []
    availableId = 1
    
    for lTeam in teams:
        if len(lTeam) > 0:
            for player in lTeam:
                takenIds.append(player.id)

    while availableId in takenIds:
        availableId = availableId + 1
    
    playerBox.append(TextBox('Player ' + str(availableId), textBoxPos, [0, 0], '0', '255', 0, 'team' + str(team)))
    buttons['removePlayer' + str(availableId)] = Button('/img/red_cross.png', [150 + (600 * (team % 2)), textBoxPos[1]], [50, 50], linked = [len(playerBox) - 1])
    teams[team].append(Player('Player ' + str(availableId), id = availableId))
    
    if len(teams[team]) == 1:
        buttons['addPlayer' + str(team)] = Button('Add Player', [textBoxPos[0], center[1] - 50 + (200 * (team // 2))], [25, 10], '235,255,235', 'none', '0', '200,255,200')
    elif len(teams[team]) == 2:
        buttons['addPlayer' + str(team)].destroy()
        del buttons['addPlayer' + str(team)]

def setup():
    buttons['startGame'] = Button('START GAME', [screenSize[0] - 350, 200], [50, 25], '200', 'none', '0')
    
    for i in range(0, 4):
        addPlayerField(i)

def draw():
    global screenSize, center, tick, curScreen

    flameSpeed = [tick / 3.5, tick / 5]

    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    addText('Player Selection', [center[0], 75], '255', 64, 'scorch')

    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])
    
    addText('Team 1', [300, center[1] - 250], '255', 48, 'scorch')
    addText('Team 2', [600, center[1] - 250], '255', 48, 'scorch')
    addText('Team 3', [300, center[1] + 350 + 24], '255', 48, 'scorch')
    addText('Team 4', [600, center[1] + 350 + 24], '255', 48, 'scorch')
    
    stroke('#ffffff')
    strokeWeight(5)
    line(150, center[1] + 50, 750, center[1] + 50)
    line(450, center[1] - 250, 450, center[1] + 350)
    
    for i in range(1, 9):
        if ('removePlayer' + str(i)) in buttons and buttons['removePlayer' + str(i)].state == 'clicked':
            for element in elements.elements:
                if ('removePlayer' + str(i)) in buttons and buttons['removePlayer' + str(i)] == element:
                    tag = playerBox[element.linked[0]].tag
                    teamId = int(tag[len(tag) - 1])
                    
                    for player in teams[teamId]:
                        if player.id == i:
                            teams[teamId].remove(player)
                            player.destroy()
                            
                            if len(teams[teamId]) == 1:
                                addPlayerButton(teamId)

                                playerId = teams[teamId][0].id
                                
                                if ('removePlayer' + str(playerId)) in buttons:
                                    yOffset = 100 * len(teams[teamId]) * (1 - 2 * (teamId // 2))
                                    textBoxPos = [300 + (300 * (teamId % 2)), center[1] - 150 + (400 * (teamId // 2) + yOffset)]
    
                                    buttons['removePlayer' + str(playerId)].pos = [textBoxPos[0] - 150 + (300 * (teamId % 2)), textBoxPos[1] - 100 + (200 * (teamId // 2))]
                                    playerBox[buttons['removePlayer' + str(playerId)].linked[0]].pos = [textBoxPos[0], textBoxPos[1] - 100 + (200 * (teamId // 2))]
                
                    playerBox[element.linked[0]].destroy()
                    elements.elements.remove(element)
                    
                    for e in elements.elements:
                        if e == playerBox[element.linked[0]]:
                            elements.elements.remove(e)
                    
                    del buttons['removePlayer' + str(i)]
                    
    for team in teams:
        teamId = teams.index(team)
        if ('addPlayer' + str(teamId)) in buttons and buttons['addPlayer' + str(teamId)].state == 'clicked':
            addPlayerField(teamId)

    if buttons['startGame'].state == 'clicked':
        curScreen = 'player_dashboard'

    tick = tick + 1

    elements.updateElements()
