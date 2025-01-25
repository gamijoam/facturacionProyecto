# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_panelDeControl.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from src.view.iconos_panel_de_control import iconos 

class Ui_panel_de_control(object):
    def setupUi(self, panel_de_control):
        if not panel_de_control.objectName():
            panel_de_control.setObjectName(u"panel_de_control")
        panel_de_control.resize(1112, 596)
        font = QFont()
        font.setPointSize(7)
        font.setBold(True)
        panel_de_control.setFont(font)
        panel_de_control.setStyleSheet(u"")
        self.pushButton_11 = QPushButton(panel_de_control)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setGeometry(QRect(760, 40, 141, 131))
        self.pushButton_11.setStyleSheet(u"border:3px solid #B2F2BB;\n"
"background-color: rgb(234, 234, 234);\n"
"\n"
"border-radius:3px;\n"
"border-bottom-left-radius: 10px; /* Radio de la esquina inferior izquierda */\n"
"border-bottom-right-radius: 10px; /* Radio de la esquina inferior derecha */\n"
"")
        icon = QIcon()
        icon.addFile(u":/iconos_panel_control/clasificacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(60, 60))
        self.label_2 = QLabel(panel_de_control)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(760, 10, 141, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border:1.7px solid black;\n"
"background:#B2F2BB;\n"
"border-radius:4.5px;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_2 = QWidget(panel_de_control)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 251, 571))
        self.widget_2.setStyleSheet(u"background:#87CEEB;\n"
"border:1px solid black;\n"
"border-radius:5px;")
        self.verticalWidget_2 = QWidget(self.widget_2)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setGeometry(QRect(20, 90, 61, 441))
        self.verticalWidget_2.setStyleSheet(u"border:none;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_17 = QLabel(self.verticalWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border-image: url(:/iconos_panel_control/ordenador-portatil.png);")

        self.verticalLayout_3.addWidget(self.label_17)

        self.label_18 = QLabel(self.verticalWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border-image: url(:/iconos_panel_control/carrito_de_compras.png);")

        self.verticalLayout_3.addWidget(self.label_18)

        self.label_19 = QLabel(self.verticalWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border-image: url(:/iconos_panel_control/clasificacion.png);")

        self.verticalLayout_3.addWidget(self.label_19)

        self.label_20 = QLabel(self.verticalWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border-image: url(:/iconos_panel_control/camion-de-reparto.png);")

        self.verticalLayout_3.addWidget(self.label_20)

        self.label_21 = QLabel(self.verticalWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border-image: url(:/iconos_panel_control/clasificacion.png);")

        self.verticalLayout_3.addWidget(self.label_21)

        self.label_22 = QLabel(self.verticalWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border-image: url(:/iconos_panel_control/agregar-usuario.png);")

        self.verticalLayout_3.addWidget(self.label_22)

        self.label_23 = QLabel(self.verticalWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border-image: url(:/iconos_panel_control/mano.png);")

        self.verticalLayout_3.addWidget(self.label_23)

        self.label_24 = QLabel(self.verticalWidget_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border-image: url(:/iconos_panel_control/informe.png);")

        self.verticalLayout_3.addWidget(self.label_24)

        self.verticalFrame_2 = QFrame(self.widget_2)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setGeometry(QRect(80, 70, 161, 451))
        self.verticalFrame_2.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"QFrame QPushButton {\n"
"	background-color: #87CEEB; /* Color de fondo */\n"
"    color: black; /* Color del texto */\n"
"    font-size: 16px; /* Tama\u00f1o de la fuente */\n"
"    padding: 10px; /* Espaciado interno */\n"
"    margin: 5px; /* Margen externo */\n"
"    border: 1.5px solid black; /* Borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"QFrame QPushButton:hover {\n"
"    background-color: #37A1FA; /* Cambia el color al pasar el mouse */\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_9 = QPushButton(self.verticalFrame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"\n"
"padding:5px;\n"
"margin-botom:10px")

        self.verticalLayout_4.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.verticalFrame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.verticalFrame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.verticalFrame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.verticalFrame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.verticalFrame_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.verticalFrame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.verticalFrame_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.pushButton_17)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 30, 221, 41))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"border:none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_20 = QPushButton(panel_de_control)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(280, 40, 141, 131))
        self.pushButton_20.setStyleSheet(u"border:3px solid #B2F2BB;\n"
"\n"
"background-color: rgb(234, 234, 234);\n"
"\n"
"border-bottom-left-radius: 10px; /* Radio de la esquina inferior izquierda */\n"
"border-bottom-right-radius: 10px; /* Radio de la esquina inferior derecha */\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos_panel_control/carrito_de_compras.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_20.setIcon(icon1)
        self.pushButton_20.setIconSize(QSize(60, 60))
        self.label_5 = QLabel(panel_de_control)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 10, 141, 41))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border:1.7px solid black;\n"
"background:#B2F2BB;\n"
"border-radius:4.5px;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_18 = QPushButton(panel_de_control)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setGeometry(QRect(600, 40, 141, 131))
        self.pushButton_18.setStyleSheet(u"border:3px solid #B2F2BB;\n"
"border-radius:3px;\n"
"background-color: rgb(234, 234, 234);\n"
"border-bottom-left-radius: 10px; /* Radio de la esquina inferior izquierda */\n"
"border-bottom-right-radius: 10px; /* Radio de la esquina inferior derecha */")
        icon2 = QIcon()
        icon2.addFile(u":/iconos_panel_control/caja-registradora.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QSize(60, 60))
        self.label_3 = QLabel(panel_de_control)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(600, 10, 141, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border:1.7px solid black;\n"
"background:#B2F2BB;\n"
"border-radius:4.5px;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_19 = QPushButton(panel_de_control)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(440, 40, 141, 131))
        self.pushButton_19.setStyleSheet(u"border:3px solid #B2F2BB;\n"
"border-radius:3px;\n"
"background-color: rgb(234, 234, 234);\n"
"border-bottom-left-radius: 10px; /* Radio de la esquina inferior izquierda */\n"
"border-bottom-right-radius: 10px; /* Radio de la esquina inferior derecha */")
        icon3 = QIcon()
        icon3.addFile(u":/iconos_panel_control/productos-de-limpieza.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_19.setIcon(icon3)
        self.pushButton_19.setIconSize(QSize(60, 60))
        self.label_4 = QLabel(panel_de_control)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 10, 141, 41))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:1.7px solid black;\n"
"background:#B2F2BB;\n"
"border-radius:4.5px;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_21 = QPushButton(panel_de_control)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setEnabled(False)
        self.pushButton_21.setGeometry(QRect(920, 40, 141, 131))
        self.pushButton_21.setStyleSheet(u"border:3px solid #B2F2BB;\n"
"border-radius:3px;\n"
"background-color: rgb(234, 234, 234);\n"
"border-bottom-left-radius: 10px; /* Radio de la esquina inferior izquierda */\n"
"border-bottom-right-radius: 10px; /* Radio de la esquina inferior derecha */")
        icon4 = QIcon()
        icon4.addFile(u":/iconos_panel_control/grafico-de-acciones.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon4)
        self.pushButton_21.setIconSize(QSize(60, 60))
        self.label_6 = QLabel(panel_de_control)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(920, 10, 141, 41))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border:1.7px solid black;\n"
"background:#B2F2BB;\n"
"border-radius:4.5px;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(panel_de_control)

        QMetaObject.connectSlotsByName(panel_de_control)
    # setupUi

    def retranslateUi(self, panel_de_control):
        panel_de_control.setWindowTitle(QCoreApplication.translate("panel_de_control", u"Panel de control", None))
        self.pushButton_11.setText("")
        self.label_2.setText(QCoreApplication.translate("panel_de_control", u"CLIENTES", None))
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("panel_de_control", u"PRODUCTOS", None))
        self.pushButton_10.setText(QCoreApplication.translate("panel_de_control", u"VENTAS", None))
        self.pushButton_12.setText(QCoreApplication.translate("panel_de_control", u"CLIENTES", None))
        self.pushButton_13.setText(QCoreApplication.translate("panel_de_control", u"COMPRAS", None))
        self.pushButton_14.setText(QCoreApplication.translate("panel_de_control", u"PROVEEDORES", None))
        self.pushButton_15.setText(QCoreApplication.translate("panel_de_control", u"EMPLEADOS", None))
        self.pushButton_16.setText(QCoreApplication.translate("panel_de_control", u"PAGOS", None))
        self.pushButton_17.setText(QCoreApplication.translate("panel_de_control", u"REPORTES", None))
        self.label.setText(QCoreApplication.translate("panel_de_control", u"SISTEMA DE FACTURACION", None))
        self.pushButton_20.setText("")
        self.label_5.setText(QCoreApplication.translate("panel_de_control", u"VENTAS", None))
        self.pushButton_18.setText("")
        self.label_3.setText(QCoreApplication.translate("panel_de_control", u"CAJA", None))
        self.pushButton_19.setText("")
        self.label_4.setText(QCoreApplication.translate("panel_de_control", u"<html><head/><body><p>REGISTRAR <br/>PRODUCTO</p></body></html>", None))
        self.pushButton_21.setText("")
        self.label_6.setText(QCoreApplication.translate("panel_de_control", u"COTIZACIONES", None))
    # retranslateUi

