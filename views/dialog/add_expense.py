# Form implementation generated from reading ui file 'add_expense.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddExpenseDialog(object):
    def setupUi(self, AddExpenseDialog):
        AddExpenseDialog.setObjectName("AddExpenseDialog")
        AddExpenseDialog.resize(330, 374)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddExpenseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(parent=AddExpenseDialog)
        self.titleLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("font-weight: bold;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.categoryLabel_2 = QtWidgets.QLabel(parent=AddExpenseDialog)
        self.categoryLabel_2.setObjectName("categoryLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.categoryLabel_2)
        self.expense_type = QtWidgets.QLineEdit(parent=AddExpenseDialog)
        self.expense_type.setObjectName("expense_type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_type)
        self.dateLabel = QtWidgets.QLabel(parent=AddExpenseDialog)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dateLabel)
        self.expense_date = QtWidgets.QDateEdit(parent=AddExpenseDialog)
        self.expense_date.setCalendarPopup(True)
        self.expense_date.setObjectName("expense_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_date)
        self.amountLabel = QtWidgets.QLabel(parent=AddExpenseDialog)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.amountLabel)
        self.amount = QtWidgets.QDoubleSpinBox(parent=AddExpenseDialog)
        self.amount.setDecimals(0)
        self.amount.setMaximum(1000000000.0)
        self.amount.setProperty("groupSeparatorShown", True)
        self.amount.setObjectName("amount")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.amount)
        self.detailsLabel = QtWidgets.QLabel(parent=AddExpenseDialog)
        self.detailsLabel.setObjectName("detailsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.detailsLabel)
        self.description = QtWidgets.QTextEdit(parent=AddExpenseDialog)
        self.description.setObjectName("description")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.description)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_add_expense = QtWidgets.QPushButton(parent=AddExpenseDialog)
        self.btn_add_expense.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_add_expense.setStyleSheet("QPushButton {\n"
"    background-color: #2ecc71;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.btn_add_expense.setObjectName("btn_add_expense")
        self.horizontalLayout_3.addWidget(self.btn_add_expense)
        self.btn_cancel = QtWidgets.QPushButton(parent=AddExpenseDialog)
        self.btn_cancel.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_cancel.setStyleSheet("QPushButton {\n"
"    background-color: #585858;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)
        self.timeLabel = QtWidgets.QLabel(parent=AddExpenseDialog)
        self.timeLabel.setObjectName("timeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.timeLabel)
        self.expense_time = QtWidgets.QTimeEdit(parent=AddExpenseDialog)
        self.expense_time.setObjectName("expense_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_time)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(AddExpenseDialog)
        QtCore.QMetaObject.connectSlotsByName(AddExpenseDialog)

    def retranslateUi(self, AddExpenseDialog):
        _translate = QtCore.QCoreApplication.translate
        AddExpenseDialog.setWindowTitle(_translate("AddExpenseDialog", "Thêm chi phí"))
        self.titleLabel.setText(_translate("AddExpenseDialog", "Thêm chi phí"))
        self.categoryLabel_2.setText(_translate("AddExpenseDialog", "Loại chi phí:"))
        self.expense_type.setPlaceholderText(_translate("AddExpenseDialog", "Nhập loại chi phí"))
        self.dateLabel.setText(_translate("AddExpenseDialog", "Ngày phát sinh:"))
        self.expense_date.setDisplayFormat(_translate("AddExpenseDialog", "dd/MM/yyyy"))
        self.amountLabel.setText(_translate("AddExpenseDialog", "Số tiền:"))
        self.amount.setSuffix(_translate("AddExpenseDialog", " VNĐ"))
        self.detailsLabel.setText(_translate("AddExpenseDialog", "Chi tiết:"))
        self.description.setPlaceholderText(_translate("AddExpenseDialog", "Nhập chi tiết..."))
        self.btn_add_expense.setText(_translate("AddExpenseDialog", "Thêm"))
        self.btn_cancel.setText(_translate("AddExpenseDialog", "Hủy"))
        self.timeLabel.setText(_translate("AddExpenseDialog", "Thời gian:"))
        self.expense_time.setDisplayFormat(_translate("AddExpenseDialog", "hh:mm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddExpenseDialog = QtWidgets.QDialog()
    ui = Ui_AddExpenseDialog()
    ui.setupUi(AddExpenseDialog)
    AddExpenseDialog.show()
    sys.exit(app.exec())
