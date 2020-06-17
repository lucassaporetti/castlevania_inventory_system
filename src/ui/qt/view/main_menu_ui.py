from PyQt5 import uic
from PyQt5.QtWidgets import *
from src.ui.qt.view.qt_view import QtView
from ui.qt.view.item_edit_ui import ItemEditUi
from src.ui.qt.view.item_add_ui import ItemAddUi
from src.ui.qt.view.item_information_ui import ItemInformationUi
from resources.resources_properties.image_paths import ImagePaths


class MainMenuUi(QtView):
    form, window = uic.loadUiType("ui/qt/form/castlevania_inventory.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.itemInformationUi = ItemInformationUi(self)
        self.ImagePaths = ImagePaths(self)
        self.itemAddUi = ItemAddUi(self)
        self.ItemEditUi = ItemEditUi(self)
        self.frameMain = self.qt.find_frame('frameMain')
        self.frameToolbox = self.qt.find_frame('frameToolbox')
        self.addButton = self.qt.find_tool_button('addButton')
        self.searchButton = self.qt.find_tool_button('searchButton')
        self.searchLine = self.qt.find_line_edit('searchLine')
        self.stackedMain = self.qt.find_stacked_widget('stackedMain')
        self.mainPage = self.qt.find_widget(self.window, QWidget, 'mainPage')
        self.setup_ui()

    def setup_ui(self):
        self.itemInformationUi.categoryBox.setCurrentIndex(8)
        self.stackedMain.setCurrentIndex(0)
        self.searchButton.clicked.connect(self.search_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)

    def show(self):
        self.window.show()

    def search_button_clicked(self):
        pass

    def add_button_clicked(self):
        self.itemInformationUi.categoryBox.setCurrentIndex(8)
        self.stackedMain.setCurrentIndex(2)
        self.ImagePaths.get_image(9)
