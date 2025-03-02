import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_health import Ui_EditHealthDialog
from PyQt6.QtCore import QTime

class EditHealthDialog(QDialog, Ui_EditHealthDialog):
    def __init__(self, parent=None, health=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.health = health

        self.btn_edit_health.clicked.connect(self.updated_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

        if health:
            # health_time = health['health_time']
            # total_seconds = health_time.total_seconds()

            # hours = int(total_seconds // 3600)
            # minutes = int((total_seconds % 3600) // 60)
            # seconds = int(total_seconds % 60)

            # qtime_value = QTime(hours, minutes, seconds)

            self.vaccine_name.setText(health['vaccine_name'])
            self.vaccination_date.setDate(health['vaccination_date'])
            self.health_check_date.setDate(health['health_check_date'])
            self.health_condition.setPlainText(health['health_condition'])

    def updated_data(self):
        updated_data = {
            "id": self.health['id'],
            "vaccine_name": self.vaccine_name.text(),
            "vaccination_date": self.vaccination_date.date().toString("yyyy-MM-dd"),
            "health_check_date": self.health_check_date.date().toString("yyyy-MM-dd"),
            "health_condition": self.health_condition.toPlainText(),
        }

        if self.parent:
            self.close()
            self.parent.update_health(updated_data)

    def closeEvt(self):
        self.close()
