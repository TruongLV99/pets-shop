# Form implementation generated from reading ui file 'edit_exercise.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditExerciseDialog(object):
    def setupUi(self, EditExerciseDialog):
        EditExerciseDialog.setObjectName("EditExerciseDialog")
        EditExerciseDialog.resize(330, 206)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditExerciseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(parent=EditExerciseDialog)
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
        self.categoryLabel_2 = QtWidgets.QLabel(parent=EditExerciseDialog)
        self.categoryLabel_2.setObjectName("categoryLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.categoryLabel_2)
        self.activity_type = QtWidgets.QLineEdit(parent=EditExerciseDialog)
        self.activity_type.setObjectName("activity_type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activity_type)
        self.dateLabel = QtWidgets.QLabel(parent=EditExerciseDialog)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dateLabel)
        self.exercise_date = QtWidgets.QDateEdit(parent=EditExerciseDialog)
        self.exercise_date.setCalendarPopup(True)
        self.exercise_date.setObjectName("exercise_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.exercise_date)
        self.amountLabel = QtWidgets.QLabel(parent=EditExerciseDialog)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.amountLabel)
        self.duration = QtWidgets.QLineEdit(parent=EditExerciseDialog)
        self.duration.setObjectName("duration")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.duration)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_edit_exercise = QtWidgets.QPushButton(parent=EditExerciseDialog)
        self.btn_edit_exercise.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_edit_exercise.setStyleSheet("QPushButton {\n"
"    background-color: #2ecc71;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.btn_edit_exercise.setObjectName("btn_edit_exercise")
        self.horizontalLayout_3.addWidget(self.btn_edit_exercise)
        self.btn_cancel = QtWidgets.QPushButton(parent=EditExerciseDialog)
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
        self.timeLabel = QtWidgets.QLabel(parent=EditExerciseDialog)
        self.timeLabel.setObjectName("timeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.timeLabel)
        self.exercise_time = QtWidgets.QTimeEdit(parent=EditExerciseDialog)
        self.exercise_time.setObjectName("exercise_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.exercise_time)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(EditExerciseDialog)
        QtCore.QMetaObject.connectSlotsByName(EditExerciseDialog)

    def retranslateUi(self, EditExerciseDialog):
        _translate = QtCore.QCoreApplication.translate
        EditExerciseDialog.setWindowTitle(_translate("EditExerciseDialog", "Sửa hoạt động thể chất"))
        self.titleLabel.setText(_translate("EditExerciseDialog", "Sửa hoạt động thể chất"))
        self.categoryLabel_2.setText(_translate("EditExerciseDialog", "Loại hoạt động:"))
        self.activity_type.setPlaceholderText(_translate("EditExerciseDialog", "Nhập loại hoạt động"))
        self.dateLabel.setText(_translate("EditExerciseDialog", "Ngày hoạt động:"))
        self.exercise_date.setDisplayFormat(_translate("EditExerciseDialog", "dd/MM/yyyy"))
        self.amountLabel.setText(_translate("EditExerciseDialog", "Thời gian (phút)"))
        self.duration.setPlaceholderText(_translate("EditExerciseDialog", "Nhập thời gian"))
        self.btn_edit_exercise.setText(_translate("EditExerciseDialog", "Thêm"))
        self.btn_cancel.setText(_translate("EditExerciseDialog", "Hủy"))
        self.timeLabel.setText(_translate("EditExerciseDialog", "Giờ hoạt động:"))
        self.exercise_time.setDisplayFormat(_translate("EditExerciseDialog", "hh:mm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditExerciseDialog = QtWidgets.QDialog()
    ui = Ui_EditExerciseDialog()
    ui.setupUi(EditExerciseDialog)
    EditExerciseDialog.show()
    sys.exit(app.exec())
