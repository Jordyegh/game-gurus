elements = []
typing = False

def updateElements():
    for element in elements:
        element.initiate()
        
        if mouseX >= element.borders['left'] and mouseX <= element.borders['right'] and mouseY >= element.borders['top'] and mouseY <= element.borders['bottom']:
            if element.type == 'textbox':
                element.fillColor = '#ffffff'
            elif element.type == 'button':
                element.fillColor = element.hoverColor
        elif hasattr(element, 'origFillColor'):
            if element.fillColor != element.origFillColor and element.state != 'active':
                element.fillColor = element.origFillColor
            
def mousePressed():
    global typing
    
    for element in elements:
        if mouseX >= element.borders['left'] and mouseX <= element.borders['right'] and mouseY >= element.borders['top'] and mouseY <= element.borders['bottom']:
            if element.type == 'textbox' and not typing:
                element.placeHolder = ''
                element.state = 'active'
                typing = True
            elif element.type == 'button':
                element.state = 'clicked'
                
def keyPressed():
    global typing
    
    if typing:
        for element in elements:
            if element.type == 'textbox' and element.state == 'active':
                txt = element.placeHolder
                if ((keyCode >= 65 and keyCode <= 90) or (keyCode >= 48 and keyCode <= 57)) and len(txt) < 8:
                    element.placeHolder = txt + str(key)
                elif keyCode == 8 and len(txt) > 0:
                    element.placeHolder = txt[0:len(txt) - 1]
                elif keyCode == 10:
                    element.state = 'ready'
                    typing = False
                    
                    if len(txt) <= 0:
                        element.placeHolder = '???'
            
