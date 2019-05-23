# _*_ coding=utf-8 _*_
# Ejercicio 1
# Devuelve un número de billetes
# en base al dinero introducido de forma ideal
# @author Alvaro Garcia Fuentes

# Pedir datos por pantalla
dinero = ( float( input( "Introduzca la cantidad de dinero: " ) ) )

# Calcular el número de billetes y monedas para cambio
billetes = []
tiposExistentes = []
tiposBilletesMonedas = [ 500, 200, 100, 50, 20, 10, 5,
                         2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]
for i in tiposBilletesMonedas:
    if( dinero >= i ):
        billetes.append(  ( int( dinero / i ) )  )
        tiposExistentes.append( i )
        dinero = dinero % i

# Mostrar cambio
print( "Cambio: " )
for i in range(  len( billetes )  ):
    if( tiposExistentes[i] > 2 ):
        print(  str( billetes[i] ) + " billetes de " + str( tiposExistentes[i] )  )
    else:
        print(  str( billetes[i] ) + " monedas de " + str( tiposExistentes[i] )  )
