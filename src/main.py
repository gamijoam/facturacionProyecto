# Este archivo Python utiliza la codificación UTF-8
# -*- coding: utf-8 -*-

# Importación de módulos necesarios
import sys  # Proporciona acceso a funciones y variables relacionadas con el intérprete de Python.
from PySide6 import QtWidgets  # Importa el módulo QtWidgets de PySide6 para crear interfaces gráficas.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget , QCompleter # Importa clases específicas de QtWidgets.

# Importación de las interfaces gráficas generadas automáticamente desde archivos .ui
# Nota: Estas interfaces deben generarse usando el comando pyside6-uic.
from src.view.PY.ui_facturacion import Ui_Widget  # Interfaz de facturación.
from src.view.PY.ui_login import Ui_Form  # Interfaz de inicio de sesión.
from src.view.PY.ui_panelDeControl import Ui_panel_de_control  # Interfaz del panel de control.
from src.database.scripts.buscador_bd import Buscar_producto

# Definición de la clase principal de la aplicación
class Widget(QWidget):
    def __init__(self, parent=None):
        """
        Constructor de la clase Widget.
        Inicializa la ventana principal y configura la interfaz de inicio de sesión.
        """
        super().__init__(parent)  # Llama al constructor de la clase base QWidget.

        # Inicialización de atributos para las ventanas y sus interfaces
        self.completer = None
        self.lineEditProductSearch = None
        self.product_list = None
        self.ui_ventana_facturacion = None  # Almacenará la interfaz de facturación.
        self.ui_ventana_panel_de_control = None  # Almacenará la interfaz del panel de control.
        self.ventana_panel_de_control = None  # Almacenará la ventana del panel de control.

        # Configuración de la interfaz de inicio de sesión
        self.ui_login = Ui_Form()  # Crea una instancia de la interfaz de inicio de sesión.
        self.ui_login.setupUi(self)  # Configura la interfaz en la ventana actual.

        # Conexión del botón de la interfaz de inicio de sesión al metodo cerrar_ventana
        self.ui_login.pushButton.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        """
        Metodo que se ejecuta al hacer clic en el botón de la interfaz de inicio de sesión.
        Cierra la ventana actual y abre el panel de control.
        """
        self.close()  # Cierra la ventana actual.
        self.panel_de_control()  # Llama al metodo para abrir el panel de control.

        # Conexión del botón de la interfaz de inicio de sesión al metodo cerrar_ventana_login
        self.ui_login.pushButton.clicked.connect(self.cerrar_ventana_login)

    def panel_de_control(self):
        """
        Metodo que crea y muestra la ventana del panel de control.
        """
        self.ventana_panel_de_control = QtWidgets.QMainWindow()  # Crea una nueva ventana principal.
        self.ui_ventana_panel_de_control = Ui_panel_de_control()  # Crea una instancia de la interfaz del panel de control.
        self.ui_ventana_panel_de_control.setupUi(self.ventana_panel_de_control)  # Configura la interfaz en la ventana.

        # Conexión del botón de la interfaz del panel de control al metodo facturacion
        self.ui_ventana_panel_de_control.pushButton_20.clicked.connect(self.facturacion)

        self.ventana_panel_de_control.show()  # Muestra la ventana del panel de control.

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

        #Iniciar base de dato
        self.buscar_producto = Buscar_producto('inventario') #Conexion a base de dato
        self.lista_producto = self.buscar_producto.buscador_de_producto() #Metodo para buscar un producto

        # Configurar el QCompleter
        self.completer = QCompleter(self.lista_producto) # Búsqueda no sensible a mayúsculas
        self.completer.setCompletionMode(QCompleter.PopupCompletion)  # Mostrar sugerencias en un popup

        # Conectar el QCompleter al QLineEdit
        self.ui_ventana_facturacion.lineEdit.setCompleter(self.completer)
       # self.ui_ventana_facturacion.lineEdit.returnPressed.connect(self.on_product_selected)
        self.ventana_facturacion.show()  # Muestra la ventana de facturación.

    def cerrar_ventana_login(self):
        """
        Metodo que cierra la ventana de inicio de sesión y abre el panel de control.
        """
        self.close()  # Cierra la ventana actual.
        self.panel_de_control()  # Llama al metodo para abrir el panel de control.

    def producto_selecionado(self):
        # Obtener el texto ingresado en el QLineEdit
        selected_product = self.ui_ventana_facturacion.lineEdit.text()
        print(f"Producto seleccionado: {selected_product}")
        # Aquí puedes agregar la lógica para manejar el producto seleccionado

# Bloque principal de ejecución del programa
if __name__ == "__main__":
    """
    Punto de entrada principal de la aplicación.
    """
    app = QApplication(sys.argv)  # Crea una instancia de la aplicación.
    app.setStyle("Fusion")  # Cambia el estilo de la aplicación
    widget = Widget()  # Crea una instancia de la clase Widget (ventana principal).
    widget.show()  # Muestra la ventana principal.
    sys.exit(app.exec())  # Inicia el bucle de eventos y espera a que la aplicación se cierre.