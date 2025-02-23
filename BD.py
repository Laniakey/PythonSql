import sqlite3
from sqlite3 import Error
def crear_conexion(db_students):
    
    """""
    La funcion 'crear_conexion' creara una base de datos sqlite
    y conectara con ella.
    :param db_file: La ruta y nombre de la base de datos a crear.
    :return :
    o es necesario retornar nada.
    """""
    conn = None
    # Intentamos crear nuestra base de datos
    try:
        conn = sqlite3.connect(db_students)
        print(sqlite3.version)
    # Si la conexion es exitosa mostramos la version
    except Error as e:
        print(e)
    #En caso de existir un error podemos recuperarlo.
    # Una buena practica es siempre cerrar la conexion a la base de datos al finalizar.
    finally:
        if conn:
            conn.close()
    #Cerramos la conexion a la base de datos.

crear_conexion(r'students.db')