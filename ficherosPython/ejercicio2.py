#_*_ coding=UTF-8 _*_
# ejercicio2.py
# Programa que lee el fichero creado en el ejercicio anterior y
# muestra los números por pantalla.
# @author Alvaro Garcia Fuentes
			
lista = []
fichero = None
br = None

try:
	# Apertura del fichero
	fichero = open( 'primos.dat', 'r' );
	
	# Lectura del fichero
	lista = fichero.readlines()  # lee línea
except:
	print( "ERROR: no se pudo abrir el fichero." )
	
try:
	# Cierre del fichero
	if( None != fichero ):
		fichero.close()   			
except: 
	print( "ERROR: no se pudo cerrar el fichero." )
		
for i in lista:
	print( f"{i}" , end="" )

# Fin del programa
