fonts = ["Choose a font: ", "Arial Bold", "Comic Sans", "Impact", "Pixel", "Webdings"]

def getFont(fontChoice):
    for font in fonts:
        if font == fontChoice:
            return font + ".ttf"
