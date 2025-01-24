from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QStringListModel  # Importar QStringListModel
from PySide6.QtWidgets import QCompleter
from src.view.PY.ui_facturacion import Ui_Widget
from src.models.buscador_bd import Buscar_producto


class FacturacionWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Configurar la interfaz de usuario
        self.ui_ventana_facturacion = Ui_Widget()
        self.ui_ventana_facturacion.setupUi(self)

        # Configuración del ancho de las columnas de la tabla en la interfaz de facturación
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(0, 257)  # Ancho de la columna 1.
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(1, 257)  # Ancho de la columna 2.
        self.ui_ventana_facturacion.tableWidget.setColumnWidth(2, 257)  # Ancho de la columna 3.

        # Iniciar base de datos para buscar un producto
        self.buscar_producto = Buscar_producto('inventario')  # Conexión a base de datos

        # Configurar el QCompleter
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # Búsqueda no sensible a mayúsculas
        self.completer.setCompletionMode(QCompleter.PopupCompletion)  # Mostrar sugerencias en un popup

        # Asignar un QStringListModel al QCompleter
        self.completer_model = QStringListModel()
        self.completer.setModel(self.completer_model)

        # Conectar el QCompleter al QLineEdit
        self.ui_ventana_facturacion.lineEdit.setCompleter(self.completer)

        # Conectar la señal textChanged a la función actualizar_completer
        self.ui_ventana_facturacion.lineEdit.textChanged.connect(self.actualizar_completer)

        # Conectar la señal returnPressed a la función producto_seleccionado
        self.ui_ventana_facturacion.lineEdit.returnPressed.connect(self.producto_seleccionado)

    def actualizar_completer(self, texto):
        """
        Actualiza el QCompleter con los resultados de la base de datos.
        """
        if texto:  # Solo buscar si hay texto en el QLineEdit
            self.resultados = self.buscar_producto.buscador_de_producto(texto)
            if self.resultados:  # Si hay resultados
                # Convertir la lista de resultados a una lista de cadenas
                resultados_str = [str(item) for item in self.resultados[0]]
                self.completer_model.setStringList(resultados_str)  # Actualizar el modelo del QCompleter
            else:
                self.completer_model.setStringList([])  # Limpiar el QCompleter si no hay resultados
        else:
            self.completer_model.setStringList([])  # Limpiar el QCompleter si no hay texto

    def producto_seleccionado(self):
        """
        Método que se ejecuta cuando se presiona Enter en el QLineEdit.
        """
        # Obtener el texto ingresado en el QLineEdit
        selected_product = self.ui_ventana_facturacion.lineEdit.text()
        print(f"Producto seleccionado: {selected_product}")
        self.actualizar_datos_en_pantalla(self.resultados)

    def actualizar_datos_en_pantalla(self, lista_producto):
        """
        Actualiza la etiqueta en la interfaz con el texto proporcionado.
        """
        print(lista_producto[0][2])
        self.ui_ventana_facturacion.label_4.setText(lista_producto[0][0]) #Nombre Producto
        self.ui_ventana_facturacion.label.setText(lista_producto[0][1])  #Codigo de Barras
        self.ui_ventana_facturacion.label_7.setText(str(lista_producto[0][2])) #Precio
        self.ui_ventana_facturacion.label_11.setText(str(int(lista_producto[0][3])))

    #Seguir programando para que se muestren los datos en los Label , Falta stock, precio , iva etc



def facturacion(self):
    """
    Método que crea y muestra la ventana de facturación.
    """
    self.ventana_facturacion = FacturacionWindow()  # Crea una instancia de la ventana de facturación
    self.ventana_facturacion.show()  # Muestra la ventana de facturación