# ejercicio11.py
# Programa que lee 3 datos de entrada A, B y C.
# Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa determina que tipo de triangulo es,
# teniendo en cuenta los siguiente:
#    Si se cumple Pitágoras entonces es triángulo rectángulo
#    Si sólo dos lados del triángulo son iguales entonces es isósceles.
#    Si los 3 lados son iguales entonces es equilátero.
#    Si no se cumple ninguna de las condiciones anteriores, es escaleno.
# @author Alvaro Garcia Fuentes

from math import sqrt

# Entrada de datos
A = (  float( input( "Introduzca el lado A: " ) )  )
B = (  float( input( "Introduzca el lado B: " ) )  )
C = (  float( input( "Introduzca el lado C: " ) )  )

# Paso previo para calcular Pitagoras
if(  ( B > A ) and ( B > C )  ):
    aux = A
    A = B
    B = aux
elif(  ( C > A ) and ( C > B )  ):
    aux = A
    A = C
    C = aux   

# Pitagoras (rectangulo)
pitagoras = (  A == sqrt( B**2 + C**2 )  )
if( pitagoras ):
    triangulo = "rectángulo"
# dos lados iguales (isosceles)
elif(  ( A==B and A!=C ) or ( A==C and A!=B ) or ( C==B and C!=A )  ):
    triangulo = "isósceles"
# tres lados iguales (equilatero)
elif( A==B and A==C ):
    triangulo = "equilatero"
# no se cumplen los anteriores (escaleno)
else:
    triangulo = "escaleno"

print( "Es un triangulo" , triangulo )

# Fin del programa