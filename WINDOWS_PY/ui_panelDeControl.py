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
from QT_UI.iconos_panel_de_control import iconos

class Ui_panel_de_control(object):
    def setupUi(self, panel_de_control):
        if not panel_de_control.objectName():
            panel_de_control.setObjectName(u"panel_de_control")
        panel_de_control.resize(1313, 646)
        self.frame = QFrame(panel_de_control)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 1191, 611))
        self.frame.setStyleSheet(u"image: url(:/xy/ordenador-portatil.png);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 251, 571))
        self.widget.setStyleSheet(u"background:#3790FA;")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 70, 51, 431))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border-image: url(:/iconos_panel_control/ordenador-portatil.png);")

        self.verticalLayout_2.addWidget(self.label_16)

        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border-image: url(:/iconos_panel_control/carrito_de_compras.png);")

        self.verticalLayout_2.addWidget(self.label_15)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border-image: url(:/iconos_panel_control/clasificacion.png);")

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border-image: url(:/iconos_panel_control/camion-de-reparto.png);")

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border-image: url(:/iconos_panel_control/clasificacion.png);")

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border-image: url(:/iconos_panel_control/agregar-usuario.png);")

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border-image: url(:/iconos_panel_control/mano.png);")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border-image: url(:/iconos_panel_control/informe.png);")

        self.verticalLayout_2.addWidget(self.label_9)

        self.verticalFrame = QFrame(self.widget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(70, 60, 161, 461))
        self.verticalFrame.setStyleSheet(u"QFrame QPushButton {\n"
"	background-color: #3790FA; /* Color de fondo */\n"
"    color: black; /* Color del texto */\n"
"    font-size: 16px; /* Tama\u00f1o de la fuente */\n"
"    padding: 10px; /* Espaciado interno */\n"
"    margin: 5px; /* Margen externo */\n"
"    border: 2px solid black; /* Borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"QFrame QPushButton:hover {\n"
"    background-color: #37A1FA; /* Cambia el color al pasar el mouse */\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.verticalFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"padding:5px;\n"
"margin-botom:10px")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalFrame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.verticalFrame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.verticalFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.verticalFrame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"\n"
"padding:5px")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.verticalFrame.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(panel_de_control)

        QMetaObject.connectSlotsByName(panel_de_control)
    # setupUi

    def retranslateUi(self, panel_de_control):
        panel_de_control.setWindowTitle(QCoreApplication.translate("panel_de_control", u"Panel de control", None))
        self.label_16.setText("")
        self.label_15.setText("")
        self.label_14.setText("")
        self.label_13.setText("")
        self.label_12.setText("")
        self.label_11.setText("")
        self.label_10.setText("")
        self.label_9.setText("")
        self.pushButton.setText(QCoreApplication.translate("panel_de_control", u"PRODUCTOS", None))
        self.pushButton_2.setText(QCoreApplication.translate("panel_de_control", u"VENTAS", None))
        self.pushButton_3.setText(QCoreApplication.translate("panel_de_control", u"CLIENTES", None))
        self.pushButton_4.setText(QCoreApplication.translate("panel_de_control", u"COMPRAS", None))
        self.pushButton_5.setText(QCoreApplication.translate("panel_de_control", u"PROVEEDORES", None))
        self.pushButton_7.setText(QCoreApplication.translate("panel_de_control", u"EMPLEADOS", None))
        self.pushButton_6.setText(QCoreApplication.translate("panel_de_control", u"PAGOS", None))
        self.pushButton_8.setText(QCoreApplication.translate("panel_de_control", u"REPORTES", None))
    # retranslateUi

