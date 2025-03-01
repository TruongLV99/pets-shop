import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_pet import Ui_EditPetDialog

class EditPetDialog(QDialog, Ui_EditPetDialog):
    def __init__(self, parent=None, pet=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.pet = pet

        self.btn_edit_pet.clicked.connect(self.updated_data)

        if pet:
            self.name.setText(pet['name'])
            self.breed.setText(pet['breed'])
            self.birth_date.setDate(pet['birth_date'])
            self.color.setText(pet['color'])
            self.weight.setText(pet['weight'])
            self.height.setText(pet['height'])
            self.length.setText(pet['length'])
            self.special_features.setPlainText(pet['special_features'])

    def updated_data(self):
        updated_data = {
            "id": self.pet['id'],
            "name": self.name.text(),
            "breed": self.breed.text(),
            "birth_date": self.birth_date.date().toString("yyyy-MM-dd"),
            "color": self.color.text(),
            "weight": self.weight.text(),
            "height": self.height.text(),
            "length": self.length.text(),
            "special_features": self.special_features.toPlainText(),
        }

        if self.parent:
            self.parent.update_pet(updated_data)
            self.close()
