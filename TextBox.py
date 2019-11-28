import functions
import elements

class TextBox:
    def __init__(self, placeHolder = '', pos = [], boxSize = [], fillColor = '', txtColor = '', txtSize = 0, initiate = False):
        self.type = 'textbox'
        self.placeHolder = placeHolder
        self.pos = pos
        self.boxSize = boxSize
        self.origFillColor = fillColor
        self.fillColor = fillColor
        self.txtColor = txtColor
        self.txtSize = txtSize if txtSize > 0 else boxSize[1]
        self.state = 'ready'
        
        if initiate:
            self.initiate()
            
        elements.elements.append(self)
            
    def initiate(self):
        functions.addFigure('rect', self.pos, self.boxSize, self.fillColor)
    
        if len(self.placeHolder) > 0:
            functions.addText(self.placeHolder, [self.pos[0], self.pos[1] + self.boxSize[1] / 2 - 5], self.txtColor, self.txtSize)
        
        stroke('#999999')
        strokeWeight(2)
        line(self.pos[0] - self.boxSize[0] / 2, self.pos[1] + self.boxSize[1] / 2, self.pos[0] + self.boxSize[0] / 2, self.pos[1] + self.boxSize[1] / 2)
    
        self.borders = {'left': self.pos[0] - self.boxSize[0] / 2, 'right': self.pos[0] + self.boxSize[0] / 2, 'top': self.pos[1] - self.boxSize[1] / 2, 'bottom': self.pos[1] + self.boxSize[1] / 2}
