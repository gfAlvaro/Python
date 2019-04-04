#_*_ coding=UTF-8 _*_
# ejercicio4.py
# Programa que ordena alfabéticamente las palabras
# contenidas en un fichero de texto. El nombre del fichero que contiene las
# palabras se debe pasar como argumento en la línea de comandos. El nombre
# del fichero resultado es el mismo que el original añadiendo la coletilla
# sort , por ejemplo palabras_sort.txt . Cada palabra ocupa una línea.
# @author Alvaro Garcia Fuentes

import sys

lista = []
ficheroEntrada = None
ficheroSalida = None
		
#Se le quita la extensión al fichero para nombrar el fichero de salida
argumentos = sys.argv[1].split( '.' );
salida = argumentos[0];

try:
	# Apertura del fichero de entrada
	ficheroEntrada = open( f'{sys.argv[1]}', 'r' )

	# Lectura del fichero de entrada
	lista = ficheroEntrada.readlines()
except:
	print( "ERROR: no se pudo abrir el fichero de entrada." )
	
try:
	# Cierre del fichero de entrada
	if( None != ficheroEntrada ):
		ficheroEntrada.close()
except:
	print( "ERROR: no se pudo cerrar el fichero de entrada." )
		
#Se ordena alfabéticamente la lista
lista.sort();
		
# Creación del fichero de salida con la lista ordenada
try:
	ficheroSalida = open( f"{salida}_sort.txt" , 'w' )
	print( "Fichero de salida creado con éxito." )

	for i in lista:
		ficheroSalida.write(i)
except:
	print( "ERROR: no se pudo crear el fichero de salida." )

try:
	# Cierre del fichero de salida
	if( None != ficheroSalida ):
		ficheroSalida.close()
except:
	print( "ERROR: no se pudo cerrar el fichero de salida." )

# Fin del programa
