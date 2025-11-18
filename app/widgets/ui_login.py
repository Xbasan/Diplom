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
        Loging.resize(511, 520)
        Loging.setStyleSheet(u"")
        self.widget = QWidget(Loging)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 511, 521))
        self.widget.setStyleSheet(u"\n"
"background-color: rgba(30, 85, 255, 100);")
        self.audentifaceit_errorLabel = QLabel(self.widget)
        self.audentifaceit_errorLabel.setObjectName(u"audentifaceit_errorLabel")
        self.audentifaceit_errorLabel.setGeometry(QRect(70, 370, 351, 18))
        font = QFont()
        font.setFamilies([u"URW Gothic [UKWN]"])
        font.setPointSize(12)
        self.audentifaceit_errorLabel.setFont(font)
        self.audentifaceit_errorLabel.setStyleSheet(u"color: rgba(30, 85, 255, 0);;\n"
"background-color: None;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 451, 81))
        font1 = QFont()
        font1.setFamilies([u"URW Gothic [UKWN]"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 14pt \"URW Gothic [UKWN]\";\n"
"background-color: None;\n"
"")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)
        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(70, 300, 361, 61))
        font2 = QFont()
        font2.setFamilies([u"URW Gothic [UKWN]"])
        font2.setPointSize(16)
        self.password.setFont(font2)
        self.password.setStyleSheet(u"background-color: rgba(30, 85, 255, 55);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius:16px;\n"
"padding:16px;")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.login = QLineEdit(self.widget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(70, 190, 361, 61))
        font3 = QFont()
        font3.setFamilies([u"URW Gothic [UKWN]"])
        font3.setPointSize(16)
        font3.setItalic(False)
        self.login.setFont(font3)
        self.login.setStyleSheet(u"background-color: rgba(30, 85, 255, 55);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius:16px;\n"
"padding:16px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 410, 131, 61))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setItalic(True)
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"background-color: rgba(30, 85, 255, 55);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius:20px;\n"
"padding:16px;")
        self.show_password = QPushButton(self.widget)
        self.show_password.setObjectName(u"show_password")
        self.show_password.setGeometry(QRect(370, 310, 41, 41))
        self.show_password.setStyleSheet(u"border-radius:16px;\n"
"background-color: none;;")
        self.show_password.setIconSize(QSize(32, 32))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 160, 61, 18))
        font5 = QFont()
        font5.setFamilies([u"URW Gothic [urw]"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"background-color: None;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 270, 81, 18))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"background-color: None;")

        self.retranslateUi(Loging)

        QMetaObject.connectSlotsByName(Loging)
    # setupUi

    def retranslateUi(self, Loging):
        Loging.setWindowTitle(QCoreApplication.translate("Loging", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e \u043e\u0431\u043e\u0440\u043e\u0442\u0430", None))
        self.audentifaceit_errorLabel.setText(QCoreApplication.translate("Loging", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b", None))
        self.label.setText(QCoreApplication.translate("Loging", u"<html><head/><body><p>\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u043e\u0431\u043e\u0440\u043e\u0442\u0430 \u0434\u043b\u044f</p><p>\u0413\u0411\u041f\u041e\u0423 \u00ab\u0413\u0440\u043e\u0437\u043d\u0435\u043d\u0441\u043a\u0438\u0439 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u043b\u043b\u0435\u0434\u0436 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439\u00bb</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Loging", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.show_password.setText("")
        self.label_2.setText(QCoreApplication.translate("Loging", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("Loging", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

