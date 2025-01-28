from PySide6 import QtWidgets
from src.view.PY.registrar_productos import Ui_Registrar_productos
from src.models.ingresar_productos_a_la_bd_inventario import Ingresar_producto

class RegistarProducto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.registrar_producto = Ui_Registrar_productos()
        self.registrar_producto.setupUi(self)
        self.ingresar_producto = Ingresar_producto('inventario')
        self.mostrar_proveedores()
        self.mostrar_categorias()
        self.registrar_producto.pushButton_3.clicked.connect(self.registrar_producto_bd)
        self.registrar_producto.comboBox_2.currentIndexChanged.connect(self.actualizar_proveedores)
        self.registrar_producto.comboBox.currentIndexChanged.connect(self.actualizar_categorias)
        # Conectar señales de textChanged a un método
        self.registrar_producto.lineEdit_3.textChanged.connect(self.actualizar_precio_total)
        self.registrar_producto.lineEdit_6.textChanged.connect(self.actualizar_precio_total)

    def mostrar_proveedores(self):
        # Obtener la lista de nombres de proveedores y descartar el segundo valor devuelto
        lista_nombre, _ = self.ingresar_producto.consultar_tabla_proveedores('')
        lista_proveedores = [item[0] for item in lista_nombre]
        self.registrar_producto.comboBox_2.clear()
        self.registrar_producto.comboBox_2.addItems(lista_proveedores)

    def mostrar_categorias(self):
        # Obtener la lista de nombres de categorías y descartar el segundo valor devuelto
        lista_categorias, _ = self.ingresar_producto.consultar_tabla_categorias('')
        lista_categorias = [item[0] for item in lista_categorias]
        self.registrar_producto.comboBox.clear()
        self.registrar_producto.comboBox.addItems(lista_categorias)

    def actualizar_proveedores(self):
        proveedor = self.registrar_producto.comboBox_2.currentText()
        # Obtener el segundo valor devuelto (listaProveedor2) y descartar el primero
        _, self.listaProveedor2 = self.ingresar_producto.consultar_tabla_proveedores(proveedor)

    def actualizar_categorias(self):
        categoria = self.registrar_producto.comboBox.currentText()
        # Obtener el segundo valor devuelto (listaCategoria2) y descartar el primero
        _, self.listaCategoria2 = self.ingresar_producto.consultar_tabla_categorias(categoria)

    def registrar_producto_bd(self):
        nombre = self.registrar_producto.lineEdit_2.text()
        codigo_barras = self.registrar_producto.lineEdit.text()
        descripcion = self.registrar_producto.textEdit.toPlainText()
        precio_compra = self.registrar_producto.lineEdit_3.text()
        stock_actual = self.registrar_producto.spinBox.value()
        iva = self.registrar_producto.lineEdit_6.text()
        precio_final = self.registrar_producto.lineEdit_5.text()
        self.ingresar_producto.ingresar_producto(nombre, codigo_barras, descripcion, precio_compra, stock_actual, self.listaCategoria2[0][0], self.listaProveedor2[0][0], iva, precio_final)
        self.registrar_producto.lineEdit.setText('')
        self.registrar_producto.lineEdit_2.setText('')
        self.registrar_producto.lineEdit_3.setText('')
        self.registrar_producto.lineEdit_4.setText('')
        self.registrar_producto.lineEdit_5.setText('')
        self.registrar_producto.lineEdit_6.setText('')
        self.registrar_producto.comboBox.clear()
        self.registrar_producto.comboBox_2.clear()
        self.registrar_producto.textEdit.clear()
        self.registrar_producto.spinBox.clear()
    def actualizar_precio_total(self):
        try:
            precio = float(self.registrar_producto.lineEdit_3.text())
            iva = float(self.registrar_producto.lineEdit_6.text())
            precio_total = precio + (precio * iva / 100)
            self.registrar_producto.lineEdit_5.setText(f"{precio_total:.2f}")
        except ValueError:
            self.registrar_producto.lineEdit_5.setText("")


def ejecutar_ventana_registrar_producto(self):
    self.ventana_registrarProducto = RegistarProducto()
    self.ventana_registrarProducto.show()