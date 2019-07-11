#Función lista de argumentos indefenida
def argumentos( *arg ):
    for txt in arg:
        print( txt, end=" " )

argumentos(1,2,3,4,5,"Hellow")

print( "\n" )

#lambda nos permite crear funciones con una sola instrucción
restar = lambda num1, num2: num1 - num2
print( restar( 2, 1 ) )
