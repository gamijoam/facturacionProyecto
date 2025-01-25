from PySide6 import QtWidgets
from src.view.PY.registrar_productos import Ui_Registrar_productos

class RegistarProducto(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.registrar_producto = Ui_Registrar_productos()
        self.registrar_producto.setupUi(self)
        


def ejecutar_ventana_registrar_producto(self):
    self.ventana_registrarProducto = RegistarProducto()
    self.ventana_registrarProducto.show()
    

            