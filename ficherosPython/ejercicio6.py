#_*_ coding=UTF-8 _*_
# ejercicio6.java
# Programa que dice cuántas ocurrencias de una palabra hay en un
# fichero. Tanto el nombre del fichero como la palabra se deben pasar como
# argumentos en la línea de comandos.
# @author Alvaro Garcia Fuentes
		
import sys

lista = []
ocurrencias = 0
fichero = None

try:
	# Apertura del fichero
	fichero = open( sys.argv[1], 'r' );

	# Lectura del fichero
	lista = fichero.readlines()

	# Comparacion de palabras
	for i in lista:
		# nota: rstrip() debe usarse para comparar un string con un fichero.readline
		if( i.rstrip() == sys.argv[2] ):
			ocurrencias += 1
except:
	print( "ERROR: no se pudo abrir el fichero." )
	
try:
	# Cierre del fichero
	if( None != fichero ):
		fichero.close()
except:
	print( "ERROR: no se pudo cerrar el fichero." )
		
if( ocurrencias > 0 ):
	print( "La palabra " + sys.argv[2] + " tiene " + str(ocurrencias) + " ocurrencias." )
else:
	print( "La palabra " + sys.argv[2] + " no tiene ninguna ocurrencia." )

# Fin del programa
