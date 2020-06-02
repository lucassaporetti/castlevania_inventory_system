from abc import ABC
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from src.resources.resources_properties.image_paths import ImagePaths
from src.ui.qt.view.qt_view import QtView


class ItemInformationUI(QtView, ABC):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.characterImage = self.qt.find_label('characterImage')
        self.categoryBox = self.qt.find_tool_box('categoryBox')
        self.armorPage = self.qt.find_widget(self.window, QWidget, 'armorPage')
        self.weaponPage = self.qt.find_widget(self.window, QWidget, 'weaponPage')
        self.shieldPage = self.qt.find_widget(self.window, QWidget, 'shieldPage')
        self.relicPage = self.qt.find_widget(self.window, QWidget, 'relicPage')
        self.cardPage = self.qt.find_widget(self.window, QWidget, 'cardPage')
        self.consumablePage = self.qt.find_widget(self.window, QWidget, 'consumablePage')
        self.otherPage = self.qt.find_widget(self.window, QWidget, 'otherPage')
        self.logoPage = self.qt.find_widget(self.window, QWidget, 'logoPage')
        self.informationPage = self.qt.find_widget(self.window, QWidget, 'informationPage')
        self.itemDescription = self.qt.find_text_edit('itemDescription')
        self.itemFrame = self.qt.find_frame('itemFrame')
        self.itemGifAnimation = self.qt.find_label('itemGifAnimation')
        self.itemGifSpecial = self.qt.find_label('itemGifSpecial')
        self.itemImage = self.qt.find_label('itemImage')
        self.itemName = self.qt.find_label('itemName')
        self.animated_item_gif()
        self.show_item_image()
        self.editButton = self.qt.find_tool_button('editButton')
        self.removeButton = self.qt.find_tool_button('removeButton')
        self.setup_ui()

    def setup_ui(self):
        self.categoryBox.setCurrentIndex(7)
        self.categoryBox.currentChanged.connect(self.category_box_clicked)

    def animated_item_gif(self):
        movie = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
                             "castlevania_inventory_system/src/resources/"
                             "images/items/alucard_sword_animation.gif")
        self.itemGifAnimation.setMovie(movie)
        movie.start()
        movie2 = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
                              "castlevania_inventory_system/src/resources/"
                              "images/items/alucard_sword_special.gif")
        self.itemGifSpecial.setMovie(movie2)
        movie2.start()

    def show_item_image(self):
        item_image = '/home/lucassaporetti/GIT-Repository/' \
                     'castlevania_inventory_system/src/' \
                     'resources/images/items/alucard_sword_icon.png'
        qimage = QtGui.QImage(item_image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        pixmap_image = QtGui.QPixmap(pixmap)
        self.itemImage.setPixmap(pixmap_image)
        self.itemImage.show()

    def category_box_clicked(self):
        index = self.categoryBox.currentIndex()
        image_index = ImagePaths(index).get_image()
        self.log.info(f'{str(self.categoryBox.widget(index))} selected!')
        character_image = image_index
        q_image = QtGui.QImage(character_image)
        q_pixmap = QtGui.QPixmap.fromImage(q_image)
        q_pixmap_image = QtGui.QPixmap(q_pixmap)
        q_pixmap_image_sized = q_pixmap_image.scaled(270, 383)
        self.characterImage.setPixmap(q_pixmap_image_sized)
        self.characterImage.show()
        self.parent.stackedMain.setCurrentIndex(1)
        if index == 7:
            self.characterImage.close()
            self.parent.stackedMain.setCurrentIndex(0)

    def remove_button_clicked(self):
        pass
