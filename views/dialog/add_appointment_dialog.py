import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_appointment import Ui_AddAppointmentDialog

class AddAppointmentDialog(QDialog, Ui_AddAppointmentDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent

        self.btn_add_appointment.clicked.connect(self.add_data)

    def add_data(self):
        add_data = {
            "appointment_date": self.appointment_date.date().toString("yyyy-MM-dd"),
            "appointment_time": self.appointment_time.time().toString("HH:mm:ss"),
            "purpose": self.purpose.toPlainText(),
        }

        if self.parent:
            self.close()
            self.parent.add_appointment(add_data)