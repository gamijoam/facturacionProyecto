# Este archivo Python utiliza la codificación UTF-8
# -*- coding: utf-8 -*-

# Importación de módulos necesarios
import sys  # Proporciona acceso a funciones y variables relacionadas con el intérprete de Python.
from PySide6 import QtWidgets  # Importa el módulo QtWidgets de PySide6 para crear interfaces gráficas.
from PySide6.QtWidgets import QApplication, QWidget , QCompleter # Importa clases específicas de QtWidgets.
from src.controllers.login import login
from src.controllers.registrar_producto import ejecutar_ventana_registrar_producto

from src.controllers.registrar_producto import RegistarProducto
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #login(self)
        ejecutar_ventana_registrar_producto(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RegistarProducto()
    widget.show()
    sys.exit(app.exec_())
    """
    Punto de entrada principal de la aplicación.
    
    app = QApplication(sys.argv)  # Crea una instancia de la aplicación.
    app.setStyle("Fusion")  # Cambia el estilo de la aplicación
    widget = Widget() # Crea una instancia de la clase Widget (ventana principal).
    widget.show()  # Muestra la ventana principal.
    sys.exit(app.exec())  # Inicia el bucle de eventos y espera a que la aplicación se cierre.
    """