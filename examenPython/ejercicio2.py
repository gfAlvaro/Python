# _*_ coding=utf-8 _*_
# Ejercicio 2
# Pide un DNI, comprueba si es correcto
# y devuelve la letra
# @author Alvaro Garcia Fuentes

def validarDNI( dni ):
    
    salida = False
    if( len(dni) == 9 ):

        cuenta = int(dni[:8])
        resto = cuenta % 23        
        cadena = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                   'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]
        salida = ( cadena[resto] == dni[8] )
        
    return salida

def letraDNI( dni ):
    return dni[8]

#
# Programa principal
#
dni = raw_input( "Introduzca dni (8 numeros y 1 letra): " )

if( validarDNI( dni ) ):
    print( "El dni es valido" )
    letra = letraDNI( dni )
    print( "letra: " + letra )
else:        
    print( "El dni no es valido" )

