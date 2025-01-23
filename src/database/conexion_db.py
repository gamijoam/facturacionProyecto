import mysql.connector
class Conexion:
    def conexion(self,database):
        try:
            conexion = mysql.connector.connect(
                host = "localhost",
                user = "user_sistema",
                password = "12345",
                database = database,
                port = "3307",
                charset = 'utf8mb4',
                collation = 'utf8mb4_unicode_ci')
            return conexion

        except mysql.connector.Error as error:
            print('Error con la base de datos')