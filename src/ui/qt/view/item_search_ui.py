import base64
import io
import cv2
import imageio
import numpy
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QListView, QListWidgetItem, QMessageBox
from pymysql import InternalError
from core.service.service_facade import ServiceFacade
from ui.qt.view.qt_view import QtView


class ItemSearchUi(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.item_service = ServiceFacade.get_item_service()
        self.selected_id = None
        self.selected_item = None
        self.searchPage = self.qt.find_widget(self.window, QWidget, 'searchPage')
        self.searchList = self.qt.find_list_widget('searchList')
        self.entities_id_list = []
        self.setup_ui()

    def setup_ui(self):
        pass
        # self.searchList.mouseReleaseEvent = functools.partial(self.item_double_click)

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
                item_image = self.str_to_rgb(item_image_right)
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

    #
    #     for item in self.item_service.list():
    #         while item_category in item.category:
    #             widget_list.setViewMode(QListView.IconMode)
    #             list_item = QListWidgetItem()
    #             item_icon = QIcon()
    #             item_image_right = item.image.replace('b"b', '').replace("'", '').replace('"', '')
    #             item_image = self.str_to_rgb(item_image_right)
    #             height, width, channel = item_image.shape
    #             bytes_per_line = 3 * width
    #             q_img = QImage(item_image.data, width, height,
    #                            bytes_per_line, QImage.Format_RGB888).rgbSwapped()
    #             item_icon.addPixmap(QPixmap(q_img),
    #                                 QIcon.Normal, QIcon.Off)
    #             list_item.setIcon(item_icon)
    #             list_item.setText(item.name.replace(' ', '\n'))
    #             list_item.setWhatsThis(item.entity_id)
    #             widget_list.addItem(list_item)
    #             self.entities_id_list.append(f'{list_item.whatsThis()}')
    #             break
    #
    # def item_double_click(self):
    #     pass
    #
    # def btn_search_car_clicked(self):
    #     self.log.info('Tool button: btnSearchCars clicked')
    #     criteria = self.leSearchCar.text() or '*'
    #     try:
    #         if criteria or criteria == '*':
    #             found = self.car_service.list(filters=criteria if criteria != '*' else None)
    #             if found and len(found) > 0:
    #                 self.populate_table_cars(found)
    #                 self.parent.set_status('Found {} car models matching: {}'.format(len(found), criteria))
    #             else:
    #                 msg = 'No cars found for the matching criteria: {}'.format(criteria)
    #                 self.parent.set_status(msg, Color.ORANGE)
    #                 self.log.warn(msg)
    #     except InternalError:
    #         msg = 'Invalid criteria {}'.format(criteria)
    #         self.parent.set_status(msg, Color.RED)
    #         self.log.error(msg)
    #
    # def populate_table_cars(self, table_data: list):
    #     self.log.info('Found = {}'.format(table_data))
    #     self.tableCars.setModel(DefaultTableModel(Car, table_data=table_data, parent=self.tableCars))
    #
    # def double_clicked_row(self, index: QModelIndex):
    #     car = self.tableCars.model().row(index)
    #     self.log.info('Table: tableCars clicked: {}'.format(car))
    #     self.stackedPanelCars.setCurrentIndex(1)
    #     self.parent.car_edit.bbAddCar.button(QDialogButtonBox.Save).setDefault(True)
    #     EventBus.get('car-selection-bus').emit('rowSelected', selected_item=car)

    @staticmethod
    def str_to_rgb(base64_str):
        image_data = base64.b64decode(base64_str)
        image = imageio.imread(io.BytesIO(image_data))
        return cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2RGB)