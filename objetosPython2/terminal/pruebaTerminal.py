#_*_ coding:utf-8 _*_
# pruebaTerminal.py
# @author Álvaro García Fuentes

from terminal import Terminal

t1 = Terminal.Terminal( "678 11 22 33" )
t2 = Terminal.Terminal( "644 74 44 69" )
t3 = Terminal.Terminal( "622 32 89 09" )
t4 = Terminal.Terminal( "664 73 98 18" )
print( t1 )
print( t2 )
t1.llama( t2 , 320 )
t1.llama( t3 , 200 )
print( t1 )
print( t2 )
print( t3 )
print( t4 )

# Fin del programa
