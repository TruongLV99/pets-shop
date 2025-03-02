import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog
from views.dialog.add_exercise import Ui_AddExerciseDialog

class AddExerciseDialog(QDialog, Ui_AddExerciseDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_add_exercise.clicked.connect(self.add_data)

    def add_data(self):
        add_data = {
            "activity_type": self.activity_type.text(),
            "exercise_date": self.exercise_date.date().toString("yyyy-MM-dd"),
            "exercise_time": self.exercise_time.time().toString("HH:mm:ss"),
            "duration": self.duration.text(),
        }

        if self.parent:
            self.close()
            self.parent.add_exercise(add_data)
