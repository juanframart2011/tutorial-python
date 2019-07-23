import sqlite3, datetime

print( "*** Programas para insertar registros en la tabla test ***" )

cadena_texto = input( "Introduzca una cadena de texto" )
entero = input( "Introduzca un número entero" )
decimal = input( "Introduzca un número decimal" )

try:

    entero = int( entero )
except ValueError:

    print( entero, "Entero no es un número entero" )
    exit()

try:

    decimal = float( decimal ) or int( decimal )
except ValueError:

    print( decimal, "Decimal no es un número decimal" )
    exit()

#Establecer la conexión
conexion = sqlite3.connect( "sqlite3/test.sqlite3" )
consulta = conexion.cursor()

#Valor de los argumentos
argumentos = (cadena_texto, entero, decimal, datetime.date.today() )

#Consulta
sql = """
INSERT INTO test(cadena_texto, entero, decimal, fecha)
VALUES ( ?, ?, ?, ? )
"""

if( consulta.execute( sql, argumentos ) ):
    print( "Se inserto los datos exitosamente" )
else:
    print( "No Se inserto los datos exitosamente" )

consulta.close()
conexion.commit()
conexion.close()
