# _*_ coding=utf-8 _*_
# ejercicio15.py
# Programa que muestra los números primos que hay entre 1 y 1000.
# Se hace uso de la biblioteca matemática creada.
# @author Álvaro García Fuentes

from Matematica import siguientePrimo

k = 1

while k <= 1000 :
    print( k , end=" " )
    k = siguientePrimo( k )
print()

# Fin del programa