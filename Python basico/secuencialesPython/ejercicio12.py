# ejercicio12.py
# Pide al usuario dos pares de números x1,y2 y x2,y2,
# que representen dos puntos en el plano.
# Calcula y muestra la distancia entre ellos.
# @author Alvaro Garcia Fuentes

from math import sqrt

print( "Datos del primer punto." )
x1 = (  float( input( "Introduzca x1: " ) )  )
y1 = (  float( input( "Introduzca y1: " ) )  )
print()
print( "Datos del segundo punto." )
x2 = (  float( input( "Introduzca x2: " ) )  )
y2 = (  float( input( "Introduzca y2: " ) )  )

distancia = sqrt( ( x2 - x1 )**2 + ( y2 - y1 )**2 )

print( "Distancia:" , distancia )

# Fin del programa