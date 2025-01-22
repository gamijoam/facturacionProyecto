'''self.items = [
            {"producto": "Manzana", "cantidad": "5", "precio": "1.000"},
            {"producto": "Banana", "cantidad": "3", "precio": "500"},
            {"producto": "Naranja", "cantidad": "2", "precio": "800"},
        ]
        # Agregar los ítems a la tabla
        for item in self.items:
            row_position = self.ui_ventana_facturacion.tableWidget.rowCount()
            self.ui_ventana_facturacion.tableWidget.insertRow(row_position)

            self.ui_ventana_facturacion.tableWidget.setItem(row_position, 0, QTableWidgetItem(item["producto"]))
            self.ui_ventana_facturacion.tableWidget.setItem(row_position, 1, QTableWidgetItem(item["cantidad"]))
            self.ui_ventana_facturacion.tableWidget.setItem(row_position, 2, QTableWidgetItem(item["precio"]))'''

# def borrar_busqueda(self):
#    self.ui_ventana_facturacion.lineEdit.clear()


