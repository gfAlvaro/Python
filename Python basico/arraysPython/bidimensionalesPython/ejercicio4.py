# -*- coding: utf-8 -*-
# Ejercicio4.py
# Modificacion del programa anterior de tal forma
# que las sumas parciales y la suma total
# aparecen en la pantalla con un pequeño retardo,
# dando la impresión de que el ordenador
# se queda “pensando” antes de mostrar los números.
# @author Alvaro Garcia Fuentes

from time import sleep

# entrada de datos
numeros = [  [ 0 for i in range( 5 ) ] for j in range( 4 )  ]
for i in range( 4 ):
    for j in range( 5 ):
        numeros[i][j] = int(  input( f"Elemento [{i}][{j}]: " )  )
print()

# Se muestra el array con las sumas parciales y la total
ultimaFila = []
suma = 0
for i in range( 4 ):
    sumaFila = 0
    for j in range( 5 ):
        print( numeros[i][j] , end="  " )
        sumaFila = sumaFila + numeros[i][j]
    sleep( 1 )
    print( sumaFila )
    suma = suma + sumaFila

for i in range( 5 ):
    sumaColumna = 0
    for j in range( 4 ):
        sumaColumna = sumaColumna + numeros[j][i]
    sleep( 1 )
    print( sumaColumna , end=" " )

sleep( 1 )
print( suma )

# Fin del programa