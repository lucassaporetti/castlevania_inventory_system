import base64
import io
import numpy as np
import cv2
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *
from core.service.service_facade import ServiceFacade
from src.resources.resources_properties.image_paths import ImagePaths
from src.ui.qt.view.qt_view import QtView
from ui.promotions.cv_confirm_box import CvConfirmBox
import imageio


class ItemInformationUi(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.item_service = ServiceFacade.get_item_service()
        self.characterImage = self.qt.find_label('characterImage')
        self.categoryBox = self.qt.find_tool_box('categoryBox')
        self.weaponPage = self.qt.find_widget(self.window, QWidget, 'weaponPage')
        self.weaponList = self.qt.find_list_widget('weaponList')
        self.shieldPage = self.qt.find_widget(self.window, QWidget, 'shieldPage')
        self.shieldList = self.qt.find_list_widget('shieldList')
        self.armorPage = self.qt.find_widget(self.window, QWidget, 'armorPage')
        self.armorList = self.qt.find_list_widget('armorList')
        self.relicPage = self.qt.find_widget(self.window, QWidget, 'relicPage')
        self.relicList = self.qt.find_list_widget('relicList')
        self.spellPage = self.qt.find_widget(self.window, QWidget, 'spellPage')
        self.spellList = self.qt.find_list_widget('spellList')
        self.otherPage = self.qt.find_widget(self.window, QWidget, 'otherPage')
        self.otherList = self.qt.find_list_widget('otherList')
        self.consumablePage = self.qt.find_widget(self.window, QWidget, 'consumablePage')
        self.consumableList = self.qt.find_list_widget('consumableList')
        self.standardPage = self.qt.find_widget(self.window, QWidget, 'standardPage')
        self.standardList = self.qt.find_list_widget('standardList')
        self.logoPage = self.qt.find_widget(self.window, QWidget, 'logoPage')
        self.informationPage = self.qt.find_widget(self.window, QWidget, 'informationPage')
        self.infoCategory = self.qt.find_label('infoCategory')
        self.infoType = self.qt.find_label('infoType')
        self.infoDescription = self.qt.find_text_edit('infoDescription')
        self.infoAttributes = self.qt.find_label('infoAttributes')
        self.infoConsumeMp = self.qt.find_label('infoConsumeMp')
        self.infoConsumeHt = self.qt.find_label('infoConsumeHt')
        self.infoStatHp = self.qt.find_label('infoStatHp')
        self.infoStatMp = self.qt.find_label('infoStatMp')
        self.infoStatHt = self.qt.find_label('infoStatHt')
        self.infoStatStr = self.qt.find_label('infoStatStr')
        self.infoStatAtt = self.qt.find_label('infoStatAtt')
        self.infoStatInt = self.qt.find_label('infoStatInt')
        self.infoStatCon = self.qt.find_label('infoStatCon')
        self.infoStatMaxHt = self.qt.find_label('infoStatMaxHt')
        self.infoStatMaxHp = self.qt.find_label('infoStatMaxHp')
        self.infoStatDef = self.qt.find_label('infoStatDef')
        self.infoStatLck = self.qt.find_label('infoStatLck')
        self.infoStatGold = self.qt.find_label('infoStatGold')
        self.infoSell = self.qt.find_label('infoSell')
        self.infoFound = self.qt.find_label('infoFound')
        self.infoDropped = self.qt.find_label('infoDropped')
        self.infoEffect = self.qt.find_text_edit('infoEffect')
        self.infoItemName = self.qt.find_label('infoItemName')
        self.infoItemImage = self.qt.find_label('infoItemImage')
        self.infoItemAnimation = self.qt.find_label('infoItemAnimation')
        self.infoItemSpecial = self.qt.find_label('infoItemSpecial')
        self.editButton = self.qt.find_tool_button('editButton')
        self.removeButton = self.qt.find_tool_button('removeButton')
        self.addButton = self.qt.find_tool_button('addButton')
        self.animated_item_gif()
        self.show_item_image()
        self.setup_ui()

    def setup_ui(self):
        self.categoryBox.setCurrentIndex(8)
        self.categoryBox.currentChanged.connect(self.category_box_clicked)
        self.removeButton.clicked.connect(self.remove_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)

    def category_box_clicked(self):
        self.load_to_list(self.weaponList, 'Weapon')
        self.load_to_list(self.shieldList, 'Shield')
        self.load_to_list(self.armorList, 'Armor')
        self.load_to_list(self.relicList, 'Relic')
        self.load_to_list(self.spellList, 'Spell')
        self.load_to_list(self.otherList, 'Other')
        self.load_to_list(self.consumableList, 'Consumable')
        self.load_to_list(self.standardList, 'Standard')
        index = self.categoryBox.currentIndex()
        image_index = ImagePaths(index).get_image()
        self.log.info(f'{str(self.categoryBox.widget(index))} selected!')
        character_image = image_index
        q_image = QtGui.QImage(character_image)
        q_pixmap = QtGui.QPixmap.fromImage(q_image)
        q_pixmap_image = QtGui.QPixmap(q_pixmap)
        q_pixmap_image_sized = q_pixmap_image.scaled(370, 517)
        self.characterImage.setPixmap(q_pixmap_image_sized)
        self.characterImage.show()
        self.parent.stackedMain.setCurrentIndex(1)
        if index == 8:
            self.characterImage.close()
            self.parent.stackedMain.setCurrentIndex(0)

    def show_item_image(self):
        item_image = '/home/lucassaporetti/GIT-Repository/' \
                     'castlevania_inventory_system/src/' \
                     'resources/images/items/alucard_sword_icon.png'
        qimage = QtGui.QImage(item_image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        pixmap_image = QtGui.QPixmap(pixmap)
        self.infoItemImage.setPixmap(pixmap_image)
        self.infoItemImage.show()

    def animated_item_gif(self):
        movie = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
                             "castlevania_inventory_system/src/resources/"
                             "images/items/alucard_sword.gif")
        self.infoItemAnimation.setMovie(movie)
        movie.start()
        movie2 = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
                              "castlevania_inventory_system/src/resources/"
                              "images/items/alucard_sword_special.gif")
        self.infoItemSpecial.setMovie(movie2)
        movie2.start()

    def edit_button_clicked(self):
        pass

    def add_button_clicked(self):
        pass

    def remove_button_clicked(self):
        remove_image = ImagePaths(8).get_image()
        q_image = QtGui.QImage(remove_image)
        q_pixmap = QtGui.QPixmap.fromImage(q_image)
        q_pixmap_image = QtGui.QPixmap(q_pixmap)
        q_pixmap_image_sized = q_pixmap_image.scaled(370, 517)
        self.characterImage.setPixmap(q_pixmap_image_sized)
        self.characterImage.show()
        message_box = CvConfirmBox(self.window, 'Warning!', 'Remove this item from inventory?')
        message_box.yesClicked.connect(self.yes_clicked)
        message_box.noClicked.connect(self.no_clicked)
        message_box.exec()

    def yes_clicked(self):
        self.parent.stackedMain.setCurrentIndex(0)

    def no_clicked(self):
        self.category_box_clicked()

    def load_to_list(self, widget_list, item_category: str):
        widget_list.clear()
        for item in self.item_service.list():
            while item_category in item.category:
                widget_list.setViewMode(QListView.IconMode)
                list_item = QListWidgetItem()
                item_icon = QtGui.QIcon()
                item_image_right = item.image.replace('b"b', '').replace("'", '').replace('"', '')
                item_image = self.str_to_rgb(item_image_right)
                height, width, channel = item_image.shape
                bytes_per_line = 3 * width
                q_img = QImage(item_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                item_icon.addPixmap(QtGui.QPixmap(q_img),
                                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
                list_item.setIcon(item_icon)
                list_item.setText(item.name.replace(' ', '\n'))
                widget_list.addItem(list_item)
                break

    @staticmethod
    def str_to_rgb(base64_str):
        image_data = base64.b64decode(base64_str)
        image = imageio.imread(io.BytesIO(image_data))
        return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
