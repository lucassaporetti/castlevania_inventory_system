from PyQt5.QtWidgets import *
from src.model.item_model import Item
from src.core.enum.attributes_enum import Attributes
from src.core.enum.category_enum import Category
from src.core.enum.dropped_by_enum import DroppedBy
from src.core.enum.found_at_enum import FoundAt
from src.core.enum.item_type_enum import ItemType
from src.core.service.service_facade import ServiceFacade
from src.ui.qt.view.qt_view import QtView


class ItemAddUi(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.item_service = ServiceFacade.get_item_service()
        self.selected_item = None
        self.addPage = self.qt.find_widget(self.window, QWidget, 'addPage')
        self.addNameEdit = self.qt.find_line_edit('addNameEdit')
        self.addCategoryBox = self.qt.find_combo_box('addCategoryBox')
        self.addTypeBox = self.qt.find_combo_box('addTypeBox')
        self.addDescriptionEdit = self.qt.find_text_edit('addDescriptionEdit')
        self.addAttributes = self.qt.find_combo_box('addAttributesBox')
        self.addConsumeMp = self.qt.find_spin_box('addConsumeMp')
        self.addConsumeHt = self.qt.find_spin_box('addConsumeHt')
        self.addStatHp = self.qt.find_spin_box('addStatHp')
        self.addStatMp = self.qt.find_spin_box('addStatMp')
        self.addStatHt = self.qt.find_spin_box('addStatHt')
        self.addStatStr = self.qt.find_spin_box('addStatStr')
        self.addStatAtt = self.qt.find_spin_box('addStatAtt')
        self.addStatInt = self.qt.find_spin_box('addStatInt')
        self.addStatCon = self.qt.find_spin_box('addStatCon')
        self.addStatMaxHt = self.qt.find_spin_box('addStatMaxHt')
        self.addStatMaxHp = self.qt.find_spin_box('addStatMaxHp')
        self.addStatDef = self.qt.find_spin_box('addStatDef')
        self.addStatLck = self.qt.find_spin_box('addStatLck')
        self.addStatGold = self.qt.find_spin_box('addStatGold')
        self.addSell = self.qt.find_double_spin_box('addSell')
        self.addFoundBox = self.qt.find_combo_box('addFoundBox')
        self.addDroppedBox = self.qt.find_combo_box('addDroppedBox')
        self.addEffectEdit = self.qt.find_text_edit('addEffectEdit')
        self.addItemImage = self.qt.find_label('addItemImage')
        self.addItemAnimation = self.qt.find_label('addItemAnimation')
        self.addItemSpecialAnimation = self.qt.find_label('addItemSpecialAnimation')
        self.cancelButton = self.qt.find_tool_button('cancelButton')
        self.resetButton = self.qt.find_tool_button('resetButton')
        self.saveButton = self.qt.find_tool_button('saveButton')
        self.setup_ui()
        # self.animated_item_gif()
        # self.show_item_image()

    def setup_ui(self):
        self.saveButton.clicked.connect(self.on_save)
        self.cancelButton.clicked.connect(self.on_cancel)
        self.resetButton.clicked.connect(self.on_reset)

    def item_selected(self, args):
        item = args['selected_item']
        self.log.info('Item selected for update: {}'.format(item))
        self.selected_item = item
        self.addNameEdit.setText(item.name)
        self.addCategoryBox.setCurrentText(item.category)
        self.addTypeBox.setCurrentText(item.item_type)
        self.addDescriptionEdit.setText(item.description)
        self.addAttributes.setCurrentText(item.attributes)
        self.addConsumeMp.setValue(item.consume_mp)
        self.addConsumeHt.setValue(item.consume_heart)
        self.addStatHp.setValue(item.statistics_hp)
        self.addStatMp.setValue(item.statistics_mp)
        self.addStatHt.setValue(item.statistics_heart)
        self.addStatStr.setValue(item.statistics_str)
        self.addStatAtt.setValue(item.statistics_att)
        self.addStatInt.setValue(item.statistics_int)
        self.addStatCon.setValue(item.statistics_con)
        self.addStatMaxHt.setValue(item.statistics_max_ht)
        self.addStatMaxHp.setValue(item.statistics_max_hp)
        self.addStatDef.setValue(item.statistics_def)
        self.addStatLck.setValue(item.statistics_lck)
        self.addStatGold.setValue(item.statistics_gold)
        self.addSell.setValue(item.sell)
        self.addFoundBox.setCurrentText(item.found_at)
        self.addDroppedBox.setCurrentText(item.dropped_by)
        self.addEffectEdit.setText(item.effect)
        self.addItemImage.setText(item.image)
        self.addItemAnimation.setText(item.animation)
        self.addItemSpecialAnimation.setText(item.special_animation)

    def on_reset(self):
        self.log.info('Item form reset')
        self.selected_item = None
        self.addNameEdit.setText(None)
        self.addCategoryBox.setCurrentIndex(0)
        self.addTypeBox.setCurrentIndex(0)
        self.addDescriptionEdit.setText(None)
        self.addAttributes.setCurrentIndex(0)
        self.addConsumeMp.setValue(0)
        self.addConsumeHt.setValue(0)
        self.addStatHp.setValue(0)
        self.addStatMp.setValue(0)
        self.addStatHt.setValue(0)
        self.addStatStr.setValue(0)
        self.addStatAtt.setValue(0)
        self.addStatInt.setValue(0)
        self.addStatCon.setValue(0)
        self.addStatMaxHt.setValue(0)
        self.addStatMaxHp.setValue(0)
        self.addStatDef.setValue(0)
        self.addStatLck.setValue(0)
        self.addStatGold.setValue(0)
        self.addSell.setValue(0.00)
        self.addFoundBox.setCurrentIndex(0)
        self.addDroppedBox.setCurrentIndex(0)
        self.addEffectEdit.setText(None)
        self.addItemImage.setText(None)
        self.addItemAnimation.setText(None)
        self.addItemSpecialAnimation.setText(None)
        self.window.repaint()

    def on_save(self):
        self.selected_item = self.selected_item if self.selected_item else Item()
        self.selected_item.name = self.addNameEdit.text()
        self.selected_item.category = Category[self.addCategoryBox.currentText()]
        self.selected_item.item_type = ItemType[self.addTypeBox.currentText()]
        self.selected_item.description = self.addDescriptionEdit.text()
        self.selected_item.attributes = Attributes[self.addAttributes.currentText()]
        self.selected_item.consume_mp = self.addConsumeMp.value()
        self.selected_item.consume_heart = self.addConsumeHt.value()
        self.selected_item.statistics_hp = self.addStatHp.value()
        self.selected_item.statistics_mp = self.addStatMp.value()
        self.selected_item.statistics_heart = self.addStatHt.value()
        self.selected_item.statistics_str = self.addStatStr.value()
        self.selected_item.statistics_att = self.addStatAtt.value()
        self.selected_item.statistics_int = self.addStatInt.value()
        self.selected_item.statistics_con = self.addStatCon.value()
        self.selected_item.statistics_max_ht = self.addStatMaxHt.value()
        self.selected_item.statistics_max_hp = self.addStatMaxHp.value()
        self.selected_item.statistics_def = self.addStatDef.value()
        self.selected_item.statistics_lck = self.addStatLck.value()
        self.selected_item.statistics_gold = self.addStatGold.value()
        self.selected_item.sell = self.addSell.value()
        self.selected_item.found_at = FoundAt[self.addFoundBox.currentText()]
        self.selected_item.dropped_by = DroppedBy[self.addDroppedBox.currentText()]
        self.selected_item.effect = self.addEffectEdit.text()
        self.selected_item.image = self.addItemImage
        self.selected_item.animation = self.addItemAnimation
        self.selected_item.special_animation = self.addItemSpecialAnimation
        self.item_service.save(self.selected_item)
        self.on_reset()
        self.log.info('Item saved: {}'.format(self.selected_item))

    def on_cancel(self):
        self.on_reset()
        self.parent.itemInformationUi.categoryBox.setCurrentIndex(0)
