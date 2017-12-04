from PIL import Image, ImageDraw, ImageFont, ImageOps
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QFileDialog, QCheckBox,
							QVBoxLayout, QComboBox, QPushButton, QRadioButton, QGroupBox, QFontDialog, QGridLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from PIL import Image, ImageFilter, ImageOps
from filters import * # Filter functions located in filters.py
from fontTemplate import *
from addtext import addText
import os, sys

# meme choices dropdown list
choices =['Choose a meme template:', 'Ancient Aliens', 'Awkward Moment Seal', 'Bad Luck Brian', 'Brace Yourself',
'But That\'s None of My Business', 'Condescending Wonka', 'Desk Flip', 'Doge', 'Futurama Fry', 'Grumpy Cat',
'Matrix Morpheus', 'One Does Not Simply', 'Philosoraptor', 'Really High Guy', 'Scumbag Steve', 'Success Kid',
'Third World Skeptical Kid', 'Too Damn High', 'Y U No', 'Yo Dawg']

welcomeText = """<h1>Meme Generator</h1>
<p><i>“Divided by distance, united by memes.”</i></p>
<p>To get started, select a meme template or provide your own.</p>"""

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(500, 250)
		self.setWindowTitle("Meme Generator")
		mainQVBox = QVBoxLayout()

		self.createTitleBox()
		self.createMemeBox()

		mainQVBox.addWidget(self.QGroupTitle)
		mainQVBox.addWidget(self.QGroupOptions)
		self.setLayout(mainQVBox)

	""" Title Group containing application title, quote, and instructions. """
	def createTitleBox(self):
		self.QGroupTitle = QGroupBox()
		vBox = QVBoxLayout()
		welcomeLabel = QLabel()
		welcomeLabel.setAlignment(Qt.AlignCenter)
		welcomeLabel.setText(welcomeText)

		vBox.addWidget(welcomeLabel)
		self.QGroupTitle.setLayout(vBox)

	""" Meme Group for selecting and loading a template """
	def createMemeBox(self):
		self.QGroupOptions = QGroupBox()
		hBox = QHBoxLayout()

		self.browseButton = QPushButton("Browse")
		self.browseButton.setMaximumWidth(100)

		self.memeoptions = QComboBox()
		self.memeoptions.addItems(choices)
		self.memeoptions.setMinimumWidth(200)
		self.memeoptions.setMaximumWidth(300)

		self.startButton = QPushButton("Start")
		self.startButton.setMaximumWidth(100)

		hBox.addWidget(self.browseButton)
		hBox.addWidget(self.memeoptions)
		hBox.addWidget(self.startButton)
		self.QGroupOptions.setLayout(hBox)

		self.browseButton.clicked.connect(self.openBrowser)
		self.startButton.clicked.connect(self.openFile)

	""" Opens an image from the native file browser """
	def openBrowser(self):
		fileName, ignore = QFileDialog.getOpenFileName(self,"Choose an Image", "","JPEG (*.jpg)")
		if fileName: # if an image was provided, open it
			meme = Image.open(fileName) # opens image from directory
			meme.save("copy.jpg")
			self.meme = Image.open("copy.jpg")
			self.customize = Customizer()
			self.customize.show()

	""" Opens an image from the meme dropdown list """
	def openFile(self):
		choice = self.memeoptions.currentText()
		if choice != choices[0]: # continue only if a template is selected
			direct = "Memes/" + choice + ".jpg"
			meme = Image.open(direct) # opens image from directory
			meme.save("copy.jpg")
			meme = Image.open("copy.jpg")
			self.customize = Customizer(meme)
			self.customize.show()

