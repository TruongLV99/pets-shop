import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication

from login_window import LoginWindow
# from main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    with open("resources/styles.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)

    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()