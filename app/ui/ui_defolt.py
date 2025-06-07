# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defolt.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Defolt(object):
    def setupUi(self, Defolt):
        if not Defolt.objectName():
            Defolt.setObjectName(u"Defolt")
        Defolt.resize(1124, 409)
        Defolt.setMinimumSize(QSize(934, 171))
        Defolt.setMaximumSize(QSize(16777215, 16777215))
        Defolt.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"border-radius: 10px;\n"
"margin:5px")
        self.widget = QWidget(Defolt)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 100, 801, 190))
        self.widget.setMinimumSize(QSize(800, 190))
        self.widget.setMaximumSize(QSize(1980, 190))
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"background-color: rgba(0, 85, 255, 0);\n"
"border-radius: 10px;\n"
"margin:5px")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 491, 111))
        font1 = QFont()
        font1.setFamilies([u"PT Sans Caption"])
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.retranslateUi(Defolt)

        QMetaObject.connectSlotsByName(Defolt)
    # setupUi

    def retranslateUi(self, Defolt):
        Defolt.setWindowTitle(QCoreApplication.translate("Defolt", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Defolt", u"\u041f\u043e \u0432\u0430\u0448\u0435\u043c\u0443 \u0437\u0430\u043f\u0440\u043e\u0441\u0443 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e \n"
"\u043f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0440\u043e\u0441", None))
    # retranslateUi

