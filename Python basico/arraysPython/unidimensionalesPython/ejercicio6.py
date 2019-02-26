# -*- coding: utf-8 -*-
# ejercicio6.py
# Programa que lee 15 números por teclado y los almacena en un
# array. Rota los elementos de ese array, es decir, el elemento de la posición 0
# debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en
# la última posición pasa a la posición 0. Finalmente, muestra el contenido del array.
# @author Alvaro Garcia Fuentes

# entrada de datos
numeros = []
print( "Introduzca quince números consecutivamente: " )
for i in range( 15 ):
    numeros.append(  int( input() )  )

# rotar numeros del array
aux=numeros[ 14 ]
for i in range( 14 , 0 , -1 ):
    numeros[i] = numeros[i-1]
numeros[0] = aux

# mostrar resultado
for i in range( 15 ):
        print( numeros[i] , end=" " )
		
# Fin del programa