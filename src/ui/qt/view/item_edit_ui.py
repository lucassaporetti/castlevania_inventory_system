# from PyQt5 import QtGui
# from PyQt5.QtWidgets import *
# from src.resources.resources_properties.image_paths import ImagePaths
# from src.ui.qt.view.qt_view import QtView
# from ui.promotions.cv_confirm_box import CvConfirmBox
#
#
# class ItemEditUI(QtView):
#     def __init__(self, parent: QtView):
#         super().__init__(parent.window, parent)
#         self.EditPage = self.qt.find_widget(self.window, QWidget, 'EditPage')
#         self.EditDescriptionEdit = self.qt.find_text_edit('addDescriptionEdit')
#         self.addSpecialAttEdit = self.qt.find_text_edit('addSpecialAttEdit')
#         self.addCategoryBox = self.qt.find_combo_box('addCategoryBox')
#         self.addDroppedBox = self.qt.find_combo_box('addDroppedBox')
#         self.addFoundBox = self.qt.find_combo_box('addFoundBox')
#         self.addSpecialityBox = self.qt.find_combo_box('addSpecialityBox')
#         self.addTypeBox = self.qt.find_combo_box('addTypeBox')
#         self.addGifAnimation = self.qt.find_label('addGifAnimation')
#         self.addGifSpecial = self.qt.find_label('addGifSpecial')
#         self.addItemImage = self.qt.find_label('addItemImage')
#         self.addNameEdit = self.qt.find_line_edit('addNameEdit')
#         self.cancelButton = self.qt.find_push_button('cancelButton')
#         self.resetButton = self.qt.find_push_button('resetButton')
#         self.saveButton = self.qt.find_push_button('saveButton')
#         # self.animated_item_gif()
#         # self.show_item_image()
#         self.setup_ui()
#
#     def setup_ui(self):
#         pass

    # def show_item_image(self):
    #     item_image = '/home/lucassaporetti/GIT-Repository/' \
    #                  'castlevania_inventory_system/src/' \
    #                  'resources/images/items/alucard_sword_icon.png'
    #     qimage = QtGui.QImage(item_image)
    #     pixmap = QtGui.QPixmap.fromImage(qimage)
    #     pixmap_image = QtGui.QPixmap(pixmap)
    #     self.itemImage.setPixmap(pixmap_image)
    #     self.itemImage.show()

    # def animated_item_gif(self):
    #     movie = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
    #                          "castlevania_inventory_system/src/resources/"
    #                          "images/items/alucard_sword_animation.gif")
    #     self.itemGifAnimation.setMovie(movie)
    #     movie.start()
    #     movie2 = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
    #                           "castlevania_inventory_system/src/resources/"
    #                           "images/items/alucard_sword_special.gif")
    #     self.itemGifSpecial.setMovie(movie2)
    #     movie2.start()
