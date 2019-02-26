# _*_ coding=utf-8 _*_
# matematica.py
# Funciones de la biblioteca matemática
# @author Alvaro Garcia Fuentes
# @version 1.0
from builtins import str

# funcion que comprueba si un numero es primo
# @param numero
# @return boolean
def esPrimo( numero ):
    resultado = True
        
    for i in range( 2 , numero ):
        if ( numero % i ) == 0 :
            resultado = False
            break
        
    return resultado;

# funcion que devuelve el siguiente numero primo al entero dado
# @param numero
# @return int
def siguientePrimo( numero ):

    contador = numero + 1

    while esPrimo( contador ) == False:
        contador = contador + 1
    resultado = contador
        
    return resultado
    
#funcion que devuelve la potencia de un numero real dados su base
# y exponente
# @param base
# @param exponente
# @return float
def potencia( base , exponente ):
    return base**exponente
    
# funcion que cuenta cuántos dígitos tiene un numero entero
# @param numero
# @return int
def digitos( numero ):
    return len(  str( numero )  )
    
# funcion que voltea las cifras de un número, quedando estas invertidas
# @param numero
# @return int
# @see digitos( numero ), potencia( base , exponente )
def voltea( numero ):
        
    cadenaNum = str( numero )
    resultado = 0
    
    for i in range( 0 , digitos(numero) ):
        resultado += int( cadenaNum[i] ) * 10**i
        
    return resultado

# funcion que comprueba si un numero es capicua
# @param numero
# @return boolean
# @see voltea(int)
def esCapicua( numero ):
    return numero == voltea( numero )
    
# funcion que devuelve el digito que esta
# en la posicion N de un numero entero
# AVISO: Si N no es menor o igual a la cantidad de digitos del numero
#        devuelve -1
# @param numero
# @param N
# @return int
def digitoN( numero , N ):

    if N <= digitos( numero ) :
        return int(str( numero )[N])

    else:
        # Si N es mayor a la cantidad de dígitos,
        # se devuelve -1 como valor de error
        return -1
    
# funcion que da la posición de la primera ocurrencia de un dígito
# dentro de un número entero. Si no se encuentra, devuelve -1.
# @param numero
# @param digito
# @return int
def posicionDeDigito( numero , digito ):
        
    resultado = -1
    cifras = digitos( numero )
        
    if ( digito >= 0 ) and ( digito <= cifras ) :
        for i in range( 0 , cifras ):
            if digito == digitoN( numero , i ) :
                resultado = i
        
    return resultado

# funcion que le quita a un número n dígitos por detrás (por laderecha).
# @param numero
# @param n
# @see potencia(int, int), quitaPorDelante(int, int)
# @return int
def quitaPorDetras( numero , n ):
    return numero / potencia( 10 , n )
    
# funcion que le quita a un número n dígitos por delane (por la izquierda).
# @param numero
# @param n
# @return int
# @see potencia(base, exponente), quitaPorDetras(int, int)
def quitaPorDelante( numero , n ):
    return numero % potencia( 10 , n )

# Añade un digito a un numero por detras
# AVISO: el parametro digito debe estar entre 0 y 9, ambos inclusives
# @param numero
# @param digito
# @return int
# @see pegaPorDelante(int, int)
def pegaPorDetras( numero , digito ):
    return numero * 10 + digito
    
# Funcion que añade un digito a un numero por delante
# @param numero
# @param digito
# @return int
# @see pegaPorDetras(int, int)
# @see potencia(int, int)
def pegaPorDelante( numero , digito ):        
    return numero + digito * potencia(  10 , digitos( numero )  )

# pega dos numeros para formar uno
# @param numero1
# @param numero2
# @return int
def juntaNumeros( numero1 , numero2 ):
    return numero1 * potencia(  10 , digitos( numero2 )  ) + numero2
    
# funcion que toma como parámetros las posiciones inicial y final dentro de un numero
# y devuelve el trozo correspondiente
# @param numero
# @return
# @see juntaNumeros(int, int)
def trozoDeNumero( numero ):
    return juntaNumeros(  numero / potencia( 10 , digitos( numero ) - 1 ) , numero % 10  )

# Fin de la biblioteca
