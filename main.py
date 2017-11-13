from easygui import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import PIL.ImageOps
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, 
								QVBoxLayout, QComboBox, QPushButton, QRadioButton)
from PyQt5.QtGui import QPixmap

"""
These functions are basic image filters.
"""
# def invertColor():    
#     image= Image.open("meme.jpg") # Opens up picture.
#     inverted_image = PIL.ImageOps.invert(image) #inverts the color.
#     inverted_image.save("meme.jpg")# Result picture.
   
# def blackAndWhite():
#     image_file = Image.open("meme.jpg") #Opens up picture.
#     image_file=image_file.convert('1')  #Converts image black to white.
#     image_file.save('meme.jpg') # Result picture.
# """
# This function overlays text on the meme image in white or black.

# """

def addText():
    msg = "Enter Meme Captions"
    title = "MemeGenerator"
    textLabel = QLabel()
    textLabel.setText("White or black text?")
    white = QRadioButton("White")
    white.setChecked(True)

    black = QRadioButton("Black")
    
    color = radioBtnState(white)

                      
    fieldNames = ["Top Caption", "Bottom Caption"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)
    #Makes the text Upper Case
    fieldValues[0] = fieldValues[0].upper()
    fieldValues[1] = fieldValues[1].upper()
    
    # Centers text
    meme = Image.open("copy.jpg")
    imageSize = meme.size
    fontSize = int(imageSize[1]/5)
    font = ImageFont.truetype("impact.ttf", fontSize)
    topTextSize = font.getsize(fieldValues[0])
    bottomTextSize = font.getsize(fieldValues[1])
    # Resizes text, if size of text is bigger than image
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize = fontSize - 1
        font = ImageFont.truetype("impact.ttf", fontSize)
        topTextSize = font.getsize(fieldValues[0])
        bottomTextSize = font.getsize(fieldValues[1])

    topTextPosX = (imageSize[0]/2) - (topTextSize[0]/2)
    bottomTextPosX = (imageSize[0]/2) - (bottomTextSize[0]/2)
    bottomTextPosY = (imageSize[1] - bottomTextSize[1]- 10)

    drawTop = ImageDraw.Draw(meme)
    drawBottom = ImageDraw.Draw(meme)
    drawTop.text((topTextPosX,0), fieldValues[0],(color,color,color), font=font) #(location, string, color, font)
    drawBottom.text((bottomTextPosX, bottomTextPosY), fieldValues[1],(color,color,color), font=font)
    meme.save("meme.jpg")

"""
This functions checks which radio button is selected 
for color for the addText function and returns the colors value.
"""
def radioBtnState(btn):
	if btn.text() == "White"
		if btn.isChecked == True:
			return 255
	if btn.text() == "Black"
		if btn.isChecked == True:
			return 0
# """
# This function is called when the user wants to add some sort of image filter.
# It then calls that image manipulation function.
# """
# def colorManipulation():
#     title = "Meme Generator"
#     choice = buttonbox('What manipulation would you like?', title, ('Invert Color', 'Black and White'))
#     if (choice == 'Invert Color'):
#         invertColor()
#     elif (choice == 'Black and White'):
#         blackAndWhite()


# """
# Asks user to confirm they like the meme they created.
# Gives option to redo text or apply filters.
# If yes meme is saved as user provided file name.
# """            
# def confirmation():
#     while True:
#         meme = Image.open("meme.jpg")
#         msgConfirm = "Do you like this picture?"
#         ynChoices = ["Yes", "Redo Text", "Manipulate Colors", "No"]
#         reply = buttonbox(msgConfirm, image="meme.jpg", choices=ynChoices)
#         if reply == ("Yes"):
#             saveName = enterbox("What do you want to save the meme as?", "Meme Generator", "Save Name")
#             meme.save(saveName + ".jpg")
#             break
#         elif reply == ("Redo Text"):
#             text()
#         elif reply == ("Manipulate Colors"):
#             colorManipulation()
#         else:
#             break
        
choices =['Awkward Moment Seal', 'Bad Luck Brian', 'Brace Yourself', 'Condescending Wonka', 'Desk Flip', 'Futurama Fry', 'Philosoraptor', 'Scumbag Steve', 'Success Kid', 'Create Your Own Meme']

# meme = Image.open(memePath)
# meme.save("copy.jpg") #Saves for further use
# meme = Image.open("copy.jpg") #Allows the new meme to be used


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400,200)
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(choices)
        self.button = QPushButton("Select")
        self.button.setCheckable(True)
        
        self.label = QLabel()
        self.label.setText("Select a meme background: ")
        self.imageLabel = QLabel()

        h_layout = QHBoxLayout()
        self.button.setMaximumHeight(25)
        self.button.setMaximumWidth(75)
        self.my_combo_box.setMaximumHeight(25)
        
        h_layout.addWidget(self.label)
        h_layout.addWidget(self.my_combo_box)
        h_layout.addWidget(self.button)
        h_layout.insertStretch(-1,1)

        self.button.clicked.connect(self.btnstate)
        self.setLayout(h_layout)

    def btnstate(self):
        if self.button.isChecked():
            addText(self) 



app = QApplication(sys.argv)
main = Window()
main.setWindowTitle("Meme Generator")
main.show()
sys.exit(app.exec_())		