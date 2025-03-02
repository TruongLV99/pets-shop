import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_appointment import Ui_EditAppointmentDialog
from PyQt6.QtCore import QTime

class EditAppointmentDialog(QDialog, Ui_EditAppointmentDialog):
    def __init__(self, parent=None, appointment=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.appointment = appointment

        self.btn_edit_appointment.clicked.connect(self.updated_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

        if appointment:
            appointment_time = appointment['appointment_time']
            total_seconds = appointment_time.total_seconds()

            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            seconds = int(total_seconds % 60)

            qtime_value = QTime(hours, minutes, seconds)

            self.appointment_date.setDate(appointment['appointment_date'])
            self.appointment_time.setTime(qtime_value)
            self.purpose.setPlainText(appointment['purpose'])

    def updated_data(self):
        updated_data = {
            "id": self.appointment['id'],
            "appointment_date": self.appointment_date.date().toString("yyyy-MM-dd"),
            "appointment_time": self.appointment_time.time().toString("HH:mm:ss"),
            "purpose": self.purpose.toPlainText(),
        }

        if self.parent:
            self.close()
            self.parent.update_appointment(updated_data)
    
    def closeEvt(self):
        self.close()
