# Form implementation generated from reading ui file 'customer_detail.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CustomerDetailDialog(object):
    def setupUi(self, CustomerDetailDialog):
        CustomerDetailDialog.setObjectName("CustomerDetailDialog")
        CustomerDetailDialog.resize(926, 647)
        self.verticalLayout = QtWidgets.QVBoxLayout(CustomerDetailDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(parent=CustomerDetailDialog)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_7)
        self.customer_pet_table = QtWidgets.QTableWidget(parent=CustomerDetailDialog)
        self.customer_pet_table.setMinimumSize(QtCore.QSize(0, 150))
        self.customer_pet_table.setSizeIncrement(QtCore.QSize(0, 150))
        self.customer_pet_table.setStyleSheet("QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}")
        self.customer_pet_table.setObjectName("customer_pet_table")
        self.customer_pet_table.setColumnCount(10)
        self.customer_pet_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_pet_table.setHorizontalHeaderItem(9, item)
        self.customer_pet_table.horizontalHeader().setCascadingSectionResizes(False)
        self.customer_pet_table.horizontalHeader().setSortIndicatorShown(False)
        self.customer_pet_table.horizontalHeader().setStretchLastSection(True)
        self.customer_pet_table.verticalHeader().setCascadingSectionResizes(False)
        self.customer_pet_table.verticalHeader().setSortIndicatorShown(False)
        self.customer_pet_table.verticalHeader().setStretchLastSection(False)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.customer_pet_table)
        self.label_8 = QtWidgets.QLabel(parent=CustomerDetailDialog)
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_8.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_8)
        self.customer_expense_table = QtWidgets.QTableWidget(parent=CustomerDetailDialog)
        self.customer_expense_table.setMinimumSize(QtCore.QSize(0, 150))
        self.customer_expense_table.setMaximumSize(QtCore.QSize(16777215, 150))
        self.customer_expense_table.setStyleSheet("QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}")
        self.customer_expense_table.setObjectName("customer_expense_table")
        self.customer_expense_table.setColumnCount(5)
        self.customer_expense_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_expense_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_expense_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_expense_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_expense_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_expense_table.setHorizontalHeaderItem(4, item)
        self.customer_expense_table.horizontalHeader().setDefaultSectionSize(150)
        self.customer_expense_table.horizontalHeader().setStretchLastSection(False)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.customer_expense_table)
        self.label_9 = QtWidgets.QLabel(parent=CustomerDetailDialog)
        self.label_9.setMinimumSize(QtCore.QSize(0, 30))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_9.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_9)
        self.customer_appointment_table = QtWidgets.QTableWidget(parent=CustomerDetailDialog)
        self.customer_appointment_table.setMinimumSize(QtCore.QSize(0, 150))
        self.customer_appointment_table.setMaximumSize(QtCore.QSize(16777215, 150))
        self.customer_appointment_table.setStyleSheet("QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}")
        self.customer_appointment_table.setObjectName("customer_appointment_table")
        self.customer_appointment_table.setColumnCount(3)
        self.customer_appointment_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_appointment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_appointment_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_appointment_table.setHorizontalHeaderItem(2, item)
        self.customer_appointment_table.horizontalHeader().setDefaultSectionSize(200)
        self.customer_appointment_table.horizontalHeader().setStretchLastSection(False)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.customer_appointment_table)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(CustomerDetailDialog)
        QtCore.QMetaObject.connectSlotsByName(CustomerDetailDialog)

    def retranslateUi(self, CustomerDetailDialog):
        _translate = QtCore.QCoreApplication.translate
        CustomerDetailDialog.setWindowTitle(_translate("CustomerDetailDialog", "Chi tiết"))
        self.label_7.setText(_translate("CustomerDetailDialog", "Danh sách thú cưng"))
        item = self.customer_pet_table.horizontalHeaderItem(0)
        item.setText(_translate("CustomerDetailDialog", "STT"))
        item = self.customer_pet_table.horizontalHeaderItem(1)
        item.setText(_translate("CustomerDetailDialog", "Mã số"))
        item = self.customer_pet_table.horizontalHeaderItem(2)
        item.setText(_translate("CustomerDetailDialog", "Tên"))
        item = self.customer_pet_table.horizontalHeaderItem(3)
        item.setText(_translate("CustomerDetailDialog", "Giống loài"))
        item = self.customer_pet_table.horizontalHeaderItem(4)
        item.setText(_translate("CustomerDetailDialog", "Ngày sinh"))
        item = self.customer_pet_table.horizontalHeaderItem(5)
        item.setText(_translate("CustomerDetailDialog", "Màu sắc"))
        item = self.customer_pet_table.horizontalHeaderItem(6)
        item.setText(_translate("CustomerDetailDialog", "Cân nặng"))
        item = self.customer_pet_table.horizontalHeaderItem(7)
        item.setText(_translate("CustomerDetailDialog", "Chiều cao"))
        item = self.customer_pet_table.horizontalHeaderItem(8)
        item.setText(_translate("CustomerDetailDialog", "Chiều dài"))
        item = self.customer_pet_table.horizontalHeaderItem(9)
        item.setText(_translate("CustomerDetailDialog", "Mô tả"))
        self.label_8.setText(_translate("CustomerDetailDialog", "Chi phí"))
        item = self.customer_expense_table.horizontalHeaderItem(0)
        item.setText(_translate("CustomerDetailDialog", "STT"))
        item = self.customer_expense_table.horizontalHeaderItem(1)
        item.setText(_translate("CustomerDetailDialog", "Hoạt động"))
        item = self.customer_expense_table.horizontalHeaderItem(2)
        item.setText(_translate("CustomerDetailDialog", "Ngày phát sinh"))
        item = self.customer_expense_table.horizontalHeaderItem(3)
        item.setText(_translate("CustomerDetailDialog", "Chi phí"))
        item = self.customer_expense_table.horizontalHeaderItem(4)
        item.setText(_translate("CustomerDetailDialog", "Chi tiết"))
        self.label_9.setText(_translate("CustomerDetailDialog", "Lịch hẹn"))
        item = self.customer_appointment_table.horizontalHeaderItem(0)
        item.setText(_translate("CustomerDetailDialog", "STT"))
        item = self.customer_appointment_table.horizontalHeaderItem(1)
        item.setText(_translate("CustomerDetailDialog", "Ngày hẹn"))
        item = self.customer_appointment_table.horizontalHeaderItem(2)
        item.setText(_translate("CustomerDetailDialog", "Mục đích"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomerDetailDialog = QtWidgets.QDialog()
    ui = Ui_CustomerDetailDialog()
    ui.setupUi(CustomerDetailDialog)
    CustomerDetailDialog.show()
    sys.exit(app.exec())
