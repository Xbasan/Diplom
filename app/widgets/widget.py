# This Python file uses the following encoding: utf-8
import os
import sys
import subprocess
import re

from PySide6.QtCore import QDate
from PySide6.QtGui import (
    Qt,
    QDropEvent,
    QIcon,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QDialog,
    QLabel
)

#     pyside6-uic form.ui -o ui_form.py,

from widgets.ui_form import Ui_Documents
from widgets.ui_templates import Ui_Templates
from widgets.ui_users import Ui_Users
from widgets.ui_student_form import Ui_Student
from widgets.ui_main import Ui_Main
from widgets.ui_dialog_box import Ui_dialog_box
from widgets.ui_create_box import Ui_Create_cart
from widgets.ui_user_blok import Ui_User
from widgets.ui_dialog_remove import Ui_Remove_box
from widgets.ui_defolt import Ui_Defolt
from widgets.reference import help_text

from database.db import (
        Documents,
        UserS,
        Templates
    )

PATH_SAVE = "Downloads"


class CreateCart(QDialog, Ui_Create_cart):
    def __init__(self, file_type: str):
        super().__init__()
        self.setupUi(self)

        self.file_type = file_type
        self.widget.setAcceptDrops(True)
        self.widget.dragEnterEvent = self.dragEnterEvent
        self.widget.dropEvent = self.dropEvent
        self.saveButton.clicked.connect(self.savePressEvent)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        files = event.mimeData().urls()
        for file_url in files:
            file_parh = file_url.toLocalFile()

            self.File_name.setText(
                                   re.search(r"([^/]+\.[^.]+)$",
                                             file_parh).group(1)
                               )
            self.File_path.setText(file_parh)

    def savePressEvent(self, event):
        title = self.File_name.toPlainText()
        file_path = self.File_path.toPlainText()

        with open(file_path, "rb") as fl:
            content = fl.read()

        if self.file_type == "doxc":
            docs = Documents()
            docs.create_documents(title, content, User_id)
        elif self.file_type == "temp":
            temp = Templates()
            temp.create_templates(title, content, User_id)
        self.accept()


class SaveMenu(QDialog, Ui_dialog_box):
    """
        Окно для скачивания файлов
    """

    def __init__(self, document_id=None):
        super().__init__()
        self.setupUi(self)
        docs = Documents()
        self.document = docs.get_documents_by_id(document_id)
        self.content = self.document[0]["content"]

        self.downloads_path = os.path.join(os.path.expanduser("~"), PATH_SAVE)
        self.saveButton.clicked.connect(self.savePressEvent)

        path = self._file_saving(self.downloads_path,
                                 self.document[0]["title"])
        self.pathEdit.setText(path)

    def savePressEvent(self, event):
        path = self._file_saving(self.downloads_path,
                                 self.document[0]["title"])
        try:
            with open(path, "wb") as f:
                f.write(self.content)
            os.startfile(path)
        except AttributeError:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])
        self.accept()

    def _file_saving(self, path, title):
        name, ext = os.path.splitext(title)
        id = 0
        while True:
            if id == 0:
                new_title = f"{title}"
            else:
                new_title = f"{name}({id}){ext}"

            fill_path = os.path.join(path, new_title)
            if not os.path.isfile(fill_path):
                return fill_path
            id += 1


class SaveMenuTemp(QDialog, Ui_dialog_box):
    """
        Окно для скачивания файлов
    """

    def __init__(self, temp_id=None):
        super().__init__()
        self.setupUi(self)
        temp = Templates()
        self.document = temp.get_templates_by_id(temp_id)
        self.content = self.document[0]["content"]

        self.downloads_path = os.path.join(os.path.expanduser("~"), PATH_SAVE)
        self.saveButton.clicked.connect(self.savePressEvent)

        path = self._file_saving(self.downloads_path, self.document[0]["name"])
        self.pathEdit.setText(path)

    def savePressEvent(self, event):
        path = self._file_saving(self.downloads_path, self.document[0]["name"])
        try:
            with open(path, "wb") as f:
                f.write(self.content)
            os.startfile(path)
        except AttributeError:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])
        self.accept()

    def _file_saving(self, path, title):
        name, ext = os.path.splitext(title)
        id = 0
        while True:
            if id == 0:
                new_title = f"{title}"
            else:
                new_title = f"{name}({id}){ext}"

            fill_path = os.path.join(path, new_title)
            if not os.path.isfile(fill_path):
                return fill_path
            id += 1


class MesangeDellete(QDialog, Ui_Remove_box):
    def __init__(self, document_name):
        super().__init__()
        self.setupUi(self)
        self.file_name.setText(document_name)
        self.yesButton.clicked.connect(self.Press_yes)
        self.nowButton.clicked.connect(self.Press_now)

    def Press_yes(self, event):
        self.accept()

    def Press_now(self, event):
        self.reject()


