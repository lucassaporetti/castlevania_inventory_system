from PyQt5 import uic
from PyQt5.QtWidgets import QTabWidget, QLabel, QFrame, QToolBox, QWidget, QStackedWidget, QTextEdit, QLineEdit

# from src.core.config.app_configs import AppConfigs
# from core.enum.color import Color
# from core.model.entity import Entity
# from src.ui.qt.views.car.car_edit_view import CarEditView
# from src.ui.qt.views.car.car_search_view import CarSearchView
# from src.ui.qt.views.rental.rental_edit_view import RentalEditView
# from src.ui.qt.views.rental.rental_search_view import RentalSearchView
# from src.ui.qt.views.user.user_edit_view import UserEditView
# from src.ui.qt.views.user.user_search_view import UserSearchView
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
        self.stackedMain = self.qt.find_stacked_widget('stackedMain')
        self.stackedPage = self.qt.find_widget(self.window, QWidget, 'stackedPage')
        self.itemDescription = self.qt.find_text_edit('itemDescription')
        self.itemAttributes = self.qt.find_text_edit('itemAttributes')
        self.itemImage = self.qt.find_text_edit('itemImage')
        self.frameToolbox = self.qt.find_frame('frameToolbox')
        self.addButton = self.qt.find_tool_button('addButton')
        self.removeButton = self.qt.find_tool_button('removeButton')
        self.searchButton = self.qt.find_tool_button('searchButton')
        self.searchLine = self.qt.find_line_edit('searchLine')
        # self.tabPanel = self.qt.find_widget(self.window, QTabWidget, 'tabPanel')
        # self.labelStatusBar = self.qt.find_widget(self.window, QLabel, 'labelStatusBar')
        # self.car_search = CarSearchView(self.window, self)
        # self.car_edit = CarEditView(self.window, self)
        # self.user_search = UserSearchView(self.window, self)
        # self.user_edit = UserEditView(self.window, self)
        # self.rental_search = RentalSearchView(self.window, self)
        # self.rental_edit = RentalEditView(self.window, self)
        self.setup_ui()
        # self.set_status('Ready.')

    def setup_ui(self):
        # self.frameMain.setCurrentIndex(0)
        # self.frameMain.connect()
        pass

    def show(self):
        self.window.show()

    def tab_changed(self, idx: int):
        # self.car_search.stackedPanelCars.setCurrentIndex(0)
        # self.user_search.stackedPanelUsers.setCurrentIndex(0)
        # self.rental_search.stackedPanelRentals.setCurrentIndex(0)
        self.log.info('Tab: tabPanel changed to {}'.format(idx))

    # def set_status(self, message):
    #     text = '<font color="{}">{}</font>'.format(str('color.name').lower(), message)
    #     self.labelStatusBar.setText(text)
