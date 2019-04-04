#_*_ coding=UTF-8 _*_
# ejercicio1.py
# Programa que guarda en un fichero con nombre primos.dat los
# números primos que hay entre 1 y 500.
# @author Alvaro Garcia Fuentes
	
from io import open

# Funcion para determinar si un número es primo
# @param i
# @return boolean
def esPrimo( i ):
				
	for k in range( 2 , int(i/2+1) ):
		if( int(i) % k == 0 ):
			return False
			
	return True
			
lista = []
fichero = None
pw = None

# Se calculan los números primos entre 1 y 500
# y se almacenan en la lista
for i in range( 1, 500 ):			
	if(  esPrimo(i)  ):
		lista += [i]
		
try:
	# Se crea abre el fichero en modo escritura
	fichero = open( 'primos.dat' , 'w' )
	
	# Se escriben los datos en el fichero
	for i in lista:
		fichero.write( f"{i}" + '\n' )

	print( "Fichero creado con éxito." )
except:
	print( "ERROR: no se pudo crear el fichero." )

try:
	# Se cierra el fichero
	if( None != fichero ):
		fichero.close()
except:
	print( "ERROR: no se pudo cerrar el fichero." )
	
# Fin del programa
