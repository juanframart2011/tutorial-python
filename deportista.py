from poo import Persona

class Deportista( Persona ):

    def deporte( self, deporte ):
        return deporte

    def detener( self ):
        return "El deportista está detenido"

    def correr( self ):
        return "el deportista esta corriendo"

    #Metodo privado
    def __metodo_privado( self ):
        return pass
