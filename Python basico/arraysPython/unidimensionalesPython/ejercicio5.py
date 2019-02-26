# -*- coding: utf-8 -*-
# ejercicio5.py
# Programa que pida 10 números por teclado y que luego muestre
# los números introducidos junto con las palabras “máximo” y “mínimo” al lado
# del máximo y del mínimo respectivamente.
# @author Alvaro Garcia Fuentes

# entrada de datos
numeros = []
print( "Introduzca diez números consecutivamente: " )
for i in range( 10 ):
    numeros.append(  int( input() )  )

# encontrar el maximo y el minimo
maximo = numeros[0]
minimo = numeros[0]
for i in range( 10 ):
    if numeros[i] > maximo:
        maximo = numeros[i]
    elif numeros[i] < minimo:
        maximo = numeros[i]

# mostrar resultado
for i in range( 10 ):
    if numeros[i] == maximo:
        print( numeros[i] , "Maximo" )
    elif numeros[i] == minimo:
        print( numeros[i] , "Minimo" )
    else:
        print( numeros[i] )

# Fin del programa