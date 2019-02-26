# ejercicio4.py
# Escribir un programa que imprima todos
# los números pares entre dos números que se le pidan al usuario.
# @author Alvaro Garcia Fuentes

# entrada de datos
numero1 = (  int( input( "Introduzca el primer número: " ) )  )
numero2 = (  int( input( "Introduzca el segundo número: " ) )  )

# validar numeros
if( numero1 > numero2 ):
    aux = numero1
    numero1 = numero2
    numero2 = aux
    
# imprimir todos los pares entre los numeros dados
for i in range(  numero1 , ( numero2 + 1 )  ):
    if( i%2 == 0 ):
        print( i , end=" " )
print()

# Fin del programa