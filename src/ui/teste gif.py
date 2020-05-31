# def clickable(self, toolbox):
#     class Filter(QObject):
#         clicked = pyqtSignal()
#
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