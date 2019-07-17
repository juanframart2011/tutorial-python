import glob, os.path

#Glob permite indexar en la ruta seleccionada para examinar los archivos y documentos que contiene

#Path es un submodulo de os, que nos permite entre otras cosas saber si un archivo o carpeta existe en la ruta indicada

todos = glob.glob( "directorio/*" )
print( "todos los archivos y carpetas que se encuentra en el directorio", todos )

archivos = []
carpetas = []
txt = glob.glob( "directorio/*.txt" )
txt3_char = glob.glob( "directorio/???.txt" )

for element in todos:
    if( os.path.isfile( element ) ):

        archivos.append( element )
    elif( os.path.isdir( element ) ):

        carpetas.append( element )
        
print( "\n Todos los archivos: ", archivos )
print( "\n Todas las carpetas: ", carpetas )
print( "\n Todos archivos TXT: ", txt )
print( "\n Todos los archivos de 3 char: ", txt3_char )
