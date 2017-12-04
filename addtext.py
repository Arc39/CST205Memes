import fontTemplate
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL.ImageOps


def addText(topCap,bottomCap,imgFont,color):
	meme = Image.open("meme.jpg")
	imageSize = meme.size
	w, h = imageSize
	fontSize = int(imageSize[1]/5)

	drawTop = ImageDraw.Draw(meme)
	drawBottom = ImageDraw.Draw(meme)

	text1 = topCap.text()
	text2 = bottomCap.text()
	#Makes the text Upper Case
	text1 = text1.upper()
	text2 = text2.upper()

	font = ImageFont.truetype(imgFont, fontSize)

	textSize = drawTop.textsize(text1,font)
	textSize2 = drawBottom.textsize(text2, font)

	while textSize[0] > imageSize[0] - 20 or textSize2[0] > imageSize[0] - 20:
		fontSize = fontSize - 1
		font = ImageFont.truetype(imgFont, fontSize)
		textSize = text1.textsize(text1,font)
		textSize2 = text2.textsize(text2, font)

	topTextPosX = (imageSize[0]/2) - (textSize[0]/2)
	bottomTextPosX = (imageSize[0]/2) - (textSize2[0]/2)
	bottomTextPosY = (imageSize[1] - textSize2[1]- 10)

	drawTop.text((topTextPosX,0), text1, color, font=font) #(location, string, color, font)
	drawBottom.text((bottomTextPosX,bottomTextPosY), text2,color, font=font)
	return meme
