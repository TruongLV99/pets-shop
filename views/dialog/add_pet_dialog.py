import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_pet import Ui_AddPetDialog

class AddPetDialog(QDialog, Ui_AddPetDialog):
    def __init__(self, parent=None, customer_id=0):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.customer_id = customer_id

        self.btn_add_pet.clicked.connect(self.add_data)

    def add_data(self):
        add_data = {
            'customer_id': self.customer_id,
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
            self.close()
            self.parent.add_pet(add_data)
