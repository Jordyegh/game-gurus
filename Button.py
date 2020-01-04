from functions import *
from TextBox import *
from Button import *
import elements

class Button:
    def __init__(self, placeHolder = '', pos = [], padding = [], fillColor = '#eeeeee', borderColor = 'none', txtColor = '#000000', hoverColor = '#ffffff', txtSize = 32, initiate = False, linked = [], willDraw = True, borderRadius = 0):
        self.type = 'button'
        self.placeHolder = placeHolder
        self.pos = pos
        self.padding = padding
        self.fillColor = fillColor
        self.origFillColor = fillColor
        self.borderColor = borderColor
        self.txtColor = txtColor
        self.hoverColor = hoverColor
        self.txtSize = 32
        self.state = 'ready'
        self.linked = linked
        self.willDraw = willDraw
        self.borderRadius = borderRadius
        self.onHover = False

        if initiate:
            self.initiate()

        elements.elements.append(self)

    def initiate(self):
        textSize(self.txtSize)
        txtWidth = textWidth(self.placeHolder)
            
        if self.placeHolder[0:5] == '/img/':
            functions.addImage(self.placeHolder, self.pos, self.padding, True)
            txtWidth = 0
        else:
            functions.addFigure('rect', self.pos, [txtWidth + self.padding[0], self.txtSize + self.padding[1]], self.fillColor, 'none' if self.borderColor == 'none' else self.borderColor, borderRadius = self.borderRadius)
            if len(self.placeHolder) > 0:
                functions.addText(self.placeHolder, [self.pos[0], self.pos[1] + self.txtSize / 2 - 5], self.txtColor, self.txtSize)
    
            line(self.pos[0] - txtWidth / 2, self.pos[1] + self.txtSize / 2, self.pos[0] + txtWidth / 2, self.pos[1] + self.txtSize / 2)
    
        left = self.pos[0] - (txtWidth + self.padding[0]) / 2
        right = self.pos[0] + (txtWidth + self.padding[0]) / 2
        top = self.pos[1] - (self.txtSize + self.padding[1]) / 2
        bottom = self.pos[1] + (self.txtSize + self.padding[1]) / 2
        self.borders = {'left': left, 'right': right, 'top': top, 'bottom': bottom}
        
    def destroy(self):
        for element in elements.elements:
            if element == self:
                elements.elements.remove(element)
        
        del self
