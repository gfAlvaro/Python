# _*_ coding=utf-8 _*_
# decimalABinario.py
# ejercicio 18 pg. 114 del libro de Java
# Programa que pasa de decimal a binario
# @author Álvaro García Fuentes
    
def decimalBinario( numero ):

    cociente = numero
    cadenaBinaria = ""

    while cociente != 1 :
        resto = cociente % 2
        cociente = int( cociente / 2 )
        cadenaBinaria = str( resto ) + cadenaBinaria

    cadenaBinaria = str( cociente ) + cadenaBinaria

    return int( cadenaBinaria )

#Programa principal        
numero = int(  input( "Introduzca un numero: " )  )
print(  decimalBinario( numero )  )
        
# Fin del programa