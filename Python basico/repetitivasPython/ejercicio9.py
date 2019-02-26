# ejercicio9.py
# Mostrar en pantalla los N primeros número primos.
# Se pide por teclado la cantidad de números primos que queremos mostrar.
# @author Alvaro Garcia Fuentes

N = (  int( input( "Introduzca la cantidad de numeros primos a mostrar: " ) )  )

i = 0
cuenta = 0
while( True ):
    i = i + 1
    primo = True
    if( i > 3 ):
        for j in range( 2, i ):
            if(  ( i % j ) == 0  ):
                primo = False
                break
    if( primo ):
        print( i , end=" " )
        cuenta = cuenta + 1
    if( cuenta == N ):
        break
print()

#Fin del programa