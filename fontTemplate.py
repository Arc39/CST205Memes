import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    @pyqtSlot()
    def on_click(self):
        openFontDialog(self)


def openFontDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        print(font.toString())
