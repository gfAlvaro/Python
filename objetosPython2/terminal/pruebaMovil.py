#_*_ coding:utf-8 _*_
# pruebaMovil.py
# Programa para probar la clase Movil
# @author Álvaro García Fuentes

from terminal import Movil

m1 = Movil.Movil( "678 11 22 33" , "rata" )
m2 = Movil.Movil( "644 74 44 69" , "mono" )
m3 = Movil.Movil( "622 32 89 09" , "bisonte" )
print( m1 )
print( m2 )
m1.llama( m2 , 320 )
m1.llama( m3 , 200 )
m2.llama( m3 , 550 )
print( m1 )
print( m2 )
print( m3 )

# fin del programa
