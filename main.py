# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_facturacion.py file
#     pyside6-uic ui_facturacion.ui -o ui_facturacion.py, or
#     pyside2-uic ui_facturacion.ui -o ui_facturacion.py
from WINDOWS_PY.ui_facturacion import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0,182.75)
        self.ui.tableWidget.setColumnWidth(1,182.75)
        self.ui.tableWidget.setColumnWidth(2,182.75)
        self.ui.tableWidget.setColumnWidth(3,182.75)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
