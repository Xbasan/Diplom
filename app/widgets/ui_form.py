# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QPushButton,
    QScrollArea, QSizePolicy, QTextEdit, QWidget)

class Ui_Documents(object):
    def setupUi(self, Documents):
        if not Documents.objectName():
            Documents.setObjectName(u"Documents")
        Documents.resize(1400, 855)
        Documents.setMinimumSize(QSize(1320, 0))
        Documents.setMaximumSize(QSize(16777215, 16777215))
        Documents.setStyleSheet(u"")
        self.scrollArea = QScrollArea(Documents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-2, -1, 1021, 870))
        self.scrollArea.setMaximumSize(QSize(2222222, 16777215))
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
        self.createButton = QPushButton(Documents)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(1040, 730, 100, 100))
        self.createButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createButton.setStyleSheet(u"border-radius: 50%;\n"
"background-color: rgba(0, 85, 255, 55);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.createButton.setIcon(icon)
        self.createButton.setIconSize(QSize(48, 48))
        self.NameButton = QPushButton(Documents)
        self.NameButton.setObjectName(u"NameButton")
        self.NameButton.setGeometry(QRect(1340, 90, 42, 42))
        self.NameButton.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.NameButton.setFont(font)
        self.NameButton.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgba(0, 85, 255, 55);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.NameButton.setIcon(icon1)
        self.nameTextEdit = QTextEdit(Documents)
        self.nameTextEdit.setObjectName(u"nameTextEdit")
        self.nameTextEdit.setGeometry(QRect(1040, 90, 281, 40))
        self.nameTextEdit.setMaximumSize(QSize(300, 45))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setItalic(True)
        self.nameTextEdit.setFont(font1)
        self.nameTextEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        self.FileButton = QPushButton(Documents)
        self.FileButton.setObjectName(u"FileButton")
        self.FileButton.setGeometry(QRect(1340, 160, 42, 42))
        self.FileButton.setMaximumSize(QSize(100, 16777215))
        self.FileButton.setFont(font)
        self.FileButton.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgba(0, 85, 255, 55);")
        self.FileButton.setIcon(icon1)
        self.FileTextEdit = QTextEdit(Documents)
        self.FileTextEdit.setObjectName(u"FileTextEdit")
        self.FileTextEdit.setGeometry(QRect(1040, 160, 281, 40))
        self.FileTextEdit.setMaximumSize(QSize(300, 40))
        self.FileTextEdit.setFont(font1)
        self.FileTextEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        self.dateEdit = QDateEdit(Documents)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(1040, 230, 281, 41))
        self.dateEdit.setFont(font1)
        self.dateEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        self.DataButton = QPushButton(Documents)
        self.DataButton.setObjectName(u"DataButton")
        self.DataButton.setGeometry(QRect(1340, 230, 42, 42))
        self.DataButton.setMaximumSize(QSize(100, 16777215))
        self.DataButton.setFont(font)
        self.DataButton.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgba(0, 85, 255, 55);")
        self.DataButton.setIcon(icon1)
        self.comboBox = QComboBox(Documents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(1040, 300, 151, 41))
        self.comboBox.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(0, 85, 255, 55);\n"
"padding-left:10px")
        self.update = QPushButton(Documents)
        self.update.setObjectName(u"update")
        self.update.setGeometry(QRect(1030, 10, 52, 52))
        self.update.setStyleSheet(u"border-radius: 26px;\n"
"background-color: rgba(0, 85, 255, 55);")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.update.setIcon(icon2)
        self.update.setIconSize(QSize(32, 32))

        self.retranslateUi(Documents)

        QMetaObject.connectSlotsByName(Documents)
    # setupUi

    def retranslateUi(self, Documents):
        Documents.setWindowTitle(QCoreApplication.translate("Documents", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.createButton.setToolTip(QCoreApplication.translate("Documents", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.createButton.setWhatsThis(QCoreApplication.translate("Documents", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.createButton.setText("")
        self.NameButton.setText("")
        self.nameTextEdit.setPlaceholderText(QCoreApplication.translate("Documents", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0438\u043b\u044f", None))
        self.FileButton.setText("")
#if QT_CONFIG(tooltip)
        self.FileTextEdit.setToolTip(QCoreApplication.translate("Documents", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FileTextEdit.setWhatsThis(QCoreApplication.translate("Documents", u"<html><head/><body><p>;;</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FileTextEdit.setHtml(QCoreApplication.translate("Documents", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:14pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.FileTextEdit.setPlaceholderText(QCoreApplication.translate("Documents", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.DataButton.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Documents", u"\u0432\u0441\u0435 \u0444\u043e\u0440\u043c\u0430\u0442\u044b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Documents", u".doxc", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Documents", u".pdf", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Documents", u".xlsx", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Documents", u".pptx", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Documents", u".txt", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Documents", u".csv", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Documents", u".odt", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Documents", u".ods", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Documents", u".odp", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Documents", u".jpg", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Documents", u".png", None))

        self.update.setText("")
    # retranslateUi

