import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_expense import Ui_EditExpenseDialog
from PyQt6.QtCore import QTime

class EditExpenseDialog(QDialog, Ui_EditExpenseDialog):
    def __init__(self, parent=None, expense=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.expense = expense

        self.btn_edit_expense.clicked.connect(self.updated_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

        if expense:
            expense_time = expense['expense_time']
            total_seconds = expense_time.total_seconds()

            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            seconds = int(total_seconds % 60)

            qtime_value = QTime(hours, minutes, seconds)

            self.expense_type.setText(expense['expense_type'])
            self.expense_date.setDate(expense['expense_date'])
            self.expense_time.setTime(qtime_value)
            self.amount.setValue(float(expense['amount']))
            self.description.setPlainText(expense['description'])

    def updated_data(self):
        updated_data = {
            "id": self.expense['id'],
            "expense_type": self.expense_type.text(),
            "expense_date": self.expense_date.date().toString("yyyy-MM-dd"),
            "expense_time": self.expense_time.time().toString("HH:mm:ss"),
            "amount": self.amount.text(),
            "description": self.description.toPlainText(),
        }

        if self.parent:
            self.close()
            self.parent.update_expense(updated_data)

    def closeEvt(self):
        self.close()
