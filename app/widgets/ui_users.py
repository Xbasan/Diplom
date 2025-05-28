# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QPushButton, QScrollArea,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Users(object):
    def setupUi(self, Users):
        if not Users.objectName():
            Users.setObjectName(u"Users")
        Users.resize(1400, 834)
        self.scrollArea = QScrollArea(Users)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1000, 870))
        self.scrollArea.setMaximumSize(QSize(1000, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
"    background: #2c2c2c;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #606060;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height: 10px;\n"
"    background: #2c2c2c;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #606060;\n"
"    border-radius: 5px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1000, 870))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.createButton = QPushButton(Users)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(1040, 690, 100, 100))
        self.createButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createButton.setStyleSheet(u"border-radius: 50%;\n"
"background-color: rgba(0, 85, 255, 55);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.createButton.setIcon(icon)
        self.createButton.setIconSize(QSize(50, 50))
        self.nameTextEdit = QTextEdit(Users)
        self.nameTextEdit.setObjectName(u"nameTextEdit")
        self.nameTextEdit.setGeometry(QRect(1049, 60, 311, 44))
        self.nameTextEdit.setMaximumSize(QSize(320, 44))
        font = QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.nameTextEdit.setFont(font)
        self.nameTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.nameTextEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-top:5px;\n"
"padding-left:10px;")
        self.nameTextEdit.setAcceptRichText(False)
        self.LoginTextEdit = QTextEdit(Users)
        self.LoginTextEdit.setObjectName(u"LoginTextEdit")
        self.LoginTextEdit.setGeometry(QRect(1049, 130, 311, 44))
        self.LoginTextEdit.setMaximumSize(QSize(320, 44))
        self.LoginTextEdit.setFont(font)
        self.LoginTextEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-top:5px;\n"
"padding-left:10px")
        self.comboBox = QComboBox(Users)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(1050, 270, 151, 41))
        self.comboBox.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        self.PasswordTextEdit = QTextEdit(Users)
        self.PasswordTextEdit.setObjectName(u"PasswordTextEdit")
        self.PasswordTextEdit.setGeometry(QRect(1049, 200, 311, 44))
        self.PasswordTextEdit.setMaximumSize(QSize(320, 44))
        self.PasswordTextEdit.setFont(font)
        self.PasswordTextEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-top:5px;\n"
"padding-left:10px")

        self.retranslateUi(Users)

        QMetaObject.connectSlotsByName(Users)
    # setupUi

    def retranslateUi(self, Users):
        Users.setWindowTitle(QCoreApplication.translate("Users", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.createButton.setToolTip(QCoreApplication.translate("Users", u"<html><head/><body><p align=\"justify\">\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u043d\u043e\u0432\u0430\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0438\u043b\u044f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.createButton.setWhatsThis(QCoreApplication.translate("Users", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.createButton.setText("")
        self.nameTextEdit.setPlaceholderText(QCoreApplication.translate("Users", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0438\u043b\u044f", None))
#if QT_CONFIG(tooltip)
        self.LoginTextEdit.setToolTip(QCoreApplication.translate("Users", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.LoginTextEdit.setWhatsThis(QCoreApplication.translate("Users", u"<html><head/><body><p>;;</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.LoginTextEdit.setHtml(QCoreApplication.translate("Users", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:14pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.LoginTextEdit.setPlaceholderText(QCoreApplication.translate("Users", u"\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Users", u"\u0413\u043e\u0441\u0442\u044c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Users", u"Admin", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Users", u"User", None))

#if QT_CONFIG(tooltip)
        self.PasswordTextEdit.setToolTip(QCoreApplication.translate("Users", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PasswordTextEdit.setWhatsThis(QCoreApplication.translate("Users", u"<html><head/><body><p>;;</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PasswordTextEdit.setHtml(QCoreApplication.translate("Users", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:14pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.PasswordTextEdit.setPlaceholderText(QCoreApplication.translate("Users", u"\u041f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

