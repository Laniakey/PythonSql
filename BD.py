import sqlite3
from sqlite3 import Error

conn = None
BD_NAME = 'students.db'

def crear_conexion():
    global conn
    try:
        conn = sqlite3.connect(BD_NAME)
    except Error as e:
        print(e)

def cerrar_conexion():
    global conn
    conn.close()

def monstrar_todo():
    crear_conexion()
    if not conn:
        print("No se pudo acceder a la conexion")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Estudiantes")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cerrar_conexion()

def agregar_estudiante(nombre,matricula,indice):
    crear_conexion()
    if not conn:
        print("No se pudo acceder a la conexion")
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Estudiantes (nombre, matricula, indice) VALUES (?,?,?)",(nombre,matricula,indice))
    conn.commit()
    cerrar_conexion()

#agregar_estudiante("luis","2020-1239",2.4)
monstrar_todo()