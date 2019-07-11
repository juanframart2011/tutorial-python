import modulo.matematicas

print( modulo.matematicas.sumar(2,1) )

#Ejemplo 2, accediendo al modulo a traves de un alias
import modulo.matematicas as m
print( "Ejemplo 2, accediendo al modulo a traves de un alias", m.restar(4,20) )

#Sin tener que poner alias
from modulo.matematicas import *
print( sumar(2,1) )

#importar solo funciones necesarias
from modulo.matematicas import sumar
print( sumar(2,1) )
