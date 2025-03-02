import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_expense import Ui_AddExpenseDialog

class AddExpenseDialog(QDialog, Ui_AddExpenseDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent

        self.btn_add_expense.clicked.connect(self.add_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

    def add_data(self):
        add_data = {
            "expense_type": self.expense_type.text(),
            "expense_date": self.expense_date.date().toString("yyyy-MM-dd"),
            "expense_time": self.expense_time.time().toString("HH:mm:ss"),
            "amount": self.amount.text(),
            "description": self.description.toPlainText(),
        }

        if self.parent:
            self.close()
            self.parent.add_expense(add_data)

    def closeEvt(self):
        self.close()
