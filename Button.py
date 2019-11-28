import functions
import elements

class Button:
    def __init__(self, placeHolder = '', pos = [], padding = [], fillColor = '', borderColor = 'none', txtColor = '', txtSize = 32, initiate = False):
        self.type = 'button'
        self.placeHolder = placeHolder
        self.pos = pos
        self.padding = padding
        self.fillColor = fillColor
        self.origFillColor = fillColor
        self.borderColor = borderColor
        self.txtColor = txtColor
        self.txtSize = 32
        self.state = 'ready'

        if initiate:
            self.initiate()

        elements.elements.append(self)

    def initiate(self):
        textSize(self.txtSize)
        txtWidth = textWidth(self.placeHolder)

        functions.addFigure('rect', self.pos, [txtWidth + self.padding[0], self.txtSize + self.padding[1]], self.fillColor, 'none' if self.borderColor == 'none' else self.borderColor)

        if len(self.placeHolder) > 0:
            functions.addText(self.placeHolder, [self.pos[0], self.pos[1] + self.txtSize / 2 - 5], self.txtColor, self.txtSize)

        line(self.pos[0] - txtWidth / 2, self.pos[1] + self.txtSize / 2, self.pos[0] + txtWidth / 2, self.pos[1] + self.txtSize / 2)

        left = self.pos[0] - (txtWidth + self.padding[0]) / 2
        right = self.pos[0] + (txtWidth + self.padding[0]) / 2
        top = self.pos[1] - (self.txtSize + self.padding[1]) / 2
        bottom = self.pos[1] + (self.txtSize + self.padding[1]) / 2
        self.borders = {'left': left, 'right': right, 'top': top, 'bottom': bottom}
