import os
from PyQt5 import uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QTabWidget, QLabel, QFrame, QToolBox, QStackedWidget, QTextEdit, QLineEdit

# from src.core.config.app_configs import AppConfigs
# from core.enum.color import Color
# from core.model.entity import Entity
# from src.ui.qt.views.car.car_edit_view import CarEditView
# from src.ui.qt.views.car.car_search_view import CarSearchView
# from src.ui.qt.views.rental.rental_edit_view import RentalEditView
# from src.ui.qt.views.rental.rental_search_view import RentalSearchView
# from src.ui.qt.views.user.user_edit_view import UserEditView
# from src.ui.qt.views.user.user_search_view import UserSearchView
from PyQt5.uic.properties import QtCore

from src.resources.resources_properties.image_paths import ImagePaths
from src.ui.qt.view.qt_view import QtView


class MainMenuUi(QtView):
    form, window = uic \
        .loadUiType("ui/qt/form/castlevania_inventory.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.frameMain = self.qt.find_frame('frameMain')
        self.categoryBox = self.qt.find_tool_box('categoryBox')
        self.armorPage = self.qt.find_widget(self.window, QWidget, 'armorPage')
        self.weaponPage = self.qt.find_widget(self.window, QWidget, 'weaponPage')
        self.shieldPage = self.qt.find_widget(self.window, QWidget, 'shieldPage')
        self.relicPage = self.qt.find_widget(self.window, QWidget, 'relicPage')
        self.cardPage = self.qt.find_widget(self.window, QWidget, 'cardPage')
        self.consumablePage = self.qt.find_widget(self.window, QWidget, 'consumablePage')
        self.otherPage = self.qt.find_widget(self.window, QWidget, 'otherPage')
        self.logoPage = self.qt.find_widget(self.window, QWidget, 'logoPage')
        self.stackedMain = self.qt.find_stacked_widget('stackedMain')
        self.mainPage = self.qt.find_widget(self.window, QWidget, 'mainPage')
        self.itemsPage = self.qt.find_widget(self.window, QWidget, 'itemsPage')
        self.itemDescription = self.qt.find_text_edit('itemDescription')
        self.itemAttributes = self.qt.find_text_edit('itemAttributes')
        self.logoImage = self.qt.find_label('logoImage')
        self.itemImage = self.qt.find_label('itemImage')
        self.characterImage = self.qt.find_label('characterImage')
        self.itemGifAnimation = self.qt.find_label('itemGifAnimation')
        self.itemGifSpecial = self.qt.find_label('itemGifSpecial')
        self.frameToolbox = self.qt.find_frame('frameToolbox')
        self.addButton = self.qt.find_tool_button('addButton')
        self.removeButton = self.qt.find_tool_button('removeButton')
        self.searchButton = self.qt.find_tool_button('searchButton')
        self.searchLine = self.qt.find_line_edit('searchLine')
        self.setup_ui()
        self.animated_item_gif()
        self.categoryBox.setCurrentIndex(7)
        self.stackedMain.setCurrentIndex(0)
        self.show_logo_image()
        self.show_item_image()

        # self.set_status('Ready.')

    def setup_ui(self):
        self.removeButton.clicked.connect(self.remove_button_clicked)
        self.categoryBox.currentChanged.connect(self.category_box_clicked)

    def key_pressed(self, key_pressed):
        if Qt.Key_1 == key_pressed:
            self.remove_button_clicked()

    def category_box_clicked(self):
        index = self.categoryBox.currentIndex()
        if index != 7:
            image_index = ImagePaths(index).get_image()
            self.log.info(f'{str(self.categoryBox.widget(index))} selected!')
            character_image = image_index
            qimage = QtGui.QImage(character_image)
            pixmap = QtGui.QPixmap.fromImage(qimage)
            pixmap_image = QtGui.QPixmap(pixmap)
            pixmap_image_sized = pixmap_image.scaled(270, 383)
            self.characterImage.setPixmap(pixmap_image_sized)
            self.characterImage.show()
            self.stackedMain.setCurrentWidget(self.itemsPage)
        else:
            self.stackedMain.setCurrentIndex(0)
            self.characterImage.close()

    @staticmethod
    def open_file():
        directory = os.path.expanduser("~/GIT-Repository/"
                                       "castlevania_inventory_system/"
                                       "src/resources/images/items")
        os.system("ls {0}".format(directory))
        file_name = QFileDialog.getOpenFileName(caption="Choose item image...",
                                                directory=directory, filter='*.png',
                                                options=QFileDialog.DontUseNativeDialog)
        return file_name

    def remove_button_clicked(self):
        self.log.info("Remove button pressed.")
        file_name = self.open_file()
        character_image = f'{file_name[0]}'
        qimage = QtGui.QImage(character_image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        pixmap_image = QtGui.QPixmap(pixmap)
        pixmap_image_sized = pixmap_image.scaled(270, 383)
        self.characterImage.setPixmap(pixmap_image_sized)
        self.characterImage.show()


    def show(self):
        self.window.show()

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

    def show_logo_image(self):
        logo_image = '/home/lucassaporetti/GIT-Repository/' \
                     'castlevania_inventory_system/src/' \
                     'resources/images/backgrounds/system_logo.png'
        qimage = QtGui.QImage(logo_image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        pixmap_image = QtGui.QPixmap(pixmap)
        self.logoImage.setPixmap(pixmap_image)
        self.logoImage.show()

    def tab_changed(self, idx: int):
        # self.car_search.stackedPanelCars.setCurrentIndex(0)
        # self.user_search.stackedPanelUsers.setCurrentIndex(0)
        # self.rental_search.stackedPanelRentals.setCurrentIndex(0)
        # self.log.info('Tab: tabPanel changed to {}'.format(idx))
        pass

    # def set_status(self, message):
    #     text = '<font color="{}">{}</font>'.format(str('color.name').lower(), message)
    #     self.labelStatusBar.setText(text)
