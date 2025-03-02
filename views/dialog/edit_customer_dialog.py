import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_customer import Ui_EditCustomerDialog

class EditCustomerDialog(QDialog, Ui_EditCustomerDialog):
    def __init__(self, parent=None, customer=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.customer = customer

        self.btn_edit_customer.clicked.connect(self.updated_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

        if customer:
            self.name.setText(customer['name'])
            self.phone_number.setText(customer['phone_number'])

    def updated_data(self):
        add_data = {
            "id": self.customer['id'],
            "name": self.name.text(),
            "phone_number": self.phone_number.text(),
        }

        if self.parent:
            self.close()
            self.parent.update_customer(add_data)

    def closeEvt(self):
        self.close()
