from PySide6 import QtWidgets
from src.view.PY.ui_panelDeControl import Ui_panel_de_control
from src.controllers.facturacion import facturacion
from src.controllers.registrar_producto import ejecutar_ventana_registrar_producto
def panel_de_control(self):
    """
    Metodo que crea y muestra la ventana del panel de control.
    """
    self.ventana_panel_de_control = QtWidgets.QMainWindow()  # Crea una nueva ventana principal.
    self.ui_ventana_panel_de_control = Ui_panel_de_control()  # Crea una instancia de la interfaz del panel de control.
    self.ui_ventana_panel_de_control.setupUi(self.ventana_panel_de_control)  # Configura la interfaz en la ventana.

    # Conexión del botón de la interfaz del panel de control al metodo facturacion
    self.ui_ventana_panel_de_control.pushButton_20.clicked.connect(lambda : facturacion(self))
    self.ui_ventana_panel_de_control.pushButton_19.clicked.connect(lambda : ejecutar_ventana_registrar_producto(self))
    self.ventana_panel_de_control.show()  # Muestra la ventana del panel de control.