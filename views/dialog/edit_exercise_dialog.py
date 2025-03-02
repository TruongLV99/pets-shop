import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.edit_exercise import Ui_EditExerciseDialog
from PyQt6.QtCore import QTime

class EditExerciseDialog(QDialog, Ui_EditExerciseDialog):
    def __init__(self, parent=None, exercise=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.exercise = exercise

        self.btn_edit_exercise.clicked.connect(self.updated_data)
        self.btn_cancel.clicked.connect(self.closeEvt)

        if exercise:
            exercise_time = exercise['exercise_time']
            total_seconds = exercise_time.total_seconds()

            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            seconds = int(total_seconds % 60)

            qtime_value = QTime(hours, minutes, seconds)

            self.activity_type.setText(exercise['activity_type'])
            self.exercise_date.setDate(exercise['exercise_date'])
            self.exercise_time.setTime(qtime_value)
            self.duration.setText(exercise['duration'])

    def updated_data(self):
        updated_data = {
            "id": self.exercise['id'],
            "activity_type": self.activity_type.text(),
            "exercise_date": self.exercise_date.date().toString("yyyy-MM-dd"),
            "exercise_time": self.exercise_time.time().toString("HH:mm:ss"),
            "duration": self.duration.text(),
        }

        if self.parent:
            self.close()
            self.parent.update_exercise(updated_data)

    def closeEvt(self):
        self.close()
