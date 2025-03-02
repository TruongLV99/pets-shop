import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_customer import Ui_AddCustomerDialog

class AddCustomerDialog(QDialog, Ui_AddCustomerDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_add_customer.clicked.connect(self.add_data)

    def add_data(self):
        add_data = {
            "name": self.name.text(),
            "phone_number": self.phone_number.text(),
        }

        if self.parent:
            self.close()
            self.parent.add_customer(add_data)
