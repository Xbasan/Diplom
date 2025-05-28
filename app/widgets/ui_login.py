# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Loging(object):
    def setupUi(self, Loging):
        if not Loging.objectName():
            Loging.setObjectName(u"Loging")
        Loging.resize(466, 456)
        Loging.setStyleSheet(u"border-radius:30px;\n"
"background-color: rgb(52, 167, 255);")
        self.login = QLineEdit(Loging)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(70, 150, 321, 61))
        font = QFont()
        font.setFamilies([u"URW Gothic [UKWN]"])
        font.setPointSize(16)
        font.setItalic(False)
        self.login.setFont(font)
        self.login.setStyleSheet(u"background-color: rgb(62, 167, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius:16px;\n"
"padding:16px;")
        self.password = QLineEdit(Loging)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(70, 240, 321, 61))
        font1 = QFont()
        font1.setFamilies([u"URW Gothic [UKWN]"])
        font1.setPointSize(16)
        self.password.setFont(font1)
        self.password.setStyleSheet(u"background-color: rgb(62, 167, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius:16px;\n"
"padding:16px;")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(Loging)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 330, 131, 61))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setItalic(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(92, 167, 255);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: blue;\n"
"border-radius:20px;\n"
"padding:16px;")
        self.label = QLabel(Loging)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 381, 81))
        self.label.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 12pt \"URW Gothic [UKWN]\";\n"
"")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)
        self.show_password = QPushButton(Loging)
        self.show_password.setObjectName(u"show_password")
        self.show_password.setGeometry(QRect(330, 250, 41, 41))
        self.show_password.setStyleSheet(u"border-radius:16px;\n"
"background-color: none;;")
        self.show_password.setIconSize(QSize(32, 32))
        self.audentifaceit_errorLabel = QLabel(Loging)
        self.audentifaceit_errorLabel.setObjectName(u"audentifaceit_errorLabel")
        self.audentifaceit_errorLabel.setGeometry(QRect(70, 120, 321, 18))
        self.audentifaceit_errorLabel.setStyleSheet(u"color: rgb(52, 167, 255);")

        self.retranslateUi(Loging)

        QMetaObject.connectSlotsByName(Loging)
    # setupUi

    def retranslateUi(self, Loging):
        Loging.setWindowTitle(QCoreApplication.translate("Loging", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e \u043e\u0431\u043e\u0440\u043e\u0442\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Loging", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Loging", u"<html><head/><body><p>\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u043e\u0431\u043e\u0440\u043e\u0442\u0430 \u0434\u043b\u044f</p><p>\u0413\u0411\u041f\u041e\u0423 \u00ab\u0413\u0440\u043e\u0437\u043d\u0435\u043d\u0441\u043a\u0438\u0439 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u043b\u043b\u0435\u0434\u0436 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439\u00bb</p></body></html>", None))
        self.show_password.setText("")
        self.audentifaceit_errorLabel.setText(QCoreApplication.translate("Loging", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b", None))
    # retranslateUi

