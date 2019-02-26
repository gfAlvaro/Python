# _*_ coding=utf-8 _*_
# ejercicio16.py
# ejercicio 16 de la pg 113 del libro de Java
# Muestra los números capicúa que hay entre 1 y 99999.
# Se hace uso de la biblioteca matemática creada
# @author Alvaro Garcia Fuentes

from Matematica import esCapicua
        
for i in range( 1 , 100000 ):

    if( esCapicua(i) == True ):
        print( i , end=" " )
        
print()

# Fin del programa