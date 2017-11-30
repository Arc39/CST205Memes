# from easygui import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL.ImageOps
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout,
								QVBoxLayout, QComboBox, QPushButton, QRadioButton)
from PyQt5.QtGui import QPixmap

"""Font functions found in fontTemplate.py"""
import fontTemplate
from PyQt5.QtCore import pyqtSlot

""" Filter functions located in filters.py """
from filters import grayscale, deepfrier, invertColor


"""Text and caption selection window, still needs the font choices, submit button,
image effects, and a better looking layout"""
class TextWindow(QWidget):
    def __init__(self,meme):
        super().__init__()
        self.meme = meme
        self.setMinimumSize(400,200)
        self.setWindowTitle("Meme Generator")
        self.textLabel = QLabel()
        self.textLabel.setText("White or black text?")

        self.white = QRadioButton("White")
        self.white.setChecked(True)

        self.black = QRadioButton("Black")

        color = radioBtnState(self.white)

        self.topLabel = QLabel()
        self.topLabel.setText("Top Caption")
        self.topCap = QLineEdit()
        self.btmLabel = QLabel()
        self.btmLabel.setText("Bottom Caption")
        self.btmCap = QLineEdit()

		#Font button
        self.my_button = QPushButton(f"Font")
        self.my_button.clicked.connect(self.on_click)

        self.textButton = QPushButton("Submit")
        self.textButton.setCheckable(True)
        self.textButton.clicked.connect(self.btnstate)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v2_layout = QVBoxLayout()
        v2_layout.addWidget(self.textLabel)
        v2_layout.addWidget(self.white)
        v2_layout.addWidget(self.black)
        v_layout.addWidget(self.topLabel)
        v_layout.addWidget(self.topCap)
        v_layout.addWidget(self.btmLabel)
        v_layout.addWidget(self.btmCap)
        v_layout.addWidget(self.my_button)
        v_layout.addWidget(self.textButton)
        h_layout.addLayout(v2_layout)
        h_layout.addLayout(v_layout)
        self.setLayout(h_layout)

    @pyqtSlot()
    def on_click(self):
        global Font
        Font = fontTemplate.openFontDialog(self)


    def btnstate(self):
        if self.textButton.isChecked():
            print("hi")
            print(Font)
			#just add Font as the last parameter for user font
            addText(self,self.meme,self.white,self.black,self.topCap,self.btmCap,Font)

def addText(self,meme,white,black,topCap,btmCap,imgFont):

    text1 = topCap.text()
    text2 = btmCap.text()


    #Makes the text Upper Case
    text1 = text1.upper()
    text2 = text2.upper()



    # Centers text
    imageSize = meme.size
    fontSize = int(imageSize[1]/5)
    font = imgFont # This is the font the user chose
    topTextSize = font.pointSize()
    bottomTextSize = font.pointSize()
    # Resizes text, if size of text is bigger than image
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize = fontSize - 1
        font = ImageFont.truetype(imgFont, fontSize)
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
	if btn.text() == "White":
		if btn.isChecked == True:
			return 255
	if btn.text() == "Black":
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



def chcBtnState(btn):
	if btn.text() == "Yes":
		if btn.isChecked == True:
			return "Yes"
	if btn.text() == "No":
		if btn.isChecked == True:
			return "No"
	if btn.text() == "Change Text":
		if btn.isChecked == True:
			return "Change Text"

choices =['Ancient Aliens', 'Awkward Moment Seal', 'Bad Luck Brian', 'Brace Yourself', 'But That\'s None of My Business',
'Condescending Wonka', 'Desk Flip', 'Doge', 'Futurama Fry', 'Grumpy Cat', 'Matrix Morpheus', 'One Does Not Simply',
'Philosoraptor', 'Really High Guy', 'Scumbag Steve', 'Success Kid', 'Third World Skeptical Kid', 'Too Damn High',
'Y U No', 'Yo Dawg', 'Create Your Own Meme']

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
            choice = self.my_combo_box.currentText()
            direct = "Memes/" + choice + ".jpg"
            meme = Image.open(direct)
            meme.save("copy.jpg") #Saves for further use
            meme = Image.open("copy.jpg") #Allows the new meme to be used
            self.update_ui(meme)

    def update_ui(self,meme):
        self.new_win = TextWindow(meme)
        self.new_win.show()


"""
Setups app and starts event loop
"""
app = QApplication(sys.argv)
main = Window()
main.setWindowTitle("Meme Generator")
main.show()
sys.exit(app.exec_())
