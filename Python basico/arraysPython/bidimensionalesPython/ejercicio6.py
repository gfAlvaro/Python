# -*- coding: utf-8 -*-
# Ejercicio6.py
# Modificacion del programa anterior de tal forma
# que no se repite ningún número en el array.
# @author Alvaro Garcia Fuentes

from random import randrange

array = [  [ 0 for i in range( 10 ) ] for j in range( 6 )  ]
for i in range( 6 ):
    j = 0
    while j < 10:        
        array[i][j] = randrange( 1001 )        
        repetido = False
             
        for k in range( i + 1 ):
            for l in range( j ):                                
                repetido = ( array[i][j] == array[k][l] )
                
                if ( repetido ):
                    break
                             
            if( repetido ):
                break
            
        if( not repetido ):
            j += 1

maximo = [0,0]
minimo = [0,0]
for i in range( 6 ):
    for j in range( 10 ):
        if( array[i][j] > array[maximo[0]][maximo[1]] ):
            maximo = [i,j]
        if( array[i][j] < array[minimo[0]][minimo[1]] ):
            minimo = [i,j]
        print( array[i][j] , end=" " )
    print()
    
print ( "Maximo en [" , maximo[0] , "][" , maximo[1] , "]:" , array[maximo[0]][maximo[1]] )
print ( "Minimo en [" , minimo[0] , "][" , minimo[1] , "]:" , array[minimo[0]][minimo[1]] )

# Fin del programa