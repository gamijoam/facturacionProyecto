# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_facturacion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QWidget)
from QT_UI.iconos_facturacion import iconos

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1078, 656)
        Widget.setStyleSheet(u"font-size:15px")
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(270, 180, 771, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 439))
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 771, 421))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 610, 161, 41))
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border:1px solid black;\n"
"background: #51E058;\n"
"border-radius:2px;\n"
"text-align:left;\n"
"padding-left:30px")
        self.frame_2 = QFrame(Widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 50, 211, 51))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #CCDBA8;  /* Elimina el borde del QLabel */\n"
"    background-color: #CCDBA8;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 191, 31))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 10, 31, 31))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 10, 111, 31))
        self.label_3.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.frame_3 = QFrame(Widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(240, 50, 211, 51))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #CCDBA8;  /* Elimina el borde del QLabel */\n"
"    background-color: #CCDBA8;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 191, 31))
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 10, 31, 31))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 10, 161, 31))
        self.label_6.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.frame_4 = QFrame(Widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(470, 50, 211, 51))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #CCDBA8;  /* Elimina el borde del QLabel */\n"
"    background-color: #CCDBA8;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 191, 31))
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 10, 31, 31))
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 10, 111, 31))
        self.label_9.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(10, 143, 88, 31))
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 110, 111, 31))
        self.label_10.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.frame_5 = QFrame(Widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(110, 140, 71, 41))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #CCDBA8;  /* Elimina el borde del QLabel */\n"
"    background-color: #CCDBA8;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(170, 10, 31, 31))
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 31, 20))
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(120, 110, 51, 31))
        self.label_13.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 130, 771, 41))
        self.lineEdit.setStyleSheet(u"border-radius:5px;")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(990, 130, 51, 41))
        self.pushButton_2.setStyleSheet(u"border:none")
        icon = QIcon()
        icon.addFile(u":/xy/borrador-borrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(45, 45))
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(370, 620, 21, 21))
        self.label_14.setStyleSheet(u"border-image: url(:/xy/mano.png);")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"CODIGO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"PRODUCTO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"PRECIO", None));
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PAGAR", None))
        self.label.setText(QCoreApplication.translate("Widget", u"15", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"ID PRODUCTO", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"15", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"NOMBRE PRODUCTO", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"15", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"ID PRODUCTO", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"CANTIDAD", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"15", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"STOCK", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"BUSCAR PRODUCTO", None))
        self.pushButton_2.setText("")
        self.label_14.setText("")
    # retranslateUi

