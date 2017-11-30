from PyQt5.QtWidgets import QWidget, QFontDialog
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    @pyqtSlot()
    def on_click(self):
        openFontDialog(self)
        
def openFontDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        return font
