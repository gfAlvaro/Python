# -*- coding: utf-8 -*-
# ejercicio10.py
# Algoritmo que pide los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
# circunferencias y las clasifica en uno de estos estados:
#    exteriores
#    tangentes exteriores
#    secantes
#    tangentes interiores
#    interiores
#    concéntricas
# @author Alvaro Garcia Fuentes

from math import sqrt

print( "Primera  circunferencia." )
x1 = (  float( input( " x1: " ) )  )
y1 = (  float( input( " y1: " ) )  )
r1 = (  float( input( " r1: "  ))  )

print( "Segunda  circunferencia." )
x2 = (  float( input( " x2: " ) )  )
y2 = (  float( input( " y2: " ) )  )
r2 = (  float( input( " r2: " ) )  )

distancia = (  sqrt( ( x2-x1 )**2 + ( y2-y1 )**2 )  )
sumaRadios = r1+r2
restaRadios = abs( r1-r2 )

if( distancia == 0 ):
    circunferencias = "concéntricas"
    
elif( distancia > sumaRadios ):
    circunferencias = "exteriores"

elif( distancia == sumaRadios ):
    circunferencias = "tangentes exteriores"

elif(  ( distancia < sumaRadios ) and ( distancia > restaRadios )  ):
    circunferencias = "secantes"

elif( distancia == restaRadios ):
    circunferencias = "tangentes interiores"

elif( distancia < restaRadios ):
    circunferencias = "interiores"

print( "Las circunferencias son" , circunferencias )
    
# Fin del programa