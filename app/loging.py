import sys
from widgets.ui_login import Ui_Loging
from database.db import UserS
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
)
from PySide6.QtCore import Qt
import main


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Loging()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.autoden)
        self.ui.show_password.clicked.connect(self.show_password)
        self.ui.show_password.setIcon(QIcon("static/icon/eye.svg"))
        self.setWindowIcon(QIcon("static/icon/ggkit.ico"))
        self.user = UserS()

    def autoden(self, event):
        _login = self.ui.login.text()
        _password = self.ui.password.text()
        if _login and _password:
            _loging = self.user.user_loging(_login, _password)
            if _loging != dict():
                self.main_windows = main.main(_loging)
                self.close()
            else:
                textStyle = """
                background-color: rgba(245, 40, 76, 30);
                border-style: solid;
                border-width: 2px;
                border-color: red;
                border-radius:16px;
                padding:16px;
                """
                self.ui.login.setStyleSheet(textStyle)
                self.ui.password.setStyleSheet(textStyle)
                self.ui.audentifaceit_errorLabel.setStyleSheet("color:red;")

    def show_password(self, event):
        if self.ui.password.echoMode().value == 2:
            self.ui.password.setEchoMode(QLineEdit.Normal)
            self.ui.show_password.setIcon(QIcon("static/icon/eye-off.svg"))
        elif self.ui.password.echoMode().value == 0:
            self.ui.password.setEchoMode(QLineEdit.Password)
            self.ui.show_password.setIcon(QIcon("static/icon/eye.svg"))

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            if self.ui.login.hasFocus():
                self.ui.password.setFocus()
            elif self.ui.password.hasFocus():
                self.ui.pushButton.click()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/icon/ggkit.ico"))
    widget = Widget()
    widget.setWindowIcon(QIcon("static/icon/ggkit.ico"))
    widget.show()
    sys.exit(app.exec())
