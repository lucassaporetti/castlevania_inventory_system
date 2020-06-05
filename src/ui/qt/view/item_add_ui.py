from PyQt5.QtWidgets import *
from core.service.service_facade import ServiceFacade
from src.ui.qt.view.qt_view import QtView


class ItemAddUi(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.item_service = ServiceFacade.get_item_service()
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

    def setup_ui(self):
        EventBus.get('car-selection-bus').subscribe('rowSelected', self.car_selected)
        self.bbAddCar.accepted.connect(self.on_save)
        self.bbAddCar.rejected.connect(self.on_cancel)
        self.bbAddCar.button(QDialogButtonBox.Reset).clicked.connect(self.on_reset)

    def car_selected(self, args):
        car = args['selected_item']
        self.log.info('Car selected for update: {}'.format(car))
        self.selected_car = car
        self.leCarName.setText(car.name)
        self.leChassis.setText(car.chassis)
        self.cmbColor.setCurrentText(car.color.name)
        self.spbDoors.setValue(car.doors)
        self.cmbFuel.setCurrentText(car.fuel.name)
        self.lePlate.setText(car.plate)
        self.spbPrice.setValue(car.price)

    def on_reset(self):
        self.log.info('Car form reset')
        self.selected_car = None
        self.leCarName.setText(None)
        self.leChassis.setText(None)
        self.cmbColor.setCurrentIndex(0)
        self.spbDoors.setValue(3)
        self.cmbFuel.setCurrentIndex(0)
        self.lePlate.setText(None)
        self.spbPrice.setValue(0.00)
        self.window.repaint()

    def on_save(self):
        self.selected_car = self.selected_car if self.selected_car else Car()
        self.selected_car.name = self.leCarName.text()
        self.selected_car.chassis = self.leChassis.text()
        self.selected_car.color = Color[self.cmbColor.currentText()]
        self.selected_car.doors = self.spbDoors.value()
        self.selected_car.fuel = Fuel[self.cmbFuel.currentText()]
        self.selected_car.plate = self.lePlate.text()
        self.selected_car.price = self.spbPrice.value()
        self.selected_car.available = self.selected_car.available.value
        self.car_service.save(self.selected_car)
        self.parent.car_search.btn_search_car_clicked()
        self.parent.car_search.stackedPanelCars.setCurrentIndex(0)
        self.on_reset()
        self.log.info('Car saved: {}'.format(self.selected_car))

    def on_cancel(self):
        self.on_reset()
        self.parent.car_search.stackedPanelCars.setCurrentIndex(0)


