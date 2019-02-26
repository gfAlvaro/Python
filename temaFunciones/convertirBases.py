# _*_ coding=utf-8 _*_
# ejercicio19.py
# Une y amplía los dos programas anteriores de tal forma que se permita
# convertir un número entre cualquiera de las siguientes bases: decimal, binario,
# hexadecimal y octal.
# @author Álvaro García Fuentes

from Matematica import digitos
from Matematica import potencia
from Matematica import digitoN
    
# funcion para pasar de binario a decimal
# @param binario
# @return int
def binarioDecimal( binario ):
        
    numero = 0
        
    for i in range(  0 , digitos( binario )  ):
        numero = numero + potencia(  2 , digitos( binario ) - i - 1  ) * digitoN( binario , i )

    return numero
    
# función para pasar de decimal a binario
# @param numero
# @return int
def decimalBinario( numero ):

    cociente = numero
    cadenaBinaria = ""

    while cociente != 1 :
        resto = cociente % 2
        cociente = int( cociente / 2 )
        cadenaBinaria = str( resto ) + cadenaBinaria
    
    cadenaBinaria = str( cociente ) + cadenaBinaria

    return int( cadenaBinaria )

# funcion para pasar de octal a decimal
# @param binario
# @return int
def octalDecimal( octal ):
        
    numero = 0
        
    for i in range(  0 , digitos( octal )  ):
        numero = numero + potencia( 8 , digitos( octal ) - i - 1 ) * digitoN( octal , i );
        
    return numero
    
# funcion para pasar de decimal a octal
# @param numero
# @return int
def decimalOctal( numero ):

    cociente = numero
    cadenaOctal = ""

    while( cociente != 1 ):
        resto = cociente % 8
        cociente = int( cociente / 8 )
        cadenaOctal = str( resto ) + cadenaOctal
        
    cadenaOctal = str( cociente ) + cadenaOctal

    return int( cadenaOctal )

# funcion para pasar de hexadecimal a decimal
# @param binario
# @return int
def hexadecimalDecimal( hexadecimal ):
        
    numero = 0;
        
    for i in range(  0 , len( hexadecimal )  ):
        
        if( hexadecimal[i] == 'A' ):
            cifra = 10
            
        elif( hexadecimal[i] == 'B' ):
            cifra = 11

        elif( hexadecimal[i] == 'C' ):
            cifra = 12
            
        elif( hexadecimal[i] == 'D' ):
            cifra = 13

        elif( hexadecimal[i] == 'E' ):
            cifra = 14

        elif( hexadecimal[i] == 'F' ):
            cifra = 15;

        else:
            cifra = int( hexadecimal[i] )
            
        numero = numero + potencia(  16 , len( hexadecimal ) - i - 1  ) * cifra;
        
    return numero
    
# funcion para psar de decimal a hexadecimal
# @param numero
# @return int
def decimalHexadecimal( numero ):

    cociente = numero
    cadenaHexadecimal = ""

    while( cociente >= 16 ):
        
        resto = cociente % 16
        cociente = int( cociente / 16 )

        if( resto == 10 ):
            cadenaHexadecimal = 'A' + cadenaHexadecimal
                
        elif( resto == 11 ):
            cadenaHexadecimal = 'B' + cadenaHexadecimal

        elif( resto == 12 ):
            cadenaHexadecimal = 'C' + cadenaHexadecimal

        elif( resto == 13 ):
            cadenaHexadecimal = 'D' + cadenaHexadecimal

        elif( resto == 14 ):
            cadenaHexadecimal = 'E' + cadenaHexadecimal
            
        elif( resto == 15 ):
            cadenaHexadecimal = 'F' + cadenaHexadecimal

        else:
            cadenaHexadecimal = str( resto ) + cadenaHexadecimal

    cadenaHexadecimal = str( cociente ) + cadenaHexadecimal

    return cadenaHexadecimal
    
# Programa principal        
numero = 1020
numero = decimalBinario( numero );
print( "numero en binario: " , numero )
numero = binarioDecimal( numero )
print( "numero en decimal: " , numero )        
numero = decimalOctal( numero )
print( "numero en octal: " , numero )
numero = octalDecimal( numero )        
cadenaHexadecimal = decimalHexadecimal( numero )
print( "numero en hexadecimal: " , cadenaHexadecimal )     
numero = hexadecimalDecimal( cadenaHexadecimal )
print( "decimal de nuevo: " , numero )

# Fin del programa