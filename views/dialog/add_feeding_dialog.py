import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_feeding import Ui_AddFeedingDialog

class AddFeedingDialog(QDialog, Ui_AddFeedingDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_add_feeding.clicked.connect(self.add_data)

    def add_data(self):
        add_data = {
            "food_type": self.food_type.text(),
            "feeding_date": self.feeding_date.date().toString("yyyy-MM-dd"),
            "feeding_time": self.feeding_time.time().toString("HH:mm:ss"),
            "quantity": self.quantity.text(),
        }

        if self.parent:
            self.close()
            self.parent.add_feeding(add_data)
