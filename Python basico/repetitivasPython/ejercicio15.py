# ejercicio15.py
#Introducir una cadena de caracteres e indicar si es un palíndromo.
# Una palabra palíndroma es aquella que se lee igual adelante que atrás.
# @author Alvaro Garcia Fuentes

# entrada de datos
cadena = input( "Introduzca la cadena: " )

# obtener la cadena sin espacios y la cadena invertida
cadenaSinEspacios = []
cadenaInvertida = []
for i in range( len( cadena ) ):
    if( cadena[i] != ' ' ):
        cadenaSinEspacios.append( cadena[i] )
        
for i in range( len( cadenaSinEspacios ) ):
    cadenaInvertida.append(  cadenaSinEspacios[ len( cadenaSinEspacios ) - ( i + 1 ) ]  )

# comparar la cadena sin espacios y la cadena invertida
# y mostrar el resultado por pantalla
if( cadenaSinEspacios == cadenaInvertida ):
    print( "Es un palindromo." )
else:
    print( "No es un palindromo." )