class Customizer(QWidget):
	def __init__(self, meme):
		super().__init__()
		self.setFixedSize(600,400)
		self.setWindowTitle("Customizer")
		self.meme = meme
		mainQVBox = QVBoxLayout()

		self.fontOptions()
		self.textEdit()
		self.filterEdit()

		self.savebtn = QPushButton("Save...")
		self.savebtn.clicked.connect(self.saveImage)

		mainQVBox.addWidget(self.QGroupFont)
		mainQVBox.addWidget(self.QGroupText)
		mainQVBox.addWidget(self.QGroupFilter)
		mainQVBox.addWidget(self.savebtn)
		self.setLayout(mainQVBox)

	""" Show options for font, size, and color """
	def fontOptions(self):
		self.QGroupFont = QGroupBox("Font Options")
		hBox = QHBoxLayout()
		gLayout = QGridLayout()
		self.fontCombo = QComboBox()
		self.fontCombo.addItems(fonts)
		self.fontCombo.setMaximumWidth(200)


		self.fontColorLabel = QLabel("Font Color:")
		self.fontColorLabel.setAlignment(Qt.AlignCenter)

		self.colorButton = QRadioButton("White")
		self.colorButton.setChecked(True)
		gLayout.addWidget(self.colorButton, 0, 0)

		self.colorButton2 = QRadioButton("Black")
		gLayout.addWidget(self.colorButton2, 0, 1)

		hBox.addWidget(self.fontCombo)
		hBox.addWidget(self.fontColorLabel)
		hBox.addLayout(gLayout)
		self.QGroupFont.setLayout(hBox)

	""" Allows meme caption editing """
	def textEdit(self):
		self.QGroupText = QGroupBox("Caption Editor")
		vBox = QVBoxLayout()

		self.topCap = QLineEdit()
		self.topCap.setPlaceholderText("Top Caption")
		self.topCap.setMaximumWidth(400)

		self.bottomCap = QLineEdit()
		self.bottomCap.setPlaceholderText("Bottom Caption")
		self.bottomCap.setMaximumWidth(400)

		vBox.addWidget(self.topCap)
		vBox.addWidget(self.bottomCap)
		vBox.setAlignment(Qt.AlignCenter)
		self.QGroupText.setLayout(vBox)

	""" Allows users to add filters with dropdown menu """
	def filterEdit(self):

		self.QGroupFilter = QGroupBox("Filters")
		vBox = QVBoxLayout()
		hBox = QHBoxLayout()

		self.optionBox = QComboBox()
		self.optionBox.addItems(filterlist)
		self.optionBox.setMaximumWidth(300)
		self.applybtn = QPushButton("Apply",self)
		self.applybtn.setMaximumWidth(100)
		hBox.addWidget(self.optionBox)
		hBox.addWidget(self.applybtn)

		vBox.addLayout(hBox)
		self.QGroupFilter.setLayout(vBox)

		self.applybtn.clicked.connect(self.onClick)
	@pyqtSlot()
	def onClick(self):
		aFilter = self.optionBox.currentText()
		meme = Image.open("copy.jpg")
		if aFilter == "Choose a filter: ":
			return
		if aFilter == "Deep Frier":
			deepfrier(meme)
		if aFilter == "Grayscale":
			grayscale(meme)
		if aFilter == "Inverted":
			invertColor(meme)
		if aFilter == "Emoji":
			# emoji(meme) #This needs more info
			print("still In progress")

	def radioBtnState(self,radiobutton,radiobutton2):
		#radiobutton = self.sender()
		if radiobutton.isChecked() == True:
			print("WHITE")
			return ((255,255,255))
		if radiobutton2.isChecked() == True:
			print("BLACK")
			return ((0,0,0))

	def saveImage(self):
		global color
		color = self.radioBtnState(self.colorButton,self.colorButton2)
		print("COLOR:", color)

		if self.fontCombo.currentText() != fonts[0]:
			FontChoice = getFont(self.fontCombo.currentText())
			self.final = addText(self.topCap,self.bottomCap,FontChoice,color)

		fileName, ignore = QFileDialog.getSaveFileName(self,"Save Meme")
		if ".jpg" not in fileName:
			fileName += ".jpg"
		self.final.save(fileName) # saves image to selected directory and adds extension

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
