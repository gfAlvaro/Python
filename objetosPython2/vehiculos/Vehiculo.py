#_*_ coding:utf-8 _*_
# Vehiculo.py
# definicion de la clase Vehiculo
# @author Álvaro García Fuentes

class Vehiculo:	
	
	# atributos estaticos
	vehiculosCreados = 0
	kilometrosTotales = 0
	
	def __init__( self ):
		Vehiculo.vehiculosCreados = Vehiculo.vehiculosCreados + 1
		self.kilometrosRecorridos = 0

	def getKilometrosRecorridos( self ):
		return self.kilometrosRecorridos

	def setKilometrosRecorridos( self , recorridos ):
		self.kilometrosRecorridos = recorridos
		
	# Funcion que incrementa los kilometros recorridos y totales
	def andar( self ):
		self.setKilometrosRecorridos( self.getKilometrosRecorridos() + 1 )
		Vehiculo.kilometrosTotales += 1
		
	# Fin de la clase Vehiculo
