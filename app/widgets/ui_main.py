# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QScrollArea, QSizePolicy, QTabWidget,
    QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1419, 923)
        Main.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u"icon/images.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Main.setWindowIcon(icon)
        Main.setStyleSheet(u"")
        self.tabWidget = QTabWidget(Main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-1, -1, 1421, 921))
        self.tabWidget.setMaximumSize(QSize(1500, 1100))
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.tabWidget.setStyleSheet(u"")
        self.reference = QWidget()
        self.reference.setObjectName(u"reference")
        self.scrollArea = QScrollArea(self.reference)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 0, 1401, 871))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1401, 871))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.reference, "")

        self.retranslateUi(Main)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\u0421\u0438\u0441\u0442\u0435\u043c\u044b \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0430\u0446\u0438\u0438 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u043e\u0431\u043e\u0440\u043e\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reference), QCoreApplication.translate("Main", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

