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
from src.view.iconos_facturacion import iconos

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1166, 672)
        Widget.setStyleSheet(u"font-size:15px")
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(220, 180, 761, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 759, 439))
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
        self.pushButton.setGeometry(QRect(220, 610, 161, 51))
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border:1px solid black;\n"
"background: #FFC0CB;\n"
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
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 191, 31))
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
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 191, 31))
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
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
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
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(17, 143, 88, 31))
        self.spinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 110, 101, 31))
        self.label_10.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.frame_5 = QFrame(Widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(130, 140, 71, 51))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 51, 31))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(140, 110, 51, 31))
        self.label_13.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(220, 130, 761, 41))
        self.lineEdit.setStyleSheet(u"")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1020, 130, 51, 41))
        self.pushButton_2.setStyleSheet(u"border:none")
        icon = QIcon()
        icon.addFile(u":/xy/borrador-borrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(45, 45))
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 620, 31, 31))
        self.label_14.setStyleSheet(u"border-image: url(:/xy/mano.png);")
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(420, 610, 161, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"border:1px solid black;\n"
"background: #87CEEB;\n"
"border-radius:2px;\n"
"text-align:left;\n"
"padding-left:30px")
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(820, 610, 161, 51))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"border:1px solid black;\n"
"background: #B2F2BB;\n"
"border-radius:2px;\n"
"text-align:left;\n"
"padding-left:30px")
        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(620, 610, 161, 51))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"border:1px solid black;\n"
"background: #E6E6FA;\n"
"border-radius:2px;\n"
"text-align:left;\n"
"padding-left:30px")
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(530, 620, 31, 31))
        self.label_15.setStyleSheet(u"border-image: url(:/xy/caja-registradora.png);")
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(730, 620, 41, 31))
        self.label_16.setStyleSheet(u"border-image: url(:/xy/escoba.png);")
        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(930, 620, 41, 31))
        self.label_17.setStyleSheet(u"border-image: url(:/xy/nueva-cuenta.png);")
        self.label_18 = QLabel(Widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(750, 10, 111, 31))
        self.label_18.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_6 = QFrame(Widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(700, 50, 211, 51))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 191, 31))
        self.label_21 = QLabel(Widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(980, 10, 111, 31))
        self.label_21.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.frame_7 = QFrame(Widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(930, 50, 211, 51))
        self.frame_7.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 191, 31))
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 10, 31, 31))
        self.frame_8 = QFrame(Widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 230, 101, 51))
        self.frame_8.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;  /* Borde para el QFrame */\n"
"    background-color: white;  /* Fondo para el QFrame */\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border: 2px solid #FFD700;  /* Elimina el borde del QLabel */\n"
"    background-color: #FFD700;  /* Fondo transparente */\n"
"	border-radius:5px;\n"
"	font-size:20px\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 10, 31, 31))
        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 10, 81, 31))
        self.label_25 = QLabel(Widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 200, 71, 31))
        self.label_25.setStyleSheet(u"text-decoration:underline;\n"
"font: 600 12pt \"Segoe UI\";")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(990, 180, 161, 51))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"border:1px solid black;\n"
"background:  #FFC0CB;\n"
"border-radius:2px;\n"
"text-align:left;\n"
"padding-left:20px")
        self.pushButton_7 = QPushButton(Widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(990, 240, 161, 51))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"border:1px solid black;\n"
"background: #87CEEB;\n"
"border-radius:2px;\n"
"text-align:left;\n"
"padding-left:20px")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1110, 190, 31, 31))
        self.label_2.setStyleSheet(u"border-image: url(:/xy/mas.png);")
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1108, 250, 41, 31))
        self.label_5.setStyleSheet(u"border-image: url(:/xy/boleto.png);")

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
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"ID PRODUCTO", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("Widget", u"NOMBRE PRODUCTO", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"PRECIO", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"CANTIDAD", None))
        self.label_11.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"STOCK", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"BUSCAR PRODUCTO", None))
        self.pushButton_2.setText("")
        self.label_14.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"EFECTIVO", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"CLIENTE", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"LIMPIAR", None))
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Widget", u"IVA", None))
        self.label_19.setText("")
        self.label_21.setText(QCoreApplication.translate("Widget", u"DESCUENTO", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"BS", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("Widget", u"Unidad", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"AGREGAR", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"VER TICKET", None))
        self.label_2.setText("")
        self.label_5.setText("")
    # retranslateUi

