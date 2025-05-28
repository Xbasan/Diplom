# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'templates.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Templates(object):
    def setupUi(self, Templates):
        if not Templates.objectName():
            Templates.setObjectName(u"Templates")
        Templates.resize(1400, 863)
        self.scrollArea = QScrollArea(Templates)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1021, 870))
        self.scrollArea.setMaximumSize(QSize(1021, 16777215))
        self.scrollArea.setStyleSheet(u"/* \u0412 QSS-\u0444\u0430\u0439\u043b\u0435 \u0438\u043b\u0438 \u0441\u0442\u0440\u043e\u043a\u0435 */\n"
"QScrollArea {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u043b\u043e\u0441\u0430 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
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
"\n"
"/* \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u043b\u043e\u0441\u0430 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar:horizontal {\n"
"    height: 10px;\n"
"    background: #2c2c2c;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #606060;\n"
"    border-radius: 5px;"
                        "\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1021, 870))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.nameTextEdit = QTextEdit(Templates)
        self.nameTextEdit.setObjectName(u"nameTextEdit")
        self.nameTextEdit.setGeometry(QRect(1040, 80, 341, 70))
        self.nameTextEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        self.pushButtoName = QPushButton(Templates)
        self.pushButtoName.setObjectName(u"pushButtoName")
        self.pushButtoName.setGeometry(QRect(1140, 170, 121, 41))
        font = QFont()
        font.setFamilies([u"URW Gothic [UKWN]"])
        font.setPointSize(12)
        self.pushButtoName.setFont(font)
        self.pushButtoName.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.pushButtoName.setIcon(icon)
        self.pushButton_2 = QPushButton(Templates)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1060, 750, 80, 80))
        self.pushButton_2.setStyleSheet(u"border-radius: 40;\n"
"background-color: rgba(0, 85, 255, 55);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(48, 48))
        self.update = QPushButton(Templates)
        self.update.setObjectName(u"update")
        self.update.setGeometry(QRect(1030, 10, 52, 52))
        self.update.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"border-radius: 26;")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.update.setIcon(icon2)
        self.update.setIconSize(QSize(32, 32))

        self.retranslateUi(Templates)

        QMetaObject.connectSlotsByName(Templates)
    # setupUi

    def retranslateUi(self, Templates):
        Templates.setWindowTitle(QCoreApplication.translate("Templates", u"Widget", None))
        self.pushButtoName.setText(QCoreApplication.translate("Templates", u" \u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_2.setText("")
        self.update.setText("")
    # retranslateUi

