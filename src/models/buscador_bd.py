import mysql.connector
from src.database import conexion_db

class Buscar_producto:
    def __init__(self,database):
        self.database = database

    def buscador_de_producto(self, producto):
        try:
            instacia_conexion = conexion_db.Conexion()
            conexion = instacia_conexion.conexion(self.database)
            cursor = conexion.cursor()
            consulta = "SELECT nombre,codigo_barras,precio_compra,stock_actual FROM PRODUCTOS WHERE nombre LIKE %s"  # Usar LIKE para búsqueda parcial
            cursor.execute(consulta, (f'%{producto}%',))  # Buscar coincidencias parciales
            resultado = cursor.fetchall()
            lista_nombres =  [item for item in resultado]  # Extraer solo los nombres
            #print(lista_nombres)
            return lista_nombres
        except mysql.connector.Error as error:
            print(error)
            return []
        finally:
            if "cursor" in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()

#hu = Buscar_producto('inventario')
#hu.buscador_de_producto('p')