import mysql.connector

class Buscar_producto:
    def __init__(self, database):
        self.host = 'localhost'
        self.user = 'user_sistema'
        self.password = '12345'
        self.database = database
        self.port = '3307'
        self.charset = 'utf8mb4'
        self.collation = 'utf8mb4_unicode_ci'

    def iniciar_conexion_bd(self):
        try:
            conexion = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                port = self.port,
                charset = self.charset,
                collation = self.collation)
            return conexion

        except mysql.connector.Error as error:
            print('Error con la base de datos')


    def buscador_de_producto(self):
        try:
            conexion = self.iniciar_conexion_bd()
            cursor = conexion.cursor()
            consulta = 'SELECT nombre FROM PRODUCTOS'
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            lista_resultado = [item[0] for item in resultado ]
            if resultado == []:
                print("No hay resultados")
            else:
                #print(resultado)
                #print(lista_resultado)
                return resultado

        except mysql.connector.Error as error:
            print(error)
        finally:
            if "cursor" in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
            return lista_resultado

#hu = Buscar_producto('inventario')
#hu.buscador_de_producto()