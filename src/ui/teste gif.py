from PyQt5 import QtWidgets, QtGui, QtCore

import sys

app = QtWidgets.QApplication(sys.argv)

item_image = '/home/lucassaporetti/GIT-Repository/castlevania_inventory_system/src/resources/images/items/alucard_sword_icon.png'
qImage = QtGui.QImage(item_image)
pixmap = QtGui.QPixmap.fromImage(qImage)
pixmap_image = QtGui.QPixmap(pixmap)
label_imageDisplay = QtWidgets.QLabel()
label_imageDisplay.setPixmap(pixmap_image)
# label_imageDisplay.setAlignment(QtCore.Qt.AlignCenter)
# label_imageDisplay.setScaledContents(True)
# label_imageDisplay.setMinimumSize(1,1)
label_imageDisplay.show()
sys.exit(app.exec_())
