# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_box.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Create_cart(object):
    def setupUi(self, Create_cart):
        if not Create_cart.objectName():
            Create_cart.setObjectName(u"Create_cart")
        Create_cart.resize(510, 520)
        Create_cart.setMinimumSize(QSize(510, 520))
        Create_cart.setMaximumSize(QSize(510, 520))
        Create_cart.setStyleSheet(u"")
        self.widget = QWidget(Create_cart)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 511, 521))
        self.widget.setMinimumSize(QSize(511, 521))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:2px;\n"
"background-color: rgba(30, 85, 255, 55);")
        self.file_vbor = QPushButton(self.widget)
        self.file_vbor.setObjectName(u"file_vbor")
        self.file_vbor.setGeometry(QRect(410, 220, 61, 51))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(True)
        self.file_vbor.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.file_vbor.setIcon(icon)
        self.file_vbor.setIconSize(QSize(30, 30))
        self.File_name = QTextEdit(self.widget)
        self.File_name.setObjectName(u"File_name")
        self.File_name.setGeometry(QRect(80, 120, 331, 51))
        self.File_name.setFont(font1)
        self.File_name.setStyleSheet(u"background-color: none;")
        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(170, 340, 161, 61))
        font2 = QFont()
        font2.setFamilies([u"Serif"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.saveButton.setFont(font2)
        self.saveButton.setIconSize(QSize(0, 0))
        self.File_path = QTextEdit(self.widget)
        self.File_path.setObjectName(u"File_path")
        self.File_path.setGeometry(QRect(80, 220, 331, 51))
        self.File_path.setFont(font1)
        self.File_path.setStyleSheet(u"background-color: none;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 90, 171, 21))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: none;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 190, 171, 21))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: none;")

        self.retranslateUi(Create_cart)

        QMetaObject.connectSlotsByName(Create_cart)
    # setupUi

    def retranslateUi(self, Create_cart):
        Create_cart.setWindowTitle(QCoreApplication.translate("Create_cart", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.file_vbor.setToolTip(QCoreApplication.translate("Create_cart", u"<html><head/><body><p><span style=\" color:#000000;\">\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.file_vbor.setText("")
        self.saveButton.setText(QCoreApplication.translate("Create_cart", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Create_cart", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0442\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Create_cart", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
    # retranslateUi

