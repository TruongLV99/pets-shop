import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6 import QtWidgets
from views.main_window_ui import Ui_MainWindow
from db.db_connection import execute_query

class MainWindowController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)