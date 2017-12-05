"""
https://github.com/Arc39/CST205Memes
Carlos Estrada, Jacob Gull, Kara Spencer
CST205 Fall 2017
Meme Generator - PyQt5 GUI program to make your own custom meme.

"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
from PIL import ImageFilter

""" Gets font to use on meme
    Note: Webdings purposely doesn't work """
fonts = ["Choose a font: ", "Arial Bold", "Comic Sans", "Impact", "Pixel", "Webdings"]
def getFont(fontChoice):
    for font in fonts:
        if font == fontChoice:
            return "Font/" + font + ".ttf"

filterlist = ["Choose a filter: ", "Deep Frier", "Grayscale", "Inverted", "Emoji"]

""" Deep fries images """
def deepfrier(image):
    # Applies various filters to the image
    image = image.filter(ImageFilter.DETAIL)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.filter(ImageFilter.SHARPEN)
    image.save("copy.jpg")

""" Converts to grayscale """
def grayscale(image):
    new_list = []
    newimage = Image.new("RGB", (image.width, image.height), "white")
    for p in image.getdata():
        intensity = int((p[0] + p[1] + p[2])/3)
        temp = (intensity, intensity, intensity)
        new_list.append(temp)
    newimage.putdata(new_list)
    newimage.save("copy.jpg")

"""Applies inverted color effect to image """
def invertColor(image):
    inverted_image = ImageOps.invert(image) #inverts the color.
    inverted_image.save("copy.jpg")# Result picture.


"""
This function adds the text on top of the image.
There is a top caption and bottom caption for text.
"""

def addText(topCap,bottomCap,imgFont,color):
	meme = Image.open("copy.jpg")
	imageSize = meme.size
	w, h = imageSize
	fontSize = int(imageSize[1]/5)

	drawTop = ImageDraw.Draw(meme)
	drawBottom = ImageDraw.Draw(meme)

    # Gets text from line edit and makes it Upper Case
	text1 = topCap.text().upper()
	text2 = bottomCap.text().upper()

	font = ImageFont.truetype(imgFont, fontSize)

	textSize = drawTop.textsize(text1,font)
	textSize2 = drawBottom.textsize(text2, font)

	while textSize[0] > imageSize[0] - 20 or textSize2[0] > imageSize[0] - 20:
		fontSize = fontSize - 1
		font = ImageFont.truetype(imgFont, fontSize)
		textSize = drawTop.textsize(text1,font)
		textSize2 = drawBottom.textsize(text2, font)

	topTextPosX = (imageSize[0]/2) - (textSize[0]/2)
	bottomTextPosX = (imageSize[0]/2) - (textSize2[0]/2)
	bottomTextPosY = (imageSize[1] - textSize2[1]- 10)

	drawTop.text((topTextPosX,0), text1, color, font=font) #(location, string, color, font)
	drawBottom.text((bottomTextPosX,bottomTextPosY), text2,color, font=font)
	return meme
