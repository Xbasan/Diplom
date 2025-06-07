# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_update.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_User_update(object):
    def setupUi(self, User_update):
        if not User_update.objectName():
            User_update.setObjectName(u"User_update")
        User_update.resize(510, 520)
        User_update.setMinimumSize(QSize(0, 0))
        User_update.setMaximumSize(QSize(16777215, 16777215))
        User_update.setStyleSheet(u"\n"
"font: 600 14pt \"Noto Sans\";\n"
"border-radius: 10px;\n"
"")
        self.widget = QWidget(User_update)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 510, 520))
        self.widget.setMinimumSize(QSize(0, 290))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(14)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"font: 600 14pt \"Noto Sans\";\n"
"")
        self.pushButtonUpdate = QPushButton(self.widget)
        self.pushButtonUpdate.setObjectName(u"pushButtonUpdate")
        self.pushButtonUpdate.setGeometry(QRect(80, 410, 151, 61))
        self.pushButtonUpdate.setFont(font)
        self.pushButtonIgnore = QPushButton(self.widget)
        self.pushButtonIgnore.setObjectName(u"pushButtonIgnore")
        self.pushButtonIgnore.setGeometry(QRect(280, 410, 141, 61))
        self.pushButtonRemove = QPushButton(self.widget)
        self.pushButtonRemove.setObjectName(u"pushButtonRemove")
        self.pushButtonRemove.setGeometry(QRect(10, 10, 121, 51))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(12)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.pushButtonRemove.setFont(font1)
        self.pushButtonRemove.setStyleSheet(u"font: 600 12pt \"Noto Sans\";")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 100, 131, 61))
        self.label.setStyleSheet(u"background-color: None;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 160, 131, 61))
        self.label_2.setStyleSheet(u"background-color: None;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 230, 131, 61))
        self.label_3.setStyleSheet(u"background-color: None;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 340, 391, 21))
        self.label_4.setStyleSheet(u"font: 400 12pt \"Noto Sans\";\n"
"color: rgba(30, 85, 255, 0);\n"
"background-color: none;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(200, 90, 281, 211))
        self.widget_2.setStyleSheet(u"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_textEdit = QLineEdit(self.widget_2)
        self.name_textEdit.setObjectName(u"name_textEdit")
        self.name_textEdit.setMinimumSize(QSize(0, 62))
        self.name_textEdit.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout.addWidget(self.name_textEdit)

        self.login_textEdit = QLineEdit(self.widget_2)
        self.login_textEdit.setObjectName(u"login_textEdit")
        self.login_textEdit.setMinimumSize(QSize(0, 62))
        self.login_textEdit.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout.addWidget(self.login_textEdit)

        self.password_textEdit = QLineEdit(self.widget_2)
        self.password_textEdit.setObjectName(u"password_textEdit")
        self.password_textEdit.setMinimumSize(QSize(0, 62))
        self.password_textEdit.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout.addWidget(self.password_textEdit)


        self.retranslateUi(User_update)

        QMetaObject.connectSlotsByName(User_update)
    # setupUi

    def retranslateUi(self, User_update):
        User_update.setWindowTitle(QCoreApplication.translate("User_update", u"Widget", None))
        self.pushButtonUpdate.setText(QCoreApplication.translate("User_update", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButtonIgnore.setText(QCoreApplication.translate("User_update", u"\u0423\u0439\u0442\u0438", None))
        self.pushButtonRemove.setText(QCoreApplication.translate("User_update", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("User_update", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("User_update", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("User_update", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("User_update", u"\u041d\u0435 \u0432\u0441\u0435 \u043f\u043e\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u044b", None))
    # retranslateUi

