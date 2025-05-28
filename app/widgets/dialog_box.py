# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_remove.ui'
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
    QWidget)

class Ui_Remove_box(object):
    def setupUi(self, Remove_box):
        if not Remove_box.objectName():
            Remove_box.setObjectName(u"Remove_box")
        Remove_box.resize(510, 520)
        Remove_box.setMinimumSize(QSize(510, 520))
        Remove_box.setMaximumSize(QSize(510, 520))
        Remove_box.setStyleSheet(u"")
        self.widget = QWidget(Remove_box)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 510, 520))
        self.widget.setMinimumSize(QSize(510, 520))
        self.widget.setMaximumSize(QSize(510, 520))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"background-color: rgba(30, 85, 255, 55);\n"
"font: 400 12pt \"Noto Sans\";\n"
"border-radius: 10px;")
        self.yesButton = QPushButton(self.widget)
        self.yesButton.setObjectName(u"yesButton")
        self.yesButton.setGeometry(QRect(120, 360, 101, 51))
        self.nowButton = QPushButton(self.widget)
        self.nowButton.setObjectName(u"nowButton")
        self.nowButton.setGeometry(QRect(270, 360, 101, 51))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 120, 271, 41))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.file_name = QLabel(self.widget)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(70, 170, 371, 121))
        self.file_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.file_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.retranslateUi(Remove_box)

        QMetaObject.connectSlotsByName(Remove_box)
    # setupUi

    def retranslateUi(self, Remove_box):
        Remove_box.setWindowTitle(QCoreApplication.translate("Remove_box", u"Widget", None))
#if QT_CONFIG(whatsthis)
        self.widget.setWhatsThis(QCoreApplication.translate("Remove_box", u"<html><head/><body><p>dsf</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.yesButton.setText(QCoreApplication.translate("Remove_box", u"\u0414\u0430", None))
        self.nowButton.setText(QCoreApplication.translate("Remove_box", u"\u041d\u0435\u0442q", None))
        self.label.setText(QCoreApplication.translate("Remove_box", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b \u0447\u0442\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.file_name.setText(QCoreApplication.translate("Remove_box", u"<html><head/><body><p align=\"justify\">File name</p></body></html>", None))
    # retranslateUi

