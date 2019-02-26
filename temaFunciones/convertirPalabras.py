# _*_ coding=utf-8 _*_
# Crea una función que convierta en palabras las cifras de un numero.
# Utiliza esta función en un programa para comprobar que funciona bien. Desde
# la función no se debe mostrar nada por pantalla, solo se debe usar print desde
# el programa principal. Fíjate que hay una coma detrás de cada palabra salvo
# al final.
# @author Álvaro García Fuentes
    
# Función auxiliar para ser usada
# dentro de convierteEnPalabras.
# La cadena devuelta es la transcripción
# a texto del entero de entrada
# @param k
# @return String
def sacarCifra( k ):
        
    cadena = ""
        
    if (k == 1 ):
        cadena = "uno"

    elif (k == 2 ):
        cadena = "dos"

    elif (k == 3 ):
        cadena = "tres"
        
    elif (k == 4 ):
        cadena = "cuatro"

    elif (k == 5 ):
        cadena = "cinco"

    elif (k == 6 ):
        cadena = "seis"

    elif (k == 7 ):
        cadena = "siete"

    elif (k == 8 ):
        cadena = "ocho"

    elif (k == 9 ):
        cadena = "nueve"
        
    else:
        cadena = "cero"

    return cadena
    
# Convierte los dígitos de un número en las correspondientes
# palabras y lo devuelve todo en una cadena de caracteres.
# @param n
# @return String
def convierteEnPalabras( n ):
        
    listaCifras = str( n )
    cadena = ""
        
    for i in range( 0 , len( listaCifras ) ):
            
        cadena += listaCifras[i]
            
        if i < (  len( listaCifras ) - 1  ) :
            cadena += ", "

        
    return cadena
    
#Programa principal                
print(  convierteEnPalabras( 470213 )  )

# Fin del programa