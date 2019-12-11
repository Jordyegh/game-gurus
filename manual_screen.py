from functions import *
from TextBox import *
from Button import *
import elements

screenSize = [1600, 900]                        # Size of our screen, [0] is Width and [1] is Height
center = [screenSize[0] / 2, screenSize[1] / 2] # Center of our screen, [0] is X and [1] is Y
tick = 0                                        # Tick is used like a clock, it gets incremented each frame, this can be useful for animations
para = [
        {'title': 'Wapentegel', 
         'desc': 'drie keer een is de schade wat het wapen kan\naanrichten bij dit voorbeeld zou het wapen\ndus 3 keer 1 schade aan kunnen richten.\nBij een handpistool is het bijvoorbeeld enkel 1.',
         'img': '/img/guntegel.png'},
        {'title': 'Landmijn', 
         'desc': 'Dit is een tegel die de speler moet proberen te\nvermijden. Het landen op een landmijn-tegel en\ndeze ook omdraaien, richt schade toe aan de speler.\nUiteraard weet de speler niet van tevoren of het\neen landmijn-tegel is. Als de speler ervoor kiest\nom deze niet om te draaien, blijft hij ongedeerd.',
         'img': '/img/landmijn.png'},
        {'title': 'Rookbom', 
         'desc': 'Als een speler met iemand een gevecht aan wilt\ngaan en de juiste range op zijn wapen heeft om\nook daadwerkelijk te schieten, is dit de enige\nitem waardoor je niet aangevallen kunt worden.',
         'img': '/img/rookbom.png'},
        {'title': 'Energy', 
         'desc': 'Met een stimpack krijg je een aanvalsbonus. Deze\ngeldt voor 1 beurt. Je kunt met een stimpack\nextra range krijgen of extra schade. Je moet deze\ninzetten voordat je je beurt begint.\n',
         'img': '/img/energy.png'},
        {'title': 'Pleister', 
         'desc': 'Dit item kan je health points terug geven\n(niet meer dan je maximale levens).\nEr zijn verschillende sterkte pleisters,\ndus de ene kan bijvoorbeeld zorgen voor\neen plus twee en de ander voor een plus 4.\nAls je pleisters gebruikt is je beurt voorbij.\n',
         'img': '/img/pleistertegel.png'},
        {'title': 'Armor', 
         'desc': '.\n',
         'img': '/img/armor.png'}
        ]

def addDescription(title = 'Title', desc = 'Description', pos = [100, 100], img = '/img/guntegel.png'):
    addText(title, pos, '255', 24)
    addText(desc, [pos[0], pos[1] + 20], '255', 18)
    addImage(img, [pos[0] + 300, pos[1]], [150,150])
    print('Teest')

def draw():
    global screenSize, center, tick, para
    
    fade = tick * 2.5
    flameSpeed = [tick / 3.5, tick / 5]
    addImage('/img/backgroundWoods.png', [center[0], 0], [1600, 900])
    
    for y in range(0, 3):
        for x in range(0, 2):
            id = x + y * 2
            
            if id < len(para):
                addDescription(para[id]['title'], para[id]['desc'], [250 + x * 700, 200 + y * 200], para[id]['img'])
    
    addText('Manual screen', [375, 75], '255', 64, 'scorch')
    addText('Tegels', [130, 175], '255', 34)
    #addText('Primaire voorwerpen', [200, 225], '255', 24)
    #addText('Wapentegel', [140, 255], '255', 20)
    #addText('drie keer een is de schade wat het wapen kan', [280, 275], '255', 18)
    #addText('aanrichten bij dit voorbeeld zou het wapen', [265, 295], '255', 18)
    #addText('dus 3 keer 1 schade aan kunnen richten.', [258, 315], '255', 18)
    #addText('Bij een handpistool is het bijvoorbeeld enkel 1.', [280, 335], '255', 18)
    #addImage('/img/guntegel.png', [750, 195],[150,150])
  

    #addText('Pleister', [120, 395], '255', 20)
    #addText('Dit item kan je health points terug geven', [260, 415], '255', 18)
    #addText('(niet meer dan je maximale levens). ', [245, 435], '255', 18)
    #addText('Er zijn verschillende sterkte pleisters, ', [250, 455], '255', 18)
    #addText('dus de ene kan bijvoorbeeld zorgen voor', [260, 475], '255', 18)
    #addText('een plus twee en de ander voor een plus 4.', [270, 495], '255', 18)
    #addText('Als je pleisters gebruikt is je beurt voorbij.', [260, 515], '255', 18)
    #addImage('/img/pleistertegel.png', [750, 375],[150,150])
    
    #addText('Armor', [110, 565], '255', 20)
    #addText('Dit item biedt je de mogelijkheid om meer health points ', [310, 585], '255', 18)
    #addText('te hebben dan de maximale 5 levens die je hebt. Bij de ', [310, 605], '255', 18)
    #addText('tegel wordt aangeduid hoeveel extra bescherming je hebt. ', [320, 625], '255', 18)
    #addText('De armor werkt maar voor 50% van de tijd, je moet dobbelen. ', [330, 645], '255', 18)
    #addText('Dobbel je 1 t/m 3 dan werkt hij niet. 4 t/m 6 werkt hij wel.', [310, 665], '255', 18)
    #addText('', [260, 675], '255', 18)
    #addImage('/img/armor.png', [750, 555],[150,150])
    
    
    
    addText('Click to go next', [650, center[1] + 350], str(25 + toPulse(fade, 220)), 35)
    

    addImage('/img/fire.png', [screenSize[0] - 350, screenSize[1] - 175 - toPulse(flameSpeed[0], 50)], [600, 200])
    addImage('/img/fire_reverse.png', [screenSize[0] - 275, screenSize[1] - 175 - toPulse(flameSpeed[1], 75)], [500, 200])
    
    tick = tick + 1
