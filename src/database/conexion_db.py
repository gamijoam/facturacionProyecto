import mysql.connector
class Conexion:
    def conexion(self,database):
        try:
            conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "GaboMac",
                database = database,
                port = "3306",
                charset = 'utf8mb4',
                collation = 'utf8mb4_unicode_ci')
            return conexion

        except mysql.connector.Error as error:
            print('Error con la base de datos')