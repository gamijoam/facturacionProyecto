import mysql.connector
from src.database import conexion_db

class Buscar_producto:
    def __init__(self,database):
        self.database = database

    def buscador_de_producto(self):
        try:
            instacia_conexion = conexion_db.Conexion()
            conexion = instacia_conexion.conexion(self.database)
            cursor = conexion.cursor()
            consulta = 'SELECT nombre FROM PRODUCTOS'
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            lista_resultado = [item[0] for item in resultado ]
            if resultado == []:
                print("No hay resultados")
            else:
                print(resultado)
                print(lista_resultado)

        except mysql.connector.Error as error:
            print(error)
        finally:
            if "cursor" in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
            return lista_resultado

#hu = Buscar_producto()
#hu.buscador_de_producto('inventario')