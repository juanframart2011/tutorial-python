import os

def init():

    print( "*** Administrar Archivos y Carpetas ***" )
    option = input( "Seleccione una opción:\ c => Crea \n e => Eliminar: " )
    if( option == "c" ):

        print( "Vamos a crear carpeta \n" )
        ruta = input( "Indique una ruta. \n Si no es una ruta será la ruta actual: " )

        if( ruta == "" ):

            ruta = os.getcwd() + "\\"
        elif( os.path.isdir( ruta ) ):#Validamos si la ruta existe

            tipo = input( "indique el tipo: \n a => Archivo \n c => Carpeta" )

            if( tipo == "a" ):

                archivo = input( "indique nombre de archivo: " )
                manejador = open( ruta + archivo, "w" )
                manejador.close()

                print( "Archivo creado con éxito" )
            elif( tipo == "c" ):

                carpeta = input( "indique nombre de carpeta: " )
                os.mkdir( ruta + carpeta )

                print( "Carpeta creada con éxito" )
            else:
                init()
    elif( option == "e" ):

        print( "Vamos a eliminar carpeta \n" )
        ruta = input( "Indique una ruta. \n Si no es una ruta será la ruta actual: " )

        if( ruta == "" ):

            ruta = os.getcwd() + "\\"
        elif( os.path.isdir( ruta ) ):#Validamos si la ruta existe

            tipo = input( "indique el tipo: \n a => Archivo \n c => Carpeta" )

            if( tipo == "a" ):

                archivo = input( "indique nombre de archivo a eliminar: " )
                os.remove( ruta + archivo )

                print( "Archivo eliminada con éxito" )
            elif( tipo == "c" ):

                carpeta = input( "indique nombre de carpeta a eliminar:: " )
                os.rmdir( ruta + carpeta )

                print( "Carpeta eliminada con éxito" )
            else:
                init()
    else:
        init()
