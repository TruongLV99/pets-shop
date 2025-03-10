# Form implementation generated from reading ui file 'add_health.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddHealthDialog(object):
    def setupUi(self, AddHealthDialog):
        AddHealthDialog.setObjectName("AddHealthDialog")
        AddHealthDialog.resize(327, 374)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddHealthDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(parent=AddHealthDialog)
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
        self.categoryLabel_2 = QtWidgets.QLabel(parent=AddHealthDialog)
        self.categoryLabel_2.setObjectName("categoryLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.categoryLabel_2)
        self.vaccine_name = QtWidgets.QLineEdit(parent=AddHealthDialog)
        self.vaccine_name.setObjectName("vaccine_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.vaccine_name)
        self.dateLabel = QtWidgets.QLabel(parent=AddHealthDialog)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dateLabel)
        self.vaccination_date = QtWidgets.QDateEdit(parent=AddHealthDialog)
        self.vaccination_date.setCalendarPopup(True)
        self.vaccination_date.setObjectName("vaccination_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.vaccination_date)
        self.amountLabel = QtWidgets.QLabel(parent=AddHealthDialog)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.amountLabel)
        self.detailsLabel = QtWidgets.QLabel(parent=AddHealthDialog)
        self.detailsLabel.setObjectName("detailsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.detailsLabel)
        self.health_condition = QtWidgets.QTextEdit(parent=AddHealthDialog)
        self.health_condition.setObjectName("health_condition")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.health_condition)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_add_health = QtWidgets.QPushButton(parent=AddHealthDialog)
        self.btn_add_health.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_add_health.setStyleSheet("QPushButton {\n"
"    background-color: #2ecc71;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.btn_add_health.setObjectName("btn_add_health")
        self.horizontalLayout_3.addWidget(self.btn_add_health)
        self.btn_cancel = QtWidgets.QPushButton(parent=AddHealthDialog)
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
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)
        self.health_check_date = QtWidgets.QDateEdit(parent=AddHealthDialog)
        self.health_check_date.setCalendarPopup(True)
        self.health_check_date.setObjectName("health_check_date")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.health_check_date)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(AddHealthDialog)
        QtCore.QMetaObject.connectSlotsByName(AddHealthDialog)

    def retranslateUi(self, AddHealthDialog):
        _translate = QtCore.QCoreApplication.translate
        AddHealthDialog.setWindowTitle(_translate("AddHealthDialog", "Thêm chăm sóc sức khỏe"))
        self.titleLabel.setText(_translate("AddHealthDialog", "Thêm chăm sóc sức khỏe"))
        self.categoryLabel_2.setText(_translate("AddHealthDialog", "Loại vắc xin:"))
        self.vaccine_name.setPlaceholderText(_translate("AddHealthDialog", "Nhập loại vắc xin"))
        self.dateLabel.setText(_translate("AddHealthDialog", "Ngày tiêm:"))
        self.vaccination_date.setDisplayFormat(_translate("AddHealthDialog", "dd/MM/yyyy"))
        self.amountLabel.setText(_translate("AddHealthDialog", "Ngày khám:"))
        self.detailsLabel.setText(_translate("AddHealthDialog", "Tình trạng:"))
        self.health_condition.setPlaceholderText(_translate("AddHealthDialog", "Nhập tình trạng..."))
        self.btn_add_health.setText(_translate("AddHealthDialog", "Thêm"))
        self.btn_cancel.setText(_translate("AddHealthDialog", "Hủy"))
        self.health_check_date.setDisplayFormat(_translate("AddHealthDialog", "dd/MM/yyyy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddHealthDialog = QtWidgets.QDialog()
    ui = Ui_AddHealthDialog()
    ui.setupUi(AddHealthDialog)
    AddHealthDialog.show()
    sys.exit(app.exec())
