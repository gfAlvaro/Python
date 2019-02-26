# -*- coding: utf-8 -*-
# Ejercicio5.py
# Programa que rellena un array
# de 6 filas por 10 columnas con números enteros
# positivos comprendidos entre 0 y 1000 (ambos incluidos).
# A continuación, el programa da
# la posición tanto del máximo como del mínimo.
# @author Alvaro Garcia Fuentes

from random import randrange

array = [  [ 0 for i in range( 10 ) ] for j in range( 6 )  ]
for i in range( 6 ):
    for j in range( 10 ):
        array[i][j] = randrange( 1001 ) 

maximo = [0,0]
minimo = [0,0]
for i in range( 6 ):
    for j in range( 10 ):
        if( array[i][j] > array[maximo[0]][maximo[1]] ):
            maximo = [i,j]
        if( array[i][j] < array[minimo[0]][minimo[1]] ):
            minimo = [i,j]
        print( array[i][j],end=" " )
    print()
    
print ( "Maximo en [" , maximo[0] , "][" , maximo[1] , "]:" , array[maximo[0]][maximo[1]] )
print ( "Mínimo en [" , minimo[0] , "][" , minimo[1] , "]:" , array[minimo[0]][minimo[1]] )

# Fin del programa