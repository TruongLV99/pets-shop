import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db_connection import DatabaseConnection
import pymysql
from PyQt6 import QtWidgets

class UserModel:
    def __init__(self):
        self.db = DatabaseConnection()
        self.cursor = self.db.connection.cursor()

    def login(self, username, password):
        QtWidgets.QMessageBox.information(self, "Login Successful", "Welcome to Pets Shop!")
        try:
            if self.connection: 
                query = "SELECT * FROM user WHERE username = %s"
                self.cursor.execute(query, (username,))
                user = self.cursor.fetchone()  # Lấy một dòng kết quả
                if user:
                    return True
                else:
                        return False  # Mật khẩu không đúng
        except pymysql.MySQLError as e:
            print(f"Đã xảy ra lỗi MySQL: {e}")
            return False
        finally:
            self.connection.close()  # Đảm bảo đóng kết nối