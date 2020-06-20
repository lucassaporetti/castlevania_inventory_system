import base64
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

data = open("/home/lucassaporetti/GIT-Repository/castlevania_inventory_system/"
            "src/resources/images/items/alucard_shield.gif", 'rb').read()
print(data)

binary_data = base64.b64encode(data)

print(binary_data)

back_data = base64.b64decode(binary_data)

print(type(back_data))

a = QtCore.QByteArray(back_data)
b = QtCore.QBuffer(a)

print('open: %s' % b.open(QtCore.QIODevice.ReadOnly))

m = QtGui.QMovie()
m.setFormat(a)
m.setDevice(b)

print('valid: %s' % m.isValid())

w = QLabel()
w.setMovie(m)
m.start()

w.resize(200, 200)
w.show()
app.exec_()

print('pos: %s' % b.pos())

# import random
# import sys
# from PyQt5 import QtGui, QtCore, QtWidgets
#
#
# class ViewDelegate(QtWidgets.QStyledItemDelegate):
#     def __init__(self):
#         QtWidgets.QStyledItemDelegate.__init__(self)
#         self.padding = 2
#         self.AlignmentFlag = QtCore.Qt.AlignRight
#
#     def paint(self, painter, option, index):
#         x = option.rect.x()
#         y = option.rect.y()
#         width = option.rect.width()
#         height = option.rect.height()
#         icon_list = index.data(256)                      # get the icons associated with the item
#         text = index.data()                             # get the items text
#
#         for a, i in enumerate(icon_list):
#             m = max([i.width(), i.height()])
#             f = (height - 2*self.padding)                 # scalingfactor
#             i = i.scaled(int(i.width()*f), int(i.height()*f))                    # scale all pixmaps to the same size depending on lineheight
#             painter.drawPixmap(QtCore.QPoint(x, y+self.padding), i)
#             x += height
#
#         painter.drawText(QtCore.QRect(x + self.padding, y + self.padding,
#                                       width - x - 2*self.padding, height - 2*self.padding), self.AlignmentFlag, text)
#
#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         self.setGeometry(200, 100, 200, 220)
#         self.icons = []
#         i = '/home/lucassaporetti/GIT-Repository/castlevania_inventory_system/src/resources/images/items/alucard_sword_icon.png'
#         icon = QtGui.QImage(i)
#         icon2 = QtGui.QPixmap.fromImage(icon)
#         icon3 = QtGui.QPixmap(icon2)
#         self.icons.append(icon3)
#
#         self.listWidget = QtWidgets.QListView(self)
#         self.delegate = ViewDelegate()
#         self.listWidget.setGeometry(20, 20, 160, 180)
#         self.listWidget.setItemDelegate(self.delegate)
#         self.model = QtGui.QStandardItemModel(self.listWidget)
#
#     def icon_list(self):                             # creates a random iconList
#         r = random.randint(1, len(self.icons))                   # Anzahl icons in the list
#         icon_list = []
#         for i in range(0, r):
#             n = random.randint(0, len(self.icons)-1)
#             icon = self.icons[n]
#             icon_list.append(icon)
#         return icon_list
#
#
# app = QtWidgets.QApplication(sys.argv)
# widget = MyWidget()
# widget.show()
# sys.exit(app.exec_())


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from PyQt5 import QtGui, QtCore
# import sys
#
# from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QToolButton
#
#
# class Second(QMainWindow):
#     def __init__(self, parent=None):
#         super(Second, self).__init__(parent)
#         self.pushButton2 = QPushButton('Tchau')
#         self.setCentralWidget(self.pushButton2)
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.pushButton2.clicked.connect(self.on_push_button2_clicked)
#
#     def on_push_button2_clicked(self):
#         self.close()
#
#
# class First(QMainWindow):
#     def __init__(self, parent=None):
#         super(First, self).__init__(parent)
#         self.pushButton = QPushButton('Olá')
#         self.setCentralWidget(self.pushButton)
#         self.dialogs = list()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.pushButton.clicked.connect(self.on_push_button_clicked)
#
#     def on_push_button_clicked(self):
#         dialog = Second(self)
#         self.dialogs.append(dialog)
#         dialog.show()
#
#
# def main():
#     app = QApplication(sys.argv)
#     main = First()
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
#


# def clickable(self, toolbox):
#     class Filter(QObject):
#         clicked = pyqtSignal()
#         def eventFilter(self, obj, event):
#             if obj == toolbox:
#                 if event.type() == QEvent.MouseButtonPress:
#                     if obj.rect().contains(event.pos()):
#                         self.clicked.emit()
#                         return True
#             return False
#     filtered = Filter(toolbox)
#     toolbox.installEventFilter(filtered)
#     return filtered.clicked
