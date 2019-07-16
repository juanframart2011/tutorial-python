class Persona():

    #metodo constructor
    def __init__( self ):

        #Propiedad privadas
        self.__nombre = "Lionel Messi"
        self.__pais = "Argentina"

        #Propiedad Pública
        self.sexo = ["masculino", "Femenino"]

    def nombre( self, nombre='' ):

        if( nombre != '' ):
            return nombre
        else:
            return self.__nombre

    def pais( self, pais='' ):

        if( pais != '' ):
            return pais
        else:
            return self.__pais

    def edad( self, edad=0 ):

        return edad

    def estatura( self, estatura=0 ):

        return estatura / 100

    def peso( self, peso= 0 ):

        return peso
