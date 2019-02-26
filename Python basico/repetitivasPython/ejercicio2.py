# ejercicio2.py
# Algoritmo que pide números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos
# son mayores que 0, menores que 0 e iguales a 0.
# @author Alvaro Garcia Fuentes

# entrada de datos
N = (  int( input( "Introduzca la cantidad de números a introducir: " ) )  )
lista = []
for i in range( 0 , N ):
    valor = (  int( input( "Introduzca " + str(i) + "er numero: " ) )  )
    lista.append( valor )
print( lista )

# comprobar los elementos de la lista
mayor = 0
menor = 0
igual = 0    
for i in range( 0 , N ):
    if( lista[i] > 0 ):
        mayor = mayor + 1
    elif( lista[i] < 0 ):
        menor = menor + 1
    else:
        igual = igual + 1
        
# mostrar el resultado
print( "Cantidad de numeros mayores que 0:" , mayor )
print( "Cantidad de numeros menores que 0:" , menor )
print( "Cantidad de ceros:" , igual )

# Fin del programa