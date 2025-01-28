# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrar_productos.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget)

class Ui_Registrar_productos(object):
    def setupUi(self, Registrar_productos):
        if not Registrar_productos.objectName():
            Registrar_productos.setObjectName(u"Registrar_productos")
        Registrar_productos.resize(949, 602)
        Registrar_productos.setStyleSheet(u"QLineEdit{\n"
"	/*border : 1.5px solid black;\n"
"	border-radius: 5px;*/\n"
"}\n"
"QTextEdit{\n"
"	border : 1.5px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton{\n"
"	border: 1px solid black;\n"
"	background:#fff;\n"
"	border-radius:6px;\n"
"	\n"
"	font: 600 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"")
        self.lineEdit_2 = QLineEdit(Registrar_productos)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(26, 20, 841, 31))
        self.lineEdit_2.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(Registrar_productos)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(26, 60, 841, 31))
        self.lineEdit.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.textEdit = QTextEdit(Registrar_productos)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 100, 371, 281))
        self.textEdit.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.comboBox = QComboBox(Registrar_productos)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(440, 140, 171, 41))
        self.comboBox.setEditable(True)
        self.comboBox_2 = QComboBox(Registrar_productos)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(650, 140, 181, 41))
        self.comboBox_2.setEditable(True)
        self.pushButton_3 = QPushButton(Registrar_productos)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 500, 288, 41))
        self.pushButton = QPushButton(Registrar_productos)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 500, 288, 41))
        self.pushButton_2 = QPushButton(Registrar_productos)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(590, 500, 288, 41))
        self.lineEdit_3 = QLineEdit(Registrar_productos)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 410, 181, 41))
        self.lineEdit_3.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.comboBox_3 = QComboBox(Registrar_productos)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(490, 340, 91, 41))
        self.comboBox_3.setStyleSheet(u"")
        self.comboBox_3.setEditable(True)
        self.label_2 = QLabel(Registrar_productos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 310, 181, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(Registrar_productos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 110, 151, 20))
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(Registrar_productos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(670, 110, 151, 20))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(Registrar_productos)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(480, 210, 91, 21))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox = QSpinBox(Registrar_productos)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(490, 240, 81, 41))
        self.lineEdit_4 = QLineEdit(Registrar_productos)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(450, 410, 181, 41))
        self.lineEdit_4.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.label = QLabel(Registrar_productos)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 420, 31, 21))
        font3 = QFont()
        font3.setPointSize(17)
        self.label.setFont(font3)
        self.lineEdit_5 = QLineEdit(Registrar_productos)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(660, 410, 191, 41))
        self.lineEdit_5.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.lineEdit_6 = QLineEdit(Registrar_productos)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(240, 410, 181, 41))
        self.lineEdit_6.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.label_7 = QLabel(Registrar_productos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 420, 31, 21))
        self.label_7.setFont(font3)

        self.retranslateUi(Registrar_productos)

        QMetaObject.connectSlotsByName(Registrar_productos)
    # setupUi

    def retranslateUi(self, Registrar_productos):
        Registrar_productos.setWindowTitle(QCoreApplication.translate("Registrar_productos", u"Form", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"Nombre del Producto", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"C\u00f3digo ", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"Descripci\u00f3n", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"Valor", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"Valor", None))
        self.pushButton_3.setText(QCoreApplication.translate("Registrar_productos", u"Registrar Producto", None))
        self.pushButton.setText(QCoreApplication.translate("Registrar_productos", u"Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Registrar_productos", u"Limpiar Formulario", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"COSTO PRODUCTO", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Registrar_productos", u"10", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Registrar_productos", u"20", None))

        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"Margen de ganancia", None))
        self.label_2.setText(QCoreApplication.translate("Registrar_productos", u"Margen de ganancia %", None))
        self.label_4.setText(QCoreApplication.translate("Registrar_productos", u"CATEGORIA", None))
        self.label_5.setText(QCoreApplication.translate("Registrar_productos", u"PROVEEDORES", None))
        self.label_6.setText(QCoreApplication.translate("Registrar_productos", u"<html><head/><body><p>UNIDADES</p><p><br/></p></body></html>", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"DESCUENTO", None))
        self.label.setText(QCoreApplication.translate("Registrar_productos", u"%", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"VALOR FINAL", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Registrar_productos", u"IVA", None))
        self.label_7.setText(QCoreApplication.translate("Registrar_productos", u"%", None))
    # retranslateUi

