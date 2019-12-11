fonts = {}
images = {}

def setup():
    global fonts

    fonts['default'] = createFont('Arial', 32)
    fonts['scorch'] = createFont('Scorchedearth.otf', 32)

# This function accepts color as #fff, #ffffff, 255,255,255 and 255 and coverts it to an acceptable color code
# toColor(COLOR|string)
def toColor(sColor):
    if sColor[0] == '#':
        fill(sColor)
    elif len(sColor.split(',')) >= 3:
        lColor = sColor.split(',')
        fill(int(lColor[0]), int(lColor[1]), int(lColor[2]))
    else:
        fill(int(sColor))

# Use this for placing text on the screen
# addText(TEXT|string, POSITION|list:2, COLOR|string in rgb or hex, FONT SIZE|int)
def addText(txt, pos, txtColor, txtSize, font = '', centerVert = False):
    global fonts

    toColor(txtColor)

    textFont(fonts[font] if len(font) > 0 else fonts['default'])
    textSize(txtSize)
    text(txt, pos[0] - (textWidth(txt) / 2), pos[1] - (txtSize / 2) if centerVert else pos[1])

# Use this for placing images on the screen
# addImage(IMG SOURCE|string, POSITION|list:2, IMG SIZE|list:2)
def addImage(src, pos, imgSize, VertAlign = False):
    global images

    if not src in images:
        images[src] = loadImage(src)

    img = images[src]
    img.resize(imgSize[0], imgSize[1])
    image(img, pos[0] - imgSize[0] / 2, pos[1] if not VertAlign else pos[1] - imgSize[1] / 2)

# Use this for placing figures on the screen
# addFigure(FIGURE|string, POSITION|list:2, FIG SIZE|list:2, FIG COLOR|string, STROKE COLOR|string)
def addFigure(fig, pos, figSize, figColor, strokeColor = 'none'):
    toColor(figColor)

    if strokeColor == 'none':
        noStroke()
    else:
        stroke(strokeColor)

    if fig == 'rect':
        rect(pos[0] - (figSize[0] / 2), pos[1] - (figSize[1] / 2), figSize[0], figSize[1])

# Converts decimal to a value between 0 and 255 (Goes from 0 to maxNum and then back from maxNum to 0 in steps like a pulse)
# toPulse(INPUT DECIMAL|float, INTEGER MAX|int)
def toPulse(num, maxNum):
    return abs(((floor(num / maxNum) % 2) * maxNum) - (int(num) % maxNum))
