# ejercicio4.py
# Programa que pide al usuario dos números
# y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.
# @author Alvaro Garcia Fuentes

numero1 = (  int( input( "Introduzca el primer numero: " ) )  )
numero2 = (  int( input( "Introduzca el segundo numero: " ) )  )

if(numero2 != 0):
    print(  "Division:", ( numero1/numero2 )  )
else:
    print( "ERROR: division por cero." )

# Fin del programa