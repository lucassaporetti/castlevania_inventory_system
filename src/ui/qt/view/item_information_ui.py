import io
import cv2
import numpy
import base64
import imageio
import functools
from PyQt5 import QtCore, QtGui
from src.ui.qt.view.qt_view import QtView
from PyQt5.QtGui import QImage, QPixmap, QIcon
from core.service.service_facade import ServiceFacade
from src.ui.promotions.cv_confirm_box import CvConfirmBox
from PyQt5.QtWidgets import QWidget, QListView, QListWidgetItem


class ItemInformationUi(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.item_service = ServiceFacade.get_item_service()
        self.selected_id = None
        self.selected_item = None
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
        self.infoHpLabel = self.qt.find_label('infoHpLabel')
        self.infoMpLabel = self.qt.find_label('infoMpLabel')
        self.infoHtLabel = self.qt.find_label('infoHtLabel')
        self.infoStrLabel = self.qt.find_label('infoStrLabel')
        self.infoAttLabel = self.qt.find_label('infoAttLabel')
        self.infoIntLabel = self.qt.find_label('infoIntLabel')
        self.infoConLabel = self.qt.find_label('infoConLabel')
        self.infoMaxHtLabel = self.qt.find_label('infoMaxHtLabel')
        self.infoMaxHpLabel = self.qt.find_label('infoMaxHpLabel')
        self.infoDefLabel = self.qt.find_label('infoDefLabel')
        self.infoLckLabel = self.qt.find_label('infoLckLabel')
        self.infoGoldLabel = self.qt.find_label('infoGoldLabel')
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
        self.categoryBox.setCurrentIndex(8)
        self.entities_id_list = []
        self.update_lists()
        self.setup_ui()

    def setup_ui(self):
        self.categoryBox.currentChanged.connect(self.category_box_clicked)
        self.removeButton.clicked.connect(self.remove_button_clicked)
        self.editButton.clicked.connect(self.edit_button_clicked)
        self.weaponList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.weaponList)
        self.shieldList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.shieldList)
        self.armorList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.armorList)
        self.relicList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.relicList)
        self.spellList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.spellList)
        self.otherList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.otherList)
        self.consumableList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.consumableList)
        self.standardList.mouseReleaseEvent = functools.partial(self.icon_click, source_object=self.standardList)

    def category_box_clicked(self):
        index = self.categoryBox.currentIndex()
        self.parent.ImagePaths.get_image(index)
        self.log.info(f'{str(self.categoryBox.widget(index))} selected!')
        if self.categoryBox.currentWidget() == self.weaponPage:
            self.first_icon_view(self.weaponList)
        elif self.categoryBox.currentWidget() == self.shieldPage:
            self.first_icon_view(self.shieldList)
        elif self.categoryBox.currentWidget() == self.armorPage:
            self.first_icon_view(self.armorList)
        elif self.categoryBox.currentWidget() == self.relicPage:
            self.first_icon_view(self.relicList)
        elif self.categoryBox.currentWidget() == self.spellPage:
            self.first_icon_view(self.spellList)
        elif self.categoryBox.currentWidget() == self.otherPage:
            self.first_icon_view(self.otherList)
        elif self.categoryBox.currentWidget() == self.consumablePage:
            self.first_icon_view(self.consumableList)
        elif self.categoryBox.currentWidget() == self.standardPage:
            self.first_icon_view(self.standardList)
        if index == 8:
            self.parent.stackedMain.setCurrentIndex(0)

    def edit_button_clicked(self):
        self.categoryBox.setCurrentIndex(8)
        self.parent.stackedMain.setCurrentIndex(3)
        self.parent.ItemEditUi.item_selected(self.selected_id)

    def remove_button_clicked(self):
        self.parent.ImagePaths.get_image(10)
        message_box = CvConfirmBox(self.window, 'Warning!', 'Remove this item from inventory?')
        message_box.yesClicked.connect(self.yes_clicked)
        message_box.noClicked.connect(self.no_clicked)
        message_box.exec()

    def yes_clicked(self):
        self.parent.stackedMain.setCurrentIndex(0)
        self.categoryBox.setCurrentIndex(8)
        self.item_service.remove(self.selected_item)
        self.log.info('Item removed: {}'.format(self.selected_item))
        self.entities_id_list.clear()
        self.update_lists()

    def no_clicked(self):
        self.category_box_clicked()

    def load_to_list(self, widget_list, item_category: str):
        widget_list.clear()
        for item in self.item_service.list():
            while item_category in item.category:
                widget_list.setViewMode(QListView.IconMode)
                list_item = QListWidgetItem()
                item_icon = QIcon()
                item_image_right = item.image.replace('b"b', '').replace("'", '').replace('"', '')
                item_image = self.str_to_rgb(item_image_right)
                height, width, channel = item_image.shape
                bytes_per_line = 3 * width
                q_img = QImage(item_image.data, width, height,
                               bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                item_icon.addPixmap(QPixmap(q_img),
                                    QIcon.Normal, QIcon.Off)
                list_item.setIcon(item_icon)
                list_item.setText(item.name.replace(' ', '\n'))
                list_item.setWhatsThis(item.entity_id)
                widget_list.addItem(list_item)
                self.entities_id_list.append(f'{list_item.whatsThis()}')
                break

    def load_item_image(self, item, label):
        item_image_right = item.image.replace('b"b', '').replace("'", '').replace('"', '')
        item_image = self.str_to_rgb(item_image_right)
        height, width, channel = item_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(item_image.data, width, height,
                         bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        q_pixmap = QPixmap.fromImage(q_image)
        q_pixmap_image = QPixmap(q_pixmap)
        label.setPixmap(q_pixmap_image)
        label.show()

    def load_item_gif(self, item, label):
        if label == self.infoItemAnimation:
            item_image_right = item.animation.replace('b"b', '').replace("'", '').replace('"', '')
        else:
            item_image_right = item.special_animation.replace('b"b', '').replace("'", '').replace('"', '')
        item_image = base64.b64decode(item_image_right)
        a = QtCore.QByteArray(item_image)
        b = QtCore.QBuffer(a)
        m = QtGui.QMovie()
        m.setFormat(a)
        m.setDevice(b)
        label.setMovie(m)
        m.start()
        m.stop()

    def update_lists(self):
        self.load_to_list(self.weaponList, 'Weapon')
        self.load_to_list(self.shieldList, 'Shield')
        self.load_to_list(self.armorList, 'Armor')
        self.load_to_list(self.relicList, 'Relic')
        self.load_to_list(self.spellList, 'Spell')
        self.load_to_list(self.otherList, 'Other')
        self.load_to_list(self.consumableList, 'Consumable')
        self.load_to_list(self.standardList, 'Standard')

    def icon_click(self, event, source_object):
        icon = source_object.currentItem()
        if icon is not None:
            for item in self.item_service.list():
                if icon.whatsThis() == item.entity_id:
                    self.selected_id = icon.whatsThis()
                    self.selected_item = item
                    return self.info_item(item)
        else:
            pass

    def first_icon_view(self, source_object):
        if source_object.count() > 0:
            source_object.item(0).setSelected(True)
            source_object.setFocus()
            icon = source_object.item(0).whatsThis()
            for item in self.item_service.list():
                if icon == item.entity_id:
                    self.selected_id = icon
                    self.selected_item = item
                    return self.info_item(item)
        else:
            self.parent.stackedMain.setCurrentIndex(0)

    def info_item(self, item):
        self.log.info(f'Item {item.name} selected for information')
        self.infoItemName.setText(item.name)
        self.infoCategory.setText(item.category)
        self.infoType.setText(item.item_type)
        self.infoDescription.setText(item.description)
        self.infoAttributes.setText(item.attributes)
        self.infoConsumeMp.setText(f'{item.consume_mp}')
        self.infoConsumeHt.setText(f'{item.consume_heart}')
        self.infoHpLabel.setText(f'HP: {item.statistics_hp}')
        self.infoMpLabel.setText(f'MP: {item.statistics_mp}')
        self.infoHtLabel.setText(f'Heart: {item.statistics_heart}')
        self.infoStrLabel.setText(f'STR: {item.statistics_str}')
        self.infoAttLabel.setText(f'ATT: {item.statistics_att}')
        self.infoIntLabel.setText(f'INT: {item.statistics_int}')
        self.infoConLabel.setText(f'CON: {item.statistics_con}')
        self.infoMaxHtLabel.setText(f'MaxHT: {item.statistics_max_ht}')
        self.infoMaxHpLabel.setText(f'MaxHP: {item.statistics_max_hp}')
        self.infoDefLabel.setText(f'DEF: {item.statistics_def}')
        self.infoLckLabel.setText(f'LCK: {item.statistics_lck}')
        self.infoGoldLabel.setText(f'Gold: {item.statistics_gold}')
        self.infoSell.setText(f'{item.sell}')
        self.infoFound.setText(item.found_at)
        self.infoDropped.setText(item.dropped_by)
        self.infoEffect.setText(item.effect)
        self.load_item_image(item, label=self.infoItemImage)
        self.load_item_gif(item, label=self.infoItemAnimation)
        self.load_item_gif(item, label=self.infoItemSpecial)
        self.parent.stackedMain.setCurrentIndex(1)

    @staticmethod
    def str_to_rgb(base64_str):
        image_data = base64.b64decode(base64_str)
        image = imageio.imread(io.BytesIO(image_data))
        return cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2RGB)

    @staticmethod
    def str_to_bgr(base64_str):
        image_data = base64.b64decode(base64_str)
        return image_data
