from PyQt5.QtWidgets import *

from core.config.app_configs import AppConfigs
from core.service.item_service import ItemService
from src.ui.qt.view.qt_view import QtView


class ItemAddUi(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.item_service = ItemService(AppConfigs.repository_type(), AppConfigs.database_type(), Model.CAR)
        self.selected_item = None
        self.addPage = self.qt.find_widget(self.window, QWidget, 'addPage')
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
        self.addDroppedBox = self.qt.find_combo_box('addFDroppedBox')
        self.addEffectEdit = self.qt.find_text_edit('addEffectEdit')
        self.addNameEdit = self.qt.find_line_edit('addNameEdit')
        self.addItemImage = self.qt.find_label('addItemImage')
        self.addItemAnimation = self.qt.find_label('addItemAnimation')
        self.addItemSpecialAnimation = self.qt.find_label('addItemSpecialAnimation')
        self.cancelButton = self.qt.find_push_button('cancelButton')
        self.resetButton = self.qt.find_push_button('resetButton')
        self.saveButton = self.qt.find_push_button('saveButton')
        self.setup_ui()
        # self.animated_item_gif()
        # self.show_item_image()

