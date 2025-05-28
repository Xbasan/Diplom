# main.py
from PySide6.QtGui import QIcon
from widgets.widget import Widget


def main(user_d):
    # app = QApplication(sys.argv)
    main_windows = Widget(user_d)
    main_windows.setWindowIcon(QIcon("static/icon/ggkit.ico"))
    main_windows.setWindowTitle("Система документооборота колледжа")
    main_windows.resize(1420, 900)
    main_windows.show()
    return main_windows
    # sys.exit(app.exec())


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    main_windows = Widget({1: 'admin'})
    main_windows.setWindowTitle("Система документооборота колледжа")
    main_windows.resize(1420, 900)
    main_windows.setMaximumHeight(900)
    main_windows.setMaximumWidth(1420)
    main_windows.setMinimumSize(1420, 900)
    main_windows.show()
    sys.exit(app.exec())

