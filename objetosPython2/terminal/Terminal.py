#_*_ coding:utf-8 _*_
# Terminal.py
# Definición de la clase Terminal
# @author Álvaro García Fuentes

class Terminal:
	
	# Constructor paramétrico
	def __init__( self , entrada ):
		self.__ip = entrada
		self.__tiempo = 0

	@property
	def tiempo( self ):
		return self.__tiempo

	@tiempo.setter
	def tiempo( self , tiempo ):
		self.__tiempo += tiempo

	@property	
	def ip( self ):
		return self.__ip
	
	# Método toString de la clase
	def __str__( self ):
		return "Nº " + self.ip + " - " + str( self.tiempo ) + "s de conversación"
	
	# Método para que un terminal llame a otro
	def llama( self , t , numero ):
		self.tiempo += numero
		t.tiempo += numero
	
	# Fin de la clase Terminal
