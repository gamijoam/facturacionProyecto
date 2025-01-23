from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter
from src.view.PY.ui_facturacion import Ui_Widget
from src.models.buscador_bd import Buscar_producto

def facturacion(self):
    """
    Metodo que crea y muestra la ventana de facturación.
    """
    self.ventana_facturacion = QtWidgets.QMainWindow()  # Crea una nueva ventana principal.
    self.ui_ventana_facturacion = Ui_Widget()  # Crea una instancia de la interfaz de facturación.
    self.ui_ventana_facturacion.setupUi(self.ventana_facturacion)  # Configura la interfaz en la ventana.

    # Configuración del ancho de las columnas de la tabla en la interfaz de facturación
    self.ui_ventana_facturacion.tableWidget.setColumnWidth(0, 257)  # Ancho de la columna 1.
    self.ui_ventana_facturacion.tableWidget.setColumnWidth(1, 257)  # Ancho de la columna 2.
    self.ui_ventana_facturacion.tableWidget.setColumnWidth(2, 257)  # Ancho de la columna 3.

    # Iniciar base de dato para buscar un producto
    self.buscar_producto = Buscar_producto('inventario')  # Conexion a base de dato
    self.lista_producto = self.buscar_producto.buscador_de_producto()  # Metodo para buscar un producto

    # Configurar el QCompleter
    self.completer = QCompleter(self.lista_producto)
    self.completer.setCaseSensitivity(Qt.CaseInsensitive)# Búsqueda no sensible a mayúsculas
    self.completer.setCompletionMode(QCompleter.PopupCompletion)  # Mostrar sugerencias en un popup
    # Conectar el QCompleter al QLineEdit
    self.ui_ventana_facturacion.lineEdit.setCompleter(self.completer)
    self.ui_ventana_facturacion.lineEdit.returnPressed.connect(lambda : producto_seleccionado(self))
    self.ventana_facturacion.show()  # Muestra la ventana de facturación.



def producto_seleccionado(self):
    # Obtener el texto ingresado en el QLineEdit
    selected_product = self.ui_ventana_facturacion.lineEdit.text()
    print(f"Producto seleccionado: {selected_product}")
    actualizar_datos_en_pantalla(self,selected_product)

def actualizar_datos_en_pantalla(self,texto):
    self.ui_ventana_facturacion.label_4.setText(texto)