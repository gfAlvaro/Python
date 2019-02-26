# ejercicio3.py
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# @author Alvaro Garcia Fuentes

from math import sqrt

cateto1 = (  int( input( "Introduzca el primer cateto " ) )  )
cateto2 = (  int( input( "Introduzca el segundo cateto " ) )  )

hipotenusa = sqrt( cateto1**2 + cateto2**2 )

print( "La hipotenusa es " , hipotenusa )

# Fin del programa
