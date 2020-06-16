import os
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from src.ui.qt.view.qt_view import QtView
from src.ui.qt.view.item_add_ui import ItemAddUi
from src.ui.qt.view.item_information_ui import ItemInformationUi
from src.resources.resources_properties.image_paths import ImagePaths


class MainMenuUi(QtView):
    form, window = uic.loadUiType("ui/qt/form/castlevania_inventory.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.itemInformationUi = ItemInformationUi(self)
        self.itemAddUi = ItemAddUi(self)
        self.frameMain = self.qt.find_frame('frameMain')
        self.frameToolbox = self.qt.find_frame('frameToolbox')
        self.addButton = self.qt.find_tool_button('addButton')
        self.searchButton = self.qt.find_tool_button('searchButton')
        self.searchLine = self.qt.find_line_edit('searchLine')
        self.stackedMain = self.qt.find_stacked_widget('stackedMain')
        self.mainPage = self.qt.find_widget(self.window, QWidget, 'mainPage')
        self.logoImage = self.qt.find_label('logoImage')
        self.show_logo_image()
        self.setup_ui()

    def setup_ui(self):
        self.itemInformationUi.categoryBox.setCurrentIndex(8)
        self.stackedMain.setCurrentIndex(0)
        self.searchButton.clicked.connect(self.search_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)

    def show(self):
        self.window.show()

    def key_pressed(self, key_pressed):
        pass

    def search_button_clicked(self):
        pass

    def add_button_clicked(self):
        self.itemInformationUi.categoryBox.setCurrentIndex(8)
        self.stackedMain.setCurrentIndex(2)

    def show_logo_image(self):
        logo_image = ImagePaths(7).get_image()
        q_image = QtGui.QImage(logo_image)
        q_pixmap = QtGui.QPixmap.fromImage(q_image)
        q_pixmap_image = QtGui.QPixmap(q_pixmap)
        q_pixmap_image_sized = q_pixmap_image.scaled(307, 164)
        self.logoImage.setPixmap(q_pixmap_image_sized)
        self.logoImage.show()

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
