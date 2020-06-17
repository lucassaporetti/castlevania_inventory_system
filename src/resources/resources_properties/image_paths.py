from ui.qt.view.qt_view import QtView


class ImagePaths(QtView):
    def __init__(self, parent: QtView):
        super().__init__(parent.window, parent)
        self.characterAddImage = self.qt.find_label('characterAddImage')
        self.characterWeaponImage = self.qt.find_label('characterWeaponImage')
        self.characterShieldImage = self.qt.find_label('characterShieldImage')
        self.characterArmorImage = self.qt.find_label('characterArmorImage')
        self.characterRelicImage = self.qt.find_label('characterRelicImage')
        self.characterSpellImage = self.qt.find_label('characterSpellImage')
        self.characterOtherImage = self.qt.find_label('characterOtherImage')
        self.characterConsumableImage = self.qt.find_label('characterConsumableImage')
        self.characterStandardImage = self.qt.find_label('characterStandardImage')
        self.characterDeleteImage = self.qt.find_label('characterDeleteImage')
        self.setup_ui()

    def setup_ui(self):
        self.characterAddImage.hide()
        self.characterWeaponImage.hide()
        self.characterShieldImage.hide()
        self.characterArmorImage.hide()
        self.characterRelicImage.hide()
        self.characterSpellImage.hide()
        self.characterOtherImage.hide()
        self.characterConsumableImage.hide()
        self.characterStandardImage.hide()
        self.characterDeleteImage.hide()

    def get_image(self, image_index):
        if image_index == 0:
            self.setup_ui()
            return self.characterWeaponImage.show()
        elif image_index == 1:
            self.setup_ui()
            return self.characterShieldImage.show()
        elif image_index == 2:
            self.setup_ui()
            return self.characterArmorImage.show()
        elif image_index == 3:
            self.setup_ui()
            return self.characterRelicImage.show()
        elif image_index == 4:
            self.setup_ui()
            return self.characterSpellImage.show()
        elif image_index == 5:
            self.setup_ui()
            return self.characterOtherImage.show()
        elif image_index == 6:
            self.setup_ui()
            return self.characterConsumableImage.show()
        elif image_index == 7:
            self.setup_ui()
            return self.characterStandardImage.show()
        elif image_index == 8:
            self.setup_ui()
        elif image_index == 9:
            self.setup_ui()
            return self.characterAddImage.show()
        elif image_index == 10:
            self.setup_ui()
            return self.characterDeleteImage.show()
