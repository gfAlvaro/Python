#_*_ coding=UTF-8 _*_
# testCuadrado.py
# programa de prueba para la clase Cuadrado
# @author Álvaro García Fuentes

from Cuadrado import Cuadrado

# Creamos dos cuadrados, los comparamos y los dibujamos
try:
	cuadrado1 = Cuadrado( 3 )
	print(  "Creado cuadrado1 con lado=" + str( cuadrado1.lado )  )
	cuadrado2 = Cuadrado( 3 )
	print(  "Creado cuadrado2 con lado=" + str( cuadrado2.lado )  )
	if( cuadrado1 == cuadrado2 ):
		print( "cuadrado1 y cuadrado2 son iguales" )
	else:
		print( "cuadrado1 y cuadrado2 no son iguales" )
	print( cuadrado1 )
	print( cuadrado2 )
except ArithmeticError:
	print( "ERROR: No se pudieron crear los cuadrados." )

# Intentamos crear un cuadrado con lado fuera del rango
try:
	cuadrado3 = Cuadrado( -1 )
	print(  "Creado cuadrado3 con lado=" + str( cuadrado3.lado )  )
except ArithmeticError:
	print( "ERROR: No se pudo crear cuadrado3, lado fuera de rango." )
	
# Fin del programa