class CartFile(QWidget, Ui_Student):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.document_id = None
        self.user_id = None
        self.widget.setMouseTracking(True)
        self.widget.mousePressEvent = self.mousePressEvent

        self.dialog = None

    def mousePressEvent(self, event):
        name = self.Fil_name.text()
        if event.button() == Qt.LeftButton:
            if self.dialog is None:
                self.dialog = SaveMenu(document_id=self.document_id)
                self.dialog.setWindowTitle(f'Скачать файл ({name})')
            self.dialog.exec()
        elif event.button() == Qt.RightButton:
            if int(User_id) == int(self.user_id):
                if self.dialog is None:
                    self.dialog = MesangeDellete(name)
                    self.dialog.setWindowTitle("Удалить ({name})")
                if self.dialog.exec() == QDialog.Accepted:
                    Documents().remove_delite_by_id(self.document_id)
                else:
                    pass
        self.dialog = None
        super().mousePressEvent(event)


class CartFileTemp(QWidget, Ui_Student):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.temp_id = None
        self.user_id = None
        self.widget.setMouseTracking(True)
        self.widget.mousePressEvent = self.mousePressEvent

        self.dialog = None

    def mousePressEvent(self, event):
        name = self.Fil_name.text()
        if event.button() == Qt.LeftButton:
            if self.dialog is None:
                self.dialog = SaveMenuTemp(temp_id=self.temp_id)
                self.dialog.setWindowTitle(f'Скачать файл ({name})')
            self.dialog.exec()
        elif event.button() == Qt.RightButton:
            if int(User_id) == int(self.user_id):
                if self.dialog is None:
                    self.dialog = MesangeDellete(name)
                    self.dialog.setWindowTitle("Удалить ({name})")
                if self.dialog.exec() == QDialog.Accepted:
                    Templates().get_templates_remove_by_id(self.temp_id)
                else:
                    pass
        self.dialog = None
        super().mousePressEvent(event)


