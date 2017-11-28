# required imports
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import sys

# allows user to choose and open a file
def openImage(self):
    fileName, ignore = QFileDialog.getOpenFileName(self,"Choose an Image", "","JPEG (*.jpg)")
    self.image = Image.open(fileName) # opens image from directory

# allows user to choose a directory to save their file
def saveImage(self):
    fileName, ignore = QFileDialog.getSaveFileName(self,"Save Meme")
    self.image.save(fileName + ".jpg") # saves image to selected directory and adds extension
