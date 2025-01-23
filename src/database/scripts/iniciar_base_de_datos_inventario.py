import mysql.connector

# Configuración de la conexión a MariaDB
config = {
    'host': 'localhost',      # Dirección del servidor de MariaDB
    'user': 'user_sistema',     # Nombre de usuario de la base de datos
    'password': '12345',  # Contraseña del usuario
    'database': 'bd_aprendizaje',  # Nombre de la base de datos
    'charset':"utf8mb4",  # Usar UTF-8
    'collation': "utf8mb4_unicode_ci",  # Colación compatible con MariaDB
    'port': "3307"              # Puerto del servidor
}

# Función para ejecutar un archivo SQL
def ejecutar_archivo_sql(ruta_archivo, cursor, conexion):
    """
    Ejecuta un archivo SQL en la base de datos.

    """
    try:
        # Abrir el archivo SQL
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Leer el contenido del archivo
            sql = archivo.read()

            # Ejecutar las sentencias SQL (separadas por punto y coma)
            for sentencia in sql.split(';'):
                if sentencia.strip():  # Ignorar líneas vacías
                    cursor.execute(sentencia)

        # Confirmar los cambios en la base de datos
        conexion.commit()
        print("✅ Archivo SQL ejecutado correctamente.")

    except mysql.connector.Error as err:
        # Revertir cambios en caso de error
        conexion.rollback()
        print(f"❌ Error al ejecutar el archivo SQL: {err}")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")

# Conectar a la base de datos
try:
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()
    print("✅ Conexión a la base de datos establecida.")

    ruta_archivo_sql = 'bd_inventario2.sql'

    # Ejecutar el archivo SQL
    ejecutar_archivo_sql(ruta_archivo_sql, cursor, conexion)

except mysql.connector.Error as err:
    print(f"❌ Error al conectar a la base de datos: {err}")

finally:
    # Cerrar el cursor y la conexión
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion:
        conexion.close()
    print("✅ Conexión cerrada.")