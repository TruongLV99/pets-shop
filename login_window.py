import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from controllers.login_controller import LoginController
from views.login_ui import Ui_LoginWindow
from main_window import MainWindow
from db.db_connection import execute_query

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect login button to the login method
        self.btnLogin.clicked.connect(self.login)

    def login(self):
        username = self.username.text()
        password = self.password.text()

        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

        # query = "SELECT * FROM users WHERE username = %s"
        # user = execute_query(query, (username), False)

        # if user:
        #     self.main_window = MainWindow()
        #     self.main_window.show()
        #     self.close()
        # else:
        #     QMessageBox.warning(self, "Login Failed", "Tên đăng nhập hoặc mật khẩu không đúng.")