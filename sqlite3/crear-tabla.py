import sqlite3

#Contectar a la base de datos
conexion = sqlite3.connect( "sqlite3/test.sqlite3" )

#Seleccionar el cursor para realizar una consulta
consulta = conexion.cursor()

#Crear tabla
sql = """
CREATE TABLE IF NOT EXISTS test(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
cadena_texto VARCHAR(50) NOT NULL,
entero INTEGER NOT NULL,
decimal FLOAT NOT NULL,
fecha DATE NOT NULL
)
"""

#Ejecutar la consulta
if( consulta.execute( sql ) ):

    print( "tabla creada con éxito" )
else:
    print( "A ocurrido un error al crear la tabla" )

#Guardamos los cambios a la base de datos
consulta.close()

#Cerramos la conexión a la base de datos
conexion.commit()

#Cerramos conexión a base de datos
conexion.close()
