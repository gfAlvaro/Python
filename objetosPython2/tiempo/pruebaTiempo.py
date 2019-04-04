#_*_ coding:utf-8 _*_
# pruebaTiempo.py
# Programa para trabajar con horas
# usando la clase Tiempo definida en Tiempo.java
# @author Álvaro García Fuentes

from tiempo import Tiempo

if __name__ == '__main__':
		
	tiemp = Tiempo.Tiempo( 1 , 20 , 30 )
	tiempo2 = Tiempo.Tiempo( 10, 45, 5 )
		
	print( "tiempo: ", tiemp )
	print( "tiempo2: ", tiempo2 )
	tiemp.suma( tiempo2 )
	print( "tiempo + tiempo2: ", tiemp )
	tiempo2.resta( tiemp )
	print( "tiempo2 - tiempo: ", tiempo2 )

	# Fin del programa
