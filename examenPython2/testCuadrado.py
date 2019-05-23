#_*_ coding=UTF-8 _*_
# testCuadrado.py
# programa de prueba para la clase Cuadrado
# @author Álvaro García Fuentes

from Cuadrado import Cuadrado

# Intentamos crear un cuadrado con lado fuera del rango
try:
    cuadrado = Cuadrado( -1 )
    print(  "Creado cuadrado con lado=" + str( cuadrado.lado )  )
except ArithmeticError:
    print( "ERROR: No se pudo crear el cuadrado, lado fuera de rango." )

# Creamos cuadrados, los comparamos y los dibujamos
try:
    cuadrado1 = Cuadrado( 3 )
    print(  "Creado cuadrado1 con lado=" + str( cuadrado1.lado )  )
    cuadrado2 = Cuadrado( 3 )
    print(  "Creado cuadrado2 con lado=" + str( cuadrado2.lado )  )
    if( cuadrado1 == cuadrado2 ):
        print( "cuadrado1 y cuadrado2 son iguales" )
    print( cuadrado1 )
    print( cuadrado2 )
except ArithmeticError:
    print( "ERROR: No se pudieron crear los cuadrados." )

try:
    cuadrado3 = Cuadrado( 4 )
    print(  "Creado cuadrado3 con lado=" + str( cuadrado3.lado )  )
    cuadrado4 = Cuadrado( 3 )
    print(  "Creado cuadrado4 con lado=" + str( cuadrado4.lado )  )
    if( cuadrado3 > cuadrado4 ):
        print( "cuadrado3 es mayor que cuadrado5" )
    print( cuadrado3 )
    print( cuadrado4 )
except ArithmeticError:
    print( "ERROR: No se pudieron crear los cuadrados." )

try:
    cuadrado5 = Cuadrado( 4 )
    print(  "Creado cuadrado5 con lado=" + str( cuadrado5.lado )  )
    cuadrado6 = Cuadrado( 5 )
    print(  "Creado cuadrado6 con lado=" + str( cuadrado6.lado )  )
    if( cuadrado5 < cuadrado6 ):
        print( "cuadrado5 es menor que cuadrado6" )
    print( cuadrado5 )
    print( cuadrado6 )
except ArithmeticError:
    print( "ERROR: No se pudieron crear los cuadrados." )

try:
    cuadrado7 = Cuadrado( 4 )
    print(  "Creado cuadrado7 con lado=" + str( cuadrado7.lado )  )
    cuadrado8 = Cuadrado( 3 )
    print(  "Creado cuadrado8 con lado=" + str( cuadrado8.lado )  )
    if( cuadrado7 >= cuadrado8 ):
        print( "cuadrado7 es mayor o igual que cuadrado8" )
    print( cuadrado7 )
    print( cuadrado8 )
except ArithmeticError:
    print( "ERROR: No se pudieron crear los cuadrados." )

try:
    cuadrado9 = Cuadrado( 4 )
    print(  "Creado cuadrado9 con lado=" + str( cuadrado9.lado )  )
    cuadrado10 = Cuadrado( 5 )
    print(  "Creado cuadrado10 con lado=" + str( cuadrado10.lado )  )
    if( cuadrado9 <= cuadrado10 ):
        print( "cuadrado9 es menor o igual que cuadrado10" )
    print( cuadrado9 )
    print( cuadrado10 )
except ArithmeticError:
    print( "ERROR: No se pudieron crear los cuadrados." )

try:
    cuadrado11 = Cuadrado( 1 )
    print(  "Creado cuadrado11 con lado=" + str( cuadrado11.lado )  )
    cuadrado12 = Cuadrado( 2 )
    print(  "Creado cuadrado12 con lado=" + str( cuadrado12.lado )  )
    if( cuadrado11 != cuadrado12 ):
        print( "cuadrado11 no es igual que cuadrado12" )
    print( cuadrado11 )
    print( cuadrado12 )
except ArithmeticError:
    print( "ERROR: No se pudieron crear los cuadrados." )

# Fin del programa
