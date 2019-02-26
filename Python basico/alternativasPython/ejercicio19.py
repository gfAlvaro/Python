# ejercicio19.py
# Programa que pide un número entero entre uno
# y doce e imprime el número de días que tiene el mes correspondiente.
# @author Alvaro Garcia Fuentes

mes =(  int( input( "Introduzca el mes: " ) )  )

if( mes in [1, 3, 5, 7, 8, 10, 12] ):
    print( "Tiene 31 días" )
elif( mes in [4, 6, 9, 11] ):
    print( "Tiene 30 días" )
elif( mes == 2 ):
    print( "Tiene 28 días o 29 si es un año bisiesto" )
else:
    print( "ERROR: mes incorrecto" )

# Fin del programa