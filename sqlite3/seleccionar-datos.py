import sqlite3

conexion = sqlite3.connect( "sqlite3/test.sqlite3" )
consulta = conexion.cursor()
sql = """
SELECT * FROM test
"""

if( consulta.execute( sql ) ):
    rows = consulta.fetchall()
    for filas in rows:
        print( "ID => " , filas[0] )
        print( "Cadena => " , filas[1] )
        print( "Entero => " , filas[2] )
        print( "Decimal => " , filas[3] )
        print( "Fecha => " + filas[4] )

sql = "SELECT * FROM test"

consulta.close()

conexion.commit()
conexion.close()