class CartUser(QWidget, Ui_User):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class DefoltCart(QWidget, Ui_Defolt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class User_wid(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Users()
        self.ui.setupUi(self)
        self.ui.createButton.clicked.connect(self.create_user_press)

        self.users_db = UserS()
        user_list = self.users_db.get_users()

        self._print_user_list(user_list)

    def create_user_press(self, event):
        login = str(self.ui.LoginTextEdit.toPlainText())
        password = str(self.ui.PasswordTextEdit.toPlainText())
        name = str(self.ui.nameTextEdit.toPlainText())
        role = str(self.ui.comboBox.currentText()).lower()
        # role_index = str(self.ui.comboBox.currentIndex())
        if (
            all([login, password, name]) and
            User_role == "admin"
        ):
            self.users_db.create_user(login, password, name, role)
            self._print_user_list(user_list=self.users_db.get_users())
            # print(role_index)

    def _print_user_list(self, user_list=None):
        content_widget = QWidget()
        bl = QVBoxLayout(content_widget)

        for use in user_list:
            sq = CartUser()
            sq.user_name.setText(use[3])
            sq.user_login.setText(str(use[1]))
            sq.user_password.setText(str(use[2]))
            sq.user_prava.setText(str(use[4]))
            bl.addWidget(sq.widget)

        bl.setSpacing(5)

        self.ui.scrollArea.setWidget(content_widget)


class Templates_wid(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Templates()
        self.ui.setupUi(self)
        self.create_cart = None
        self.ui.pushButton_2.setIcon(QIcon("static/icon/create_document.svg"))
        self.ui.update.setIcon(QIcon("static/icon/updaet.svg"))
        self.ui.pushButtoName.setIcon(QIcon("static/icon/lupa.svg"))
        self.ui.pushButton_2.clicked.connect(self.createPressEvent)
        self.ui.pushButtoName.clicked.connect(self.namePressEvent)
        self.temp = Templates()
        temp_list = self.temp.get_templates()
        self._output_list_temp(temp_list)

    def namePressEvent(self, event):
        temp_name = self.ui.nameTextEdit.toPlainText()
        temp_list = self.temp.get_templates_by_name(temp_name)
        self._output_list_temp(temp_list)

    def _temp_print(self):
        temp_list = self.temp.get_templates()
        self._output_list_temp(temp_list)

    def _output_list_temp(self, temp_list=None):
        if temp_list is None:
            temp_list = self.temp.get_templates()
        content_widget = QWidget()
        bl = QVBoxLayout(content_widget)

        if temp_list == []:
            sq = DefoltCart()
            bl.addWidget(sq.widget)

        for doc in temp_list:
            file_name = re.sub(r'\.[^\.]*$', '', doc[1])
            extensi = doc[1].split(".")[-1]
            us = UserS()
            auter = str(us.get_username_by_id(doc[3]))

            sq = CartFileTemp()
            sq.temp_id = doc[0]
            sq.user_id = doc[3]
            sq.Fil_name.setText(file_name)
            sq.Extensions.setText(extensi)
            sq.File_author.setText(auter)

            bl.addWidget(sq.widget)

        bl.setSpacing(5)
        self.ui.scrollArea.setWidget(content_widget)

    def createPressEvent(self, event):
        if self.create_cart is None:
            self.create_cart = 1
            self.dialog = CreateCart(file_type="temp")
            self.dialog.setWindowTitle("Новый шаблон")
            self.dialog.finished.connect(self._temp_print)
        self.dialog.exec()


class Documents_wid(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.create_cart = None
        self.ui = Ui_Documents()
        self.ui.setupUi(self)
        self.docs = Documents()

        docs_list = self.docs.get_documents()

        self._output_list_documents(docs_list)

        self.ui.createButton.setIcon(QIcon("static/icon/create_document.svg"))
        self.ui.update.setIcon(QIcon("static/icon/updaet.svg"))
        self.ui.NameButton.setIcon(QIcon("static/icon/lupa.svg"))
        self.ui.FileButton.setIcon(QIcon("static/icon/lupa.svg"))
        self.ui.DataButton.setIcon(QIcon("static/icon/lupa.svg"))
        self.ui.dateEdit.setDate(QDate.fromString("22.05.2025", "dd.MM.yyyy"))
        self.ui.NameButton.clicked.connect(self.namePressEvent)
        self.ui.FileButton.clicked.connect(self.fileNamePressEvent)
        self.ui.update.clicked.connect(self._update_document_list)
        self.ui.createButton.clicked.connect(self.createPressEvent)
        self.ui.DataButton.clicked.connect(self.dataPressEvent)

    def namePressEvent(self, event):
        user = self.ui.nameTextEdit.toPlainText()
        docs_list = self.docs.get_documents_by_username(user)
        self._output_list_documents(docs_list)

    def createPressEvent(self, event):
        if self.create_cart is None:
            self.create_cart = 1
            self.dialog = CreateCart(file_type="doxc")
            self.dialog.setWindowTitle("новый документ")
            self.dialog.finished.connect(self._update_document_list)

        self.dialog.exec()

    def dataPressEvent(self, event):
        data = self.ui.dateEdit.text()
        self._output_list_documents(self.docs.get_documests_date(data))

    def _update_document_list(self):
        docs_list = self.docs.get_documents()
        self._output_list_documents(docs_list)

    def fileNamePressEvent(self, event):
        file_name = self.ui.FileTextEdit.toPlainText()
        docs_list = self.docs.get_documents_by_title(file_name)

        self._output_list_documents(docs_list)

    def _output_list_documents(self, documents_list=None):
        """
            Выводит список документов
        """
        if documents_list is None:
            documents_list = self.docs.get_documents()
        content_widget = QWidget()
        bl = QVBoxLayout(content_widget)

        if documents_list == []:
            sq = DefoltCart()
            bl.addWidget(sq.widget)

        for doc in documents_list:

            file_id = doc[0]
            file_name = re.sub(r'\.[^\.]*$', '', doc[1])
            extensi = doc[1].split(".")[-1]
            us = UserS()
            auter = str(us.get_username_by_id(doc[3]))

            sq = CartFile()
            sq.user_id = doc[3]
            sq.document_id = file_id
            sq.Fil_name.setText(file_name)
            sq.Extensions.setText(extensi)
            sq.Date.setText(doc[4])
            sq.File_author.setText(auter)

            bl.addWidget(sq.widget)

        bl.setSpacing(5)

        self.ui.scrollArea.setWidget(content_widget)


class Widget(QWidget):
    def __init__(self, users, parent=None):
        super().__init__(parent)

        self.ui = Ui_Main()
        self.ui.setupUi(self)

        ref_labal = QLabel()
        ref_labal.setText(help_text)
        ref_labal.setWordWrap(True)
        ref_labal.setTextFormat(Qt.TextFormat.RichText)
        cont = QWidget()

        layout = QVBoxLayout(cont)
        layout.addWidget(ref_labal)
        self.ui.scrollArea.setWidget(cont)
        self.ui.scrollArea.setWidgetResizable(True)

        self.setWindowIcon(QIcon("static/icon/ggkit.ico"))
        global User_id
        User_id = list(users.keys())[0]
        global User_role
        User_role = users[User_id]
        self.ui.tabWidget.insertTab(0, Documents_wid(), "Документы")
        self.ui.tabWidget.insertTab(1, Templates_wid(), "Шаблонны")
        if User_role == "admin":
            self.ui.tabWidget.insertTab(2, User_wid(), "Пользователи")
        self.ui.tabWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
