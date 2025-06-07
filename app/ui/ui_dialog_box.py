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
        self.widget.setStyleSheet(u"background-color: rgba(30, 85, 255, 55);")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 130, 61, 51))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(True)
        self.pushButton.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pathEdit = QTextEdit(self.widget)
        self.pathEdit.setObjectName(u"pathEdit")
        self.pathEdit.setGeometry(QRect(80, 130, 271, 51))
        self.pathEdit.setFont(font1)
        self.pathEdit.setStyleSheet(u"background-color: none;\n"
"")
        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(80, 320, 131, 61))
        font2 = QFont()
        font2.setFamilies([u"URW Gothic [urw]"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.saveButton.setFont(font2)
        self.save_pdf_btn = QPushButton(self.widget)
        self.save_pdf_btn.setObjectName(u"save_pdf_btn")
        self.save_pdf_btn.setGeometry(QRect(250, 320, 161, 61))
        self.save_pdf_btn.setFont(font2)

        self.retranslateUi(dialog_box)

        QMetaObject.connectSlotsByName(dialog_box)
    # setupUi

    def retranslateUi(self, dialog_box):
        dialog_box.setWindowTitle(QCoreApplication.translate("dialog_box", u"Widget", None))
#if QT_CONFIG(whatsthis)
        self.widget.setWhatsThis(QCoreApplication.translate("dialog_box", u"<html><head/><body><p>dsf</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("dialog_box", u"<html><head/><body><p><span style=\" color:#000000;\">\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
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

