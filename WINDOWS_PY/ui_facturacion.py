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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1078, 656)
        Widget.setStyleSheet(u"font-size:15px")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 0, 341, 61))
        self.label_3.setStyleSheet(u"font-size:40px")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 490, 161, 18))
        self.label_4.setStyleSheet(u"font-size:16px")
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 520, 161, 26))
        self.lineEdit_3 = QLineEdit(Widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(400, 520, 161, 26))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 490, 161, 18))
        self.label_5.setStyleSheet(u"font-size:16px")
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(580, 490, 161, 18))
        self.label_6.setStyleSheet(u"font-size:16px")
        self.lineEdit_4 = QLineEdit(Widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(580, 520, 161, 26))
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(220, 570, 661, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(880, 20, 231, 18))
        self.label.setStyleSheet(u"font-size: 20px")
        self.tableWidget = QTableWidget(Widget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(220, 70, 731, 401))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    font-size: 14px; /* Tama\u00f1o de la fuente */\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #f0f0f0; /* Color de fondo para la esquina */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    text-align: center; /* Centra el texto horizontalmente */\n"
"    padding: 5px; /* A\u00f1ade un poco de espacio alrededor del texto */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; /* Color de fondo para los encabezados */\n"
"    padding: 5px; /* Espacio alrededor del texto en los encabezados */\n"
"    font-weight: bold; /* Texto en negrita para los encabezados */\n"
"    text-align: center; /* Centra el texto en los encabezados */\n"
"}")
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setRowCount(3)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 201, 581))
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.groupBox.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Alinea el t\u00edtulo en el centro */\n"
"    \n"
"}")
        self.groupBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 191, 616))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 0, 9, 200)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(177, 0))
        self.label_8.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.label_8.setFrameShape(QFrame.Shape.NoFrame)
        self.label_8.setIndent(-1)

        self.verticalLayout.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout.addWidget(self.lineEdit_7)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"VENTAS", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Total venta producto", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widget", u"1000.32 BS", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Widget", u"0 BS", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Efectivo Cliente", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Cambio del cliente", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Widget", u"15 BS", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Cobrar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Limpiar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Precio dolar 53,40 BS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"ID Producto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Nombre Producto", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Valor Unidad", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"2652152", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"mayonesa", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"100", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"154152", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget", u"salsa de tomate", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget", u"2", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget", u"300", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Widget", u"5648455", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Widget", u"atun", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Widget", u"3", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Widget", u"400", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"INFORMACION DE VENTAS", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"N\u00ba TRANSACCION", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Fecha de venta", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Venta realizada por", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"N\u00ba CAJA", None))
    # retranslateUi

