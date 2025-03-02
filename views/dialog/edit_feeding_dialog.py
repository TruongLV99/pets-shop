import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_feeding import Ui_EditFeedingDialog
from PyQt6.QtCore import QTime

class EditFeedingDialog(QDialog, Ui_EditFeedingDialog):
    def __init__(self, parent=None, feeding=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.feeding = feeding

        self.btn_edit_feeding.clicked.connect(self.updated_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

        if feeding:
            feeding_time = feeding['feeding_time']
            total_seconds = feeding_time.total_seconds()

            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            seconds = int(total_seconds % 60)

            qtime_value = QTime(hours, minutes, seconds)

            self.food_type.setText(feeding['food_type'])
            self.feeding_date.setDate(feeding['feeding_date'])
            self.feeding_time.setTime(qtime_value)
            self.quantity.setText(feeding['quantity'])

    def updated_data(self):
        updated_data = {
            "id": self.feeding['id'],
            "food_type": self.food_type.text(),
            "feeding_date": self.feeding_date.date().toString("yyyy-MM-dd"),
            "feeding_time": self.feeding_time.time().toString("HH:mm:ss"),
            "quantity": self.quantity.text(),
        }

        if self.parent:
            self.close()
            self.parent.update_feeding(updated_data)

    def closeEvt(self):
        self.close()
