#capturar errore try-except
entero = input( "número entero" )

try:
    entero = int( entero )
except ValueError:
    print( "no es un entero" )

print( entero )
