# _*_ coding:utf-8 _*_
# Movil.py
# Definición de la clase Movil
# que hereda de la clase Terminal
# @author Álvaro García Fuentes

from terminal import Terminal

class Movil( Terminal.Terminal ):
	
	# Constructor paramétrico
	def __init__( self , ip , tipoTarifa ):

		super().__init__( ip )
		self.tipoTarifa = tipoTarifa
		
		if( tipoTarifa == "rata" ):
			self.precio = 0.06
		elif( tipoTarifa == "mono" ):
			self.precio = 0.12
		elif( tipoTarifa == "bisonte" ):
			self.precio = 0.30
		else:
			self.precio = 0
	
	# Método toString de la clase
	def __str__( self ):
		return super().__str__() + " - tarificados " + str( self.precio * self.tiempo / 60 ) + " euros"
	
	# Fin de la clase Movil

