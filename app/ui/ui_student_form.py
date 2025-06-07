# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_form.ui'
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

class Ui_Student(object):
    def setupUi(self, Student):
        if not Student.objectName():
            Student.setObjectName(u"Student")
        Student.resize(944, 201)
        Student.setMinimumSize(QSize(934, 171))
        Student.setMaximumSize(QSize(16777215, 16777215))
        Student.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"border-radius: 10px;\n"
"margin:5px")
        self.widget = QWidget(Student)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 190))
        self.widget.setMinimumSize(QSize(800, 190))
        self.widget.setMaximumSize(QSize(1980, 190))
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"background-color: rgba(0, 85, 255, 55);\n"
"border-radius: 10px;\n"
"margin:5px")
        self.Fil_name = QLabel(self.widget)
        self.Fil_name.setObjectName(u"Fil_name")
        self.Fil_name.setGeometry(QRect(30, 20, 481, 91))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.Fil_name.setFont(font1)
        self.Fil_name.setStyleSheet(u"background-color: none;")
        self.Fil_name.setTextFormat(Qt.TextFormat.AutoText)
        self.Fil_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.Fil_name.setWordWrap(True)
        self.Date = QLabel(self.widget)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(QRect(530, 100, 191, 51))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(True)
        self.Date.setFont(font2)
        self.Date.setStyleSheet(u"background-color: none;")
        self.File_author = QLabel(self.widget)
        self.File_author.setObjectName(u"File_author")
        self.File_author.setGeometry(QRect(30, 100, 421, 51))
        self.File_author.setFont(font2)
        self.File_author.setStyleSheet(u"background-color: none;")
        self.File_author.setWordWrap(True)
        self.Extensions = QLabel(self.widget)
        self.Extensions.setObjectName(u"Extensions")
        self.Extensions.setGeometry(QRect(540, 20, 191, 51))
        self.Extensions.setFont(font2)
        self.Extensions.setStyleSheet(u"background-color: none;")
        self.Extensions.setWordWrap(True)

        self.retranslateUi(Student)

        QMetaObject.connectSlotsByName(Student)
    # setupUi

    def retranslateUi(self, Student):
        Student.setWindowTitle(QCoreApplication.translate("Student", u"Widget", None))
        self.Fil_name.setText(QCoreApplication.translate("Student", u"<html><head/><body><p align=\"justify\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 </p></body></html>", None))
        self.Date.setText("")
        self.File_author.setText(QCoreApplication.translate("Student", u"\u0410\u0432\u0442\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.Extensions.setText(QCoreApplication.translate("Student", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u044f :", None))
    # retranslateUi

