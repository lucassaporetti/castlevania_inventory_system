from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

STYLESHEET = """
background-color: rgb(0, 0, 0);
font: 12pt 'URW Bookman L';
color: rgb(238, 238, 236);
gridline-color: rgb(46, 52, 54);
selection-color: rgb(0, 0, 0);
selection-background-color: rgb(181, 0, 0);
"""


class CvConfirmBox(QMessageBox):

    yesClicked = pyqtSignal()
    noClicked = pyqtSignal()

    def __init__(self, parent, title: str, message: str):
        super().__init__(parent=parent)
        self.title = title
        self.message = message
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet(STYLESHEET)
        self.setWindowModality(Qt.WindowModal)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setWindowTitle(self.title)
        self.setText(self.message)

    def exec(self) -> int:
        ret = super().exec_()
        if ret == QMessageBox.Yes:
            self.yesClicked.emit()
        else:
            self.noClicked.emit()

        return ret
