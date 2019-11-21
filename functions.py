# Use this for placing text on the screen
# This function accepts text color as #fff, #ffffff, 255,255,255 and 255
# placeText(TEXT|string, POSITION|list:2, COLOR|string in rgb or hex, FONT SIZE|int)
def placeText(txt, pos, txtColor, txtSize):
    if txtColor[0] == '#':
        fill(txtColor)
    elif len(txtColor.split(',')) >= 3:
        lColor = txtColor.split(',')
        fill(int(lColor[0]), int(lColor[1]), int(lColor[2]))
    else:
        fill(int(txtColor))
        
    textSize(txtSize)
    text(txt, pos[0] - (textWidth(txt) / 2), pos[1])


# Use this for placing images on the screen
# placeImage(IMG SOURCE|string, POSITION|list:2, IMG SIZE|list:2)
def placeImage(src, pos, imgSize):
    img = loadImage(src)
    img.resize(imgSize[0], imgSize[1])
    
    image(img, pos[0] - imgSize[0] / 2, pos[1])


# Converts decimal to a value between 0 and 255 (Goes from 0 to 255 and then back from 255 to 0 in steps)
# toAlpha(DECIMAL|float)
def toAlpha(num):
    return abs(((floor(num / 255) % 2) * 255) - (int(num) % 255))
