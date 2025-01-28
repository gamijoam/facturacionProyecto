import mysql.connector
from src.database import conexion_db

class Ingresar_producto:
    def __init__(self, database):
        self.database = database
    
    def ingresar_producto(self, nombre, codigo_barras, descripcion, precio_compra, stock_actual, id_categoria, id_proveedor, iva, precio_final):
        try:
            instacia_conexion = conexion_db.Conexion()
            conexion = instacia_conexion.conexion(self.database)
            cursor = conexion.cursor()
            consulta = "INSERT INTO productos (nombre, codigo_barras, descripcion, precio_compra, stock_actual, id_categoria, id_proveedor, iva, precio_final) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(consulta, (nombre, codigo_barras, descripcion, precio_compra, stock_actual, id_categoria, id_proveedor, iva, precio_final))
            conexion.commit()
            print("Producto ingresado correctamente")
        except mysql.connector.Error as error:
            print(error)
        finally:
            if "cursor" in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()

    def consultar_tabla_proveedores(self, proveedor):
        try:
            instacia_conexion = conexion_db.Conexion()
            conexion = instacia_conexion.conexion(self.database)
            cursor = conexion.cursor()
            consulta = "SELECT nombre FROM proveedores"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            consulta2 = "SELECT id_proveedores, nombre FROM proveedores WHERE nombre = %s"
            cursor.execute(consulta2, (proveedor,))
            resultado2 = cursor.fetchall()
            lista_nombres = [item for item in resultado]
            return lista_nombres, resultado2
        except mysql.connector.Error as error:
            print(error)
            # Devolver dos listas vacías en caso de error
            return [], []
        finally:
            if "cursor" in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
    
    def consultar_tabla_categorias(self, categoria):
        try:
            instacia_conexion = conexion_db.Conexion()
            conexion = instacia_conexion.conexion(self.database)
            cursor = conexion.cursor()
            consulta = "SELECT nombre FROM categorias"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            consulta2 = "SELECT id_categoria, nombre FROM categorias WHERE nombre = %s"
            cursor.execute(consulta2, (categoria,))
            resultado2 = cursor.fetchall()
            lista_nombres = [item for item in resultado]
            return lista_nombres, resultado2
        except mysql.connector.Error as error:
            print(error)
            # Devolver dos listas vacías en caso de error
            return [], []
        finally:
            if "cursor" in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()