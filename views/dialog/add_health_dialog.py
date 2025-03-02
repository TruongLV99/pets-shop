import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_health import Ui_AddHealthDialog

class AddHealthDialog(QDialog, Ui_AddHealthDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_add_health.clicked.connect(self.add_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

    def add_data(self):
        add_data = {
            "vaccine_name": self.vaccine_name.text(),
            "vaccination_date": self.vaccination_date.date().toString("yyyy-MM-dd"),
            "health_check_date": self.health_check_date.date().toString("yyyy-MM-dd"),
            "health_condition": self.health_condition.toPlainText(),
        }

        if self.parent:
            self.close()
            self.parent.add_health(add_data)

    def closeEvt(self):
        self.close()
