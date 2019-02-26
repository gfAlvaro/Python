# ejercicio5.py
# Programa que pide el limite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior lo vuelve a pedir. 
# A continuación se van introduciendo números hasta que introduzcamos el 0.
# Cuando termine el programa dará las siguientes informaciones:
#   La suma de los números que están dentro del intervalo (intervalo abierto).
#   Cuantos números están fuera del intervalo.
#   Informa si hemos introducido algún número igual a los límites del intervalo.
# @ author Alvaro Garcia Fuentes

# entrada de los limites del intervalo con validacion
while( True ):
    inferior = (  int( input( "Introduzca el limite inferior: " ) )  )
    superior = (  int( input( "Introduzca el limite superior: " ) )  )

    if( inferior > superior ):
        print( "ERROR: limite inferior mayor que el superior." )
    else:
        break

# entrada de los numeros comprobando si están o no en el intervalo
suma = 0
sumaFuera = 0
sumaIgual = 0
while( True ):
    
    numero = (  int( input( "Introduzca un numero: " ) )  )
    if( numero == 0 ):
        break
    
    if( numero > inferior and numero < superior ):
        suma = suma + 1
    elif( numero < inferior or numero > superior ):
        sumaFuera = sumaFuera + 1
    elif( numero == inferior or numero == superior ):
        sumaIgual = sumaIgual + 1

# mostrar resultado por pantalla
print( "Cantidad de números dentro del intervalo:" , suma )
print( "Cantidad de números fuera del intervalo:" , sumaFuera )
print( "Cantidad de números en los límites del intervalo:" , sumaIgual )

# Fin del programa