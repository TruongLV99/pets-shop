import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6 import QtWidgets
from views.login_ui import Ui_LoginWindow
from db.db_connection import execute_query
from controllers.main_window_controller import MainWindowController
from PyQt6.QtWidgets import QApplication

class LoginController:
    def login(username, password):
        query = "SELECT * FROM users WHERE username = %s"
        user = execute_query(query, (username))  # Lấy một dòng kết quả

        # Logic for login (This is just an example)
        if user:
            # QtWidgets.QMessageBox.information(self, "Login Successful", "Welcome to Pets Shop!")
            app = QApplication(sys.argv)
            main_window = MainWindowController()
            main_window.show()
            sys.exit(app.exec())
            # self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")