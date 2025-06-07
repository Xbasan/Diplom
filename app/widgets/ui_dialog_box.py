# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_box.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_dialog_box(object):
    def setupUi(self, dialog_box):
        if not dialog_box.objectName():
            dialog_box.setObjectName(u"dialog_box")
        dialog_box.resize(510, 520)
        dialog_box.setMinimumSize(QSize(510, 520))
        dialog_box.setMaximumSize(QSize(510, 520))
        dialog_box.setStyleSheet(u"")
        self.widget = QWidget(dialog_box)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 510, 520))
        self.widget.setMinimumSize(QSize(510, 520))
        self.widget.setMaximumSize(QSize(510, 520))
        font = QFont()
        font.setFamilies([u"URW Gothic [urw]"])
        font.setPointSize(12)
        font.setBold(True)
        self.widget.setFont(font)
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:2px;\n"
"background-color: rgba(30, 85, 255, 55);")
        self.open_file = QPushButton(self.widget)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setGeometry(QRect(350, 130, 61, 51))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(True)
        self.open_file.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.open_file.setIcon(icon)
        self.open_file.setIconSize(QSize(30, 30))
        self.pathEdit = QTextEdit(self.widget)
        self.pathEdit.setObjectName(u"pathEdit")
        self.pathEdit.setGeometry(QRect(80, 130, 271, 51))
        font2 = QFont()
        font2.setFamilies([u"URW Gothic [UKWN]"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.pathEdit.setFont(font2)
        self.pathEdit.setStyleSheet(u"background-color: none;\n"
"")
        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(80, 320, 131, 61))
        font3 = QFont()
        font3.setFamilies([u"URW Gothic [urw]"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.saveButton.setFont(font3)
        self.save_pdf_btn = QPushButton(self.widget)
        self.save_pdf_btn.setObjectName(u"save_pdf_btn")
        self.save_pdf_btn.setGeometry(QRect(250, 320, 161, 61))
        self.save_pdf_btn.setFont(font3)

        self.retranslateUi(dialog_box)

        QMetaObject.connectSlotsByName(dialog_box)
    # setupUi

    def retranslateUi(self, dialog_box):
        dialog_box.setWindowTitle(QCoreApplication.translate("dialog_box", u"Widget", None))
#if QT_CONFIG(whatsthis)
        self.widget.setWhatsThis(QCoreApplication.translate("dialog_box", u"<html><head/><body><p>dsf</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.open_file.setToolTip(QCoreApplication.translate("dialog_box", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:16pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal; color:#000000;\">\u0412\u044b\u0431\u043e\u0440 \u043f\u0430\u043f\u043a\u0438</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_file.setText("")
#if QT_CONFIG(tooltip)
        self.pathEdit.setToolTip(QCoreApplication.translate("dialog_box", u"<html><head/><body><p>sdfsd</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pathEdit.setWhatsThis(QCoreApplication.translate("dialog_box", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pathEdit.setPlaceholderText(QCoreApplication.translate("dialog_box", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.saveButton.setText(QCoreApplication.translate("dialog_box", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.save_pdf_btn.setText(QCoreApplication.translate("dialog_box", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c PDF", None))
    # retranslateUi

