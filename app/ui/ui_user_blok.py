# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_blok.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_User(object):
    def setupUi(self, User):
        if not User.objectName():
            User.setObjectName(u"User")
        User.resize(950, 296)
        User.setMinimumSize(QSize(934, 171))
        User.setMaximumSize(QSize(16777215, 16777215))
        User.setStyleSheet(u"")
        self.widget = QWidget(User)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 801, 290))
        self.widget.setMinimumSize(QSize(800, 290))
        self.widget.setMaximumSize(QSize(1980, 290))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(14)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"font: 600 14pt \"Noto Sans\";\n"
"border-radius: 10px;\n"
"margin:5px")
        self.verticalWidget = QWidget(self.widget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(20, 20, 231, 251))
        self.verticalWidget.setStyleSheet(u"background-color: None;")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_name_1 = QLabel(self.verticalWidget)
        self.user_name_1.setObjectName(u"user_name_1")
        self.user_name_1.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout.addWidget(self.user_name_1)

        self.user_login_1 = QLabel(self.verticalWidget)
        self.user_login_1.setObjectName(u"user_login_1")
        self.user_login_1.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"")

        self.verticalLayout.addWidget(self.user_login_1)

        self.user_password_1 = QLabel(self.verticalWidget)
        self.user_password_1.setObjectName(u"user_password_1")
        self.user_password_1.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout.addWidget(self.user_password_1)

        self.user_prava_1 = QLabel(self.verticalWidget)
        self.user_prava_1.setObjectName(u"user_prava_1")
        self.user_prava_1.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout.addWidget(self.user_prava_1)

        self.verticalWidget_2 = QWidget(self.widget)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setGeometry(QRect(260, 20, 361, 251))
        self.verticalWidget_2.setStyleSheet(u"background-color: None;")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.user_name = QLabel(self.verticalWidget_2)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"")

        self.verticalLayout_2.addWidget(self.user_name)

        self.user_login = QLabel(self.verticalWidget_2)
        self.user_login.setObjectName(u"user_login")
        self.user_login.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"")

        self.verticalLayout_2.addWidget(self.user_login)

        self.user_password = QLabel(self.verticalWidget_2)
        self.user_password.setObjectName(u"user_password")
        self.user_password.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"")

        self.verticalLayout_2.addWidget(self.user_password)

        self.user_prava = QLabel(self.verticalWidget_2)
        self.user_prava.setObjectName(u"user_prava")
        self.user_prava.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);")

        self.verticalLayout_2.addWidget(self.user_prava)


        self.retranslateUi(User)

        QMetaObject.connectSlotsByName(User)
    # setupUi

    def retranslateUi(self, User):
        User.setWindowTitle(QCoreApplication.translate("User", u"Widget", None))
        self.user_name_1.setText(QCoreApplication.translate("User", u"\u0424\u0418\u041e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.user_login_1.setText(QCoreApplication.translate("User", u" \u041b\u043e\u0433\u0438\u043d", None))
        self.user_password_1.setText(QCoreApplication.translate("User", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.user_prava_1.setText(QCoreApplication.translate("User", u"\u041f\u0440\u0430\u0432\u0430", None))
        self.user_name.setText(QCoreApplication.translate("User", u"TextLabel", None))
        self.user_login.setText(QCoreApplication.translate("User", u"TextLabel", None))
        self.user_password.setText(QCoreApplication.translate("User", u"TextLabel", None))
        self.user_prava.setText(QCoreApplication.translate("User", u"TextLabel", None))
    # retranslateUi

