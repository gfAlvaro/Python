# _*_ coding=utf-8 _*_
# binarioADecimal.py
# ejercicio 17 pg. 114 del libro
# Programa que pasa de binario a decimal.
# Se usa la biblioteca matemática creada.
# @author Álvaro García Fuentes

import Matematica

def binarioDecimal( binario ):
        
    numero = 0
    cifras = Matematica.digitos( binario )
    
    for i in range(  0 , cifras  ):
        numero = numero + Matematica.potencia(  2 , cifras - i - 1  ) * Matematica.digitoN( binario , i )
        
    return numero
                
bina = int(  input( "Introduzca un numero binario: " )  )           
print( binarioDecimal( bina ) )

# Fin del programa