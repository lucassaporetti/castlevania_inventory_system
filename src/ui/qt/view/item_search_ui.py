import functools
from ui.qt.view.qt_view import QtView
from PyQt5.QtGui import QIcon, QImage, QPixmap
from core.service.service_facade import ServiceFacade
from PyQt5.QtWidgets import QWidget, QListView, QListWidgetItem, QMessageBox


class ItemSearchUi(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.item_service = ServiceFacade.get_item_service()
        self.selected_id = None
        self.selected_item = None
        self.searchPage = self.qt.find_widget(self.window, QWidget, 'searchPage')
        self.searchList = self.qt.find_list_widget('searchList')
        self.weaponPage = self.parent.itemInformationUi.weaponPage
        self.entities_id_list = []
        self.setup_ui()

    def setup_ui(self):
        self.searchList.mouseDoubleClickEvent = functools.partial(self.item_click)

    def items_found(self):
        self.log.info('Tool button: btnSearchItems clicked')
        self.searchList.clear()
        criteria = self.parent.searchLine.text().upper().strip()
        found = False
        for item in self.item_service.list():
            if criteria in item.name.upper().strip() or criteria in item.category.upper().strip() \
                    or criteria in item.item_type.upper().strip() or criteria in item.attributes.upper().strip() \
                    or criteria in item.found_at.upper().strip() or criteria in item.dropped_by.upper().strip():
                self.log.info('Found: {} found with this criteria({})'.format(item, criteria))
                self.searchList.setViewMode(QListView.ListMode)
                list_item = QListWidgetItem()
                item_icon = QIcon()
                item_image_right = item.image.replace('b"b', '').replace("'", '').replace('"', '')
                item_image = self.parent.itemInformationUi.str_to_rgb(item_image_right)
                height, width, channel = item_image.shape
                bytes_per_line = 3 * width
                q_img = QImage(item_image.data, width, height,
                               bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                item_icon.addPixmap(QPixmap(q_img),
                                    QIcon.Normal, QIcon.Off)
                list_item.setIcon(item_icon)
                list_item.setText(f'{item.name} - {item.category} - {item.item_type}'
                                  f' - {item.description} - {item.attributes} -'
                                  f' {item.dropped_by} - {item.found_at}')
                list_item.setWhatsThis(item.entity_id)
                self.searchList.addItem(list_item)
                self.entities_id_list.append(f'{list_item.whatsThis()}')
                found = True
        if found is False:
            self.log.info('Not found: No items are found with this criteria({})'.format(criteria))
            message = QMessageBox()
            message.setStyleSheet("""
                                    background-color: rgb(0, 0, 0); 
                                    font: 12pt 'URW Bookman L'; 
                                    color: rgb(238, 238, 236); 
                                    gridline-color: rgb(46, 52, 54); 
                                    selection-color: rgb(0, 0, 0); 
                                    selection-background-color: rgb(181, 0, 0);
                                    """)
            message.setText('No items found matching these criteria')
            message.setWindowTitle('Sorry...')
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()

    def item_click(self, event):
        selection = self.searchList.currentItem()
        if selection is not None:
            for item in self.item_service.list():
                if selection.whatsThis() == item.entity_id:
                    self.parent.itemInformationUi.selected_id = selection.whatsThis()
                    self.parent.itemInformationUi.selected_item = item
                    self.parent.stackedMain.setCurrentIndex(1)
                    if item.category == 'Weapon':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(0)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Shield':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(1)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Armor/Clothe':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(2)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Relic':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(3)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Spell':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(4)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Other':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(5)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Consumable':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(6)
                        return self.parent.itemInformationUi.info_item(item)
                    elif item.category == 'Standard':
                        self.parent.itemInformationUi.categoryBox.setCurrentIndex(7)
                        return self.parent.itemInformationUi.info_item(item)
        else:
            pass
