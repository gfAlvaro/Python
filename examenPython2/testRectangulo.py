#_*_ coding=UTF-8 _*_
# testRectangulo.py
# programa de prueba para la clase Rectangulo
# @author Álvaro García Fuentes

from Rectangulo import Rectangulo

# Creamos un rectangulo, mostramos sus datos y lo dibujamos
try:
    rectangulo1 = Rectangulo( 4 , 2 )
    print(  "Se ha creado el rectangulo1 con alto=" + str( rectangulo1.alto ) + " y ancho=" + str( rectangulo1.ancho )  )
    print( rectangulo1 )
except ArithmeticError:
    print( "ERROR: no se pudo crear rectangulo1, valores fuera de rango." )

# Intentamos crear otro rectángulo dándole valores fuera del rango
try:
    rectangulo2 = Rectangulo( -1 , 11 )
    print( rectangulo2 )
except ArithmeticError:
    print( "ERROR: no se pudo crear rectangulo2, valores fuera de rango." )

# Fin del programa
