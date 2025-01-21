# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem

# Important:
# You need to run the following command to generate the ui_facturacion.py file
#     pyside6-uic ui_facturacion.ui -o ui_facturacion.py, or
#     pyside2-uic ui_facturacion.ui -o ui_facturacion.py
from WINDOWS_PY.ui_facturacion import Ui_Widget
from WINDOWS_PY.ui_login import Ui_Form
from WINDOWS_PY.ui_panelDeControl import Ui_panel_de_control

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_ventana_facturacion = None
        self.ui_ventana_panel_de_control = None
        self.ventana_panel_de_control = None
        self.items = None
        self.ui_login = Ui_Form()
        self.ui_login.setupUi(self)
        self.ui_login.pushButton.clicked.connect(self.cerrar_ventana_login)

    def panel_de_control(self):
        self.ventana_panel_de_control = QtWidgets.QMainWindow()
        self.ui_ventana_panel_de_control = Ui_panel_de_control()
        self.ui_ventana_panel_de_control.setupUi(self.ventana_panel_de_control)
        self.ui_ventana_panel_de_control.pushButton_20.clicked.connect(self.facturacion)
        self.ventana_panel_de_control.show()

    def facturacion(self):
        self.ventana_facturacion = QtWidgets.QMainWindow()
        self.ui_ventana_facturacion = Ui_Widget()
        self.ui_ventana_facturacion.setupUi(self.ventana_facturacion)
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(0, 257)
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(1, 257)
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(2, 257)
        self.ventana_facturacion.show()

    def cerrar_ventana_login(self):
       self.close()
       self.panel_de_control()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
