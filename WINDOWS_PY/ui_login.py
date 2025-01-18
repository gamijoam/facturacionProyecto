# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 370)
        Form.setStyleSheet(u"")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QRect(39, 130, 281, 41))
        self.lineEdit_3.setStyleSheet(u"\n"
"    border: 2px solid black;       /* Borde negro de 2px de grosor */\n"
"    border-radius: 10px;           /* Bordes redondeados */\n"
"    padding: 5px;                  /* Espacio interno */\n"
"    background-color: white;       /* Color de fondo */\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 50, 261, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 25pt \"Segoe UI\";")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 270, 131, 51))
        self.pushButton.setStyleSheet(u"background-color: #E5E3E4;\n"
"font: 700 12pt \"Segoe UI\";\n"
"font: 700 italic 12pt \"Segoe UI\";\n"
" border: 2px solid black;       /* Borde negro de 2px de grosor */\n"
"    border-radius: 10px;           /* Bordes redondeados */\n"
"    padding: 5px")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QRect(40, 200, 281, 41))
        self.lineEdit_4.setStyleSheet(u"\n"
"    border: 2px solid black;       /* Borde negro de 2px de grosor */\n"
"    border-radius: 10px;           /* Bordes redondeados */\n"
"    padding: 5px;                  /* Espacio interno */\n"
"    background-color: white;       /* Color de fondo */\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"INGRESAR", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
    # retranslateUi

