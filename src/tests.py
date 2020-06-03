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