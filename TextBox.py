import functions
import elements

class TextBox:
    def __init__(self, placeHolder = '', pos = [], padding = [], fillColor = '', txtColor = '', txtSize = 0, tag = '', initiate = True, willDraw = True):
        self.type = 'textbox'
        self.placeHolder = placeHolder
        self.pos = pos
        self.padding = padding
        self.origFillColor = fillColor
        self.fillColor = fillColor
        self.txtColor = txtColor
        self.txtSize = txtSize if txtSize > 0 else 32
        self.state = 'ready'
        self.tag = tag
        self.tick = 0
        self.willDraw = willDraw
        
        if initiate:
            self.initiate()
            
        elements.elements.append(self)
            
    def initiate(self):
        textSize(self.txtSize)
        
        txtWidth = textWidth(self.placeHolder) if len(self.placeHolder) > 2 else textWidth('WWW')
        activeColor = '255' if self.state == 'ready' else '0,255,0' if self.state == 'active' and len(self.placeHolder) >= 3 else '255, 0, 0'
        functions.addFigure('rect', self.pos, [txtWidth + self.padding[0] + 20, self.txtSize + self.padding[1] + 20], activeColor)
        functions.addFigure('rect', self.pos, [txtWidth + self.padding[0] + 15, self.txtSize + self.padding[1] + 15], self.fillColor)
    
        if len(self.placeHolder) > 0:
            functions.addText(self.placeHolder, [self.pos[0], self.pos[1] + 10], self.txtColor, self.txtSize)
        
        left = self.pos[0] - (txtWidth + self.padding[0] + 10) / 2
        right = self.pos[0] + (txtWidth + self.padding[1] + 10) / 2
        top = self.pos[1] - self.txtSize / 2 - self.padding[1]
        bottom = self.pos[1] + self.txtSize / 2 + self.padding[1]
        
        if len(self.placeHolder) < 3 and functions.toPulse(self.tick, 40) > 20:
            offset = 5 if len(self.placeHolder) > 0 else 0
            
            stroke('#ffffff')
            strokeWeight(3)
            line(self.pos[0] + textWidth(self.placeHolder) / 2 + offset, top + 3, self.pos[0] + textWidth(self.placeHolder) / 2 + offset, bottom - 3)
    
        self.borders = {'left': left, 'right': right, 'top': top, 'bottom': bottom}
        self.tick = self.tick + 1
        
    def destroy(self):
        for element in elements.elements:
            if element == self:
                elements.elements.remove(element)
        
        del self
