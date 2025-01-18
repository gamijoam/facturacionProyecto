# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_facturacion.py file
#     pyside6-uic ui_facturacion.ui -o ui_facturacion.py, or
#     pyside2-uic ui_facturacion.ui -o ui_facturacion.py
from WINDOWS_PY.ui_facturacion import Ui_Widget
from WINDOWS_PY.ui_login import Ui_Form

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_login = Ui_Form()
        self.ui_login.setupUi(self)
<<<<<<< HEAD
        self.ui_login.pushButton.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        self.close()
        self.facturacion()
=======
        self.ui_login.pushButton_2.clicked.connect(self.close)

    def cerrar_ventana_login(self):
        self.close()
>>>>>>> feature/agregar_boton_cancelar_login

    def facturacion(self):
        self.ventana_facturacion = QtWidgets.QMainWindow()
        self.ui_ventana_facturacion = Ui_Widget()
        self.ui_ventana_facturacion.setupUi(self.ventana_facturacion)
        self.ventana_facturacion.show()
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(0,182.75)
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(1,182.75)
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(2,182.75)
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(3,182.75)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
