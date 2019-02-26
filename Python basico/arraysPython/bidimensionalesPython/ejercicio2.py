# -*- coding: utf-8 -*-
# Ejercicio2.py
# Programa que pide 20 números enteros. Estos números se
# introducen en un array de 4 filas por 5 columnas. El programa mostrará las
# sumas parciales de filas y columnas igual que si de una hoja de cálculo se
# tratara. La suma total aparece en la esquina inferior derecha.

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
    print( sumaFila )
    suma = suma + sumaFila

for i in range( 5 ):
    sumaColumna = 0
    for j in range( 4 ):
        sumaColumna = sumaColumna + numeros[j][i]
    print( sumaColumna , end=" " )

print( suma )

# Fin del programa