import os
import base64
import functools
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from src.ui.qt.view.qt_view import QtView
from src.core.service.service_facade import ServiceFacade


class ItemEditUi(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.item_service = ServiceFacade.get_item_service()
        self.edited_item = None
        self.editPage = self.qt.find_widget(self.window, QWidget, 'editPage')
        self.editNameEdit = self.qt.find_line_edit('editNameEdit')
        self.editCategoryBox = self.qt.find_combo_box('editCategoryBox')
        self.editTypeBox = self.qt.find_combo_box('editTypeBox')
        self.editDescriptionEdit = self.qt.find_text_edit('editDescriptionEdit')
        self.editAttributes = self.qt.find_combo_box('editAttributesBox')
        self.editConsumeMp = self.qt.find_spin_box('editConsumeMp')
        self.editConsumeHt = self.qt.find_spin_box('editConsumeHt')
        self.editStatHp = self.qt.find_spin_box('editStatHp')
        self.editStatMp = self.qt.find_spin_box('editStatMp')
        self.editStatHt = self.qt.find_spin_box('editStatHt')
        self.editStatStr = self.qt.find_spin_box('editStatStr')
        self.editStatAtt = self.qt.find_spin_box('editStatAtt')
        self.editStatInt = self.qt.find_spin_box('editStatInt')
        self.editStatCon = self.qt.find_spin_box('editStatCon')
        self.editStatMaxHt = self.qt.find_spin_box('editStatMaxHt')
        self.editStatMaxHp = self.qt.find_spin_box('editStatMaxHp')
        self.editStatDef = self.qt.find_spin_box('editStatDef')
        self.editStatLck = self.qt.find_spin_box('editStatLck')
        self.editStatGold = self.qt.find_spin_box('editStatGold')
        self.editSell = self.qt.find_double_spin_box('editSell')
        self.editFoundBox = self.qt.find_combo_box('editFoundBox')
        self.editDroppedBox = self.qt.find_combo_box('editDroppedBox')
        self.editEffectEdit = self.qt.find_text_edit('editEffectEdit')
        self.editItemImage = self.qt.find_label('editItemImage')
        self.editItemAnimation = self.qt.find_label('editItemAnimation')
        self.editItemSpecialAnimation = self.qt.find_label('editItemSpecialAnimation')
        self.editCancelButton = self.qt.find_tool_button('editCancelButton')
        self.editResetButton = self.qt.find_tool_button('editResetButton')
        self.editSaveButton = self.qt.find_tool_button('editSaveButton')
        self.selected_item = None
        self.entityId = None
        self.imageData = None
        self.animationData = None
        self.specialAnimationData = None
        self.setup_ui()

    def setup_ui(self):
        self.editSaveButton.clicked.connect(self.on_save)
        self.editCancelButton.clicked.connect(self.on_cancel)
        self.editResetButton.clicked.connect(self.on_reset)
        self.editItemImage.mouseReleaseEvent = \
            functools.partial(self.open_file, source_object=self.editItemImage)
        self.editItemAnimation.mouseReleaseEvent = \
            functools.partial(self.open_file, source_object=self.editItemAnimation)
        self.editItemSpecialAnimation.mouseReleaseEvent = \
            functools.partial(self.open_file, source_object=self.editItemSpecialAnimation)

    def item_selected(self, selected_id):
        for item in self.item_service.list():
            if selected_id == item.entity_id:
                self.log.info('Item selected for update: {}'.format(item))
                self.entityId = item.entity_id
                self.editNameEdit.setText(item.name)
                self.editCategoryBox.setCurrentText(item.category)
                self.editTypeBox.setCurrentText(item.item_type)
                self.editDescriptionEdit.setText(item.description)
                self.editAttributes.setCurrentText(item.attributes)
                self.editConsumeMp.setValue(item.consume_mp)
                self.editConsumeHt.setValue(item.consume_heart)
                self.editStatHp.setValue(item.statistics_hp)
                self.editStatMp.setValue(item.statistics_mp)
                self.editStatHt.setValue(item.statistics_heart)
                self.editStatStr.setValue(item.statistics_str)
                self.editStatAtt.setValue(item.statistics_att)
                self.editStatInt.setValue(item.statistics_int)
                self.editStatCon.setValue(item.statistics_con)
                self.editStatMaxHt.setValue(item.statistics_max_ht)
                self.editStatMaxHp.setValue(item.statistics_max_hp)
                self.editStatDef.setValue(item.statistics_def)
                self.editStatLck.setValue(item.statistics_lck)
                self.editStatGold.setValue(item.statistics_gold)
                self.editSell.setValue(item.sell)
                self.editFoundBox.setCurrentText(item.found_at)
                self.editDroppedBox.setCurrentText(item.dropped_by)
                self.editEffectEdit.setText(item.effect)
                self.edited_item = item

    def on_reset(self):
        self.log.info('Item form reset')
        self.editNameEdit.setText(None)
        self.editCategoryBox.setCurrentIndex(0)
        self.editTypeBox.setCurrentIndex(0)
        self.editDescriptionEdit.setText(None)
        self.editAttributes.setCurrentIndex(0)
        self.editConsumeMp.setValue(0)
        self.editConsumeHt.setValue(0)
        self.editStatHp.setValue(0)
        self.editStatMp.setValue(0)
        self.editStatHt.setValue(0)
        self.editStatStr.setValue(0)
        self.editStatAtt.setValue(0)
        self.editStatInt.setValue(0)
        self.editStatCon.setValue(0)
        self.editStatMaxHt.setValue(0)
        self.editStatMaxHp.setValue(0)
        self.editStatDef.setValue(0)
        self.editStatLck.setValue(0)
        self.editStatGold.setValue(0)
        self.editSell.setValue(0.00)
        self.editFoundBox.setCurrentIndex(0)
        self.editDroppedBox.setCurrentIndex(0)
        self.editEffectEdit.setText(None)
        self.editItemImage.setText('Click')
        self.editItemAnimation.setText('Click')
        self.editItemSpecialAnimation.setText('Click')
        self.window.repaint()

    def on_save(self):
        self.edited_item.name = self.editNameEdit.text()
        self.edited_item.category = self.editCategoryBox.currentText()
        self.edited_item.item_type = self.editTypeBox.currentText()
        self.edited_item.description = self.editDescriptionEdit.toPlainText()
        self.edited_item.attributes = self.editAttributes.currentText()
        self.edited_item.consume_mp = self.editConsumeMp.value()
        self.edited_item.consume_heart = self.editConsumeHt.value()
        self.edited_item.statistics_hp = self.editStatHp.value()
        self.edited_item.statistics_mp = self.editStatMp.value()
        self.edited_item.statistics_heart = self.editStatHt.value()
        self.edited_item.statistics_str = self.editStatStr.value()
        self.edited_item.statistics_att = self.editStatAtt.value()
        self.edited_item.statistics_int = self.editStatInt.value()
        self.edited_item.statistics_con = self.editStatCon.value()
        self.edited_item.statistics_max_ht = self.editStatMaxHt.value()
        self.edited_item.statistics_max_hp = self.editStatMaxHp.value()
        self.edited_item.statistics_def = self.editStatDef.value()
        self.edited_item.statistics_lck = self.editStatLck.value()
        self.edited_item.statistics_gold = self.editStatGold.value()
        self.edited_item.sell = self.editSell.value()
        self.edited_item.found_at = self.editFoundBox.currentText()
        self.edited_item.dropped_by = self.editDroppedBox.currentText()
        self.edited_item.effect = self.editEffectEdit.toPlainText()
        self.edited_item.image = self.imageData
        self.edited_item.animation = self.animationData
        self.edited_item.special_animation = self.specialAnimationData
        self.edited_item.entity_id = self.entityId
        self.item_service.save(self.edited_item)
        self.on_reset()
        self.parent.stackedMain.setCurrentIndex(0)
        self.parent.itemInformationUi.entities_id_list.clear()
        self.parent.itemInformationUi.update_lists()
        self.log.info('Item edited: {}'.format(self.edited_item))

    def on_cancel(self):
        self.on_reset()
        self.parent.stackedMain.setCurrentIndex(0)
        self.parent.itemInformationUi.categoryBox.setCurrentIndex(8)

    def open_file(self, event, source_object):
        directory = os.path.expanduser("~/GIT-Repository/"
                                       "castlevania_inventory_system/"
                                       "src/resources/images/items")
        file_name = QFileDialog.getOpenFileName(caption="Choose item image...",
                                                directory=directory, filter='*',
                                                options=QFileDialog.DontUseNativeDialog)
        if file_name == ('', ''):
            if source_object == self.editItemImage:
                self.imageData = 'Without Image'
                return self.editItemImage.setText('Without\nImage')
            elif source_object == self.editItemAnimation:
                self.animationData = 'Without Image'
                return self.editItemAnimation.setText('Without Image')
            else:
                self.specialAnimationData = 'Without Image'
                return self.editItemSpecialAnimation.setText('Without Image')
        else:
            item_image = file_name[0]
            if source_object == self.editItemImage:
                q_image = QtGui.QImage(item_image)
                q_pixmap = QtGui.QPixmap.fromImage(q_image)
                q_pixmap_image = QtGui.QPixmap(q_pixmap)
                source_object.setPixmap(q_pixmap_image)
                source_object.show()
            else:
                movie = QtGui.QMovie(item_image)
                source_object.setMovie(movie)
                movie.start()
            with open(file_name[0], 'rb') as file:
                image_read = file.read()
                binary_data = base64.b64encode(image_read)
            if source_object == self.editItemImage:
                self.imageData = binary_data
                return self.imageData
            elif source_object == self.editItemAnimation:
                self.animationData = binary_data
                return self.animationData
            else:
                self.specialAnimationData = binary_data
                return self.specialAnimationData
