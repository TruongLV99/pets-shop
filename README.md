// bỏ viền
LoginWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
LoginWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

//thêm event close
self.btnClose.clicked.connect(LoginWindow.close)